"""Wild Coast seafloor analysis, shared by the notebook.

Functions are kept small so each step can be explained in the notebook.
All distances are computed in Africa Albers Equal Area (ESRI:102022).
At the scale of this study (under about 1,000 km) distances in this
projection are within a few percent of true distances.
"""

from pathlib import Path
import json
import urllib.request

import geopandas as gpd
import pandas as pd
from shapely.geometry import box, Point

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs"

CRS_METRIC = "ESRI:102022"  # Africa Albers Equal Area

# ODP datasets from the Seafloor Geomorphic Features Map (GSFM) collection,
# GRID-Arendal, CC BY 4.0, Harris et al. (2014).
ODP_FEATURES = "https://api.hubocean.earth/api/features/collections/{id}/items?limit=10000"
GSFM_LAYERS = {
    "seamounts": "027a6438-2d81-4a6e-91f3-e939e79f7cdd",
    "canyons": "f9ac8c35-68f8-4c4c-b033-86188608507d",
    "shelf": "9dc7ec46-f1db-482f-81aa-c5957296525e",
    "slope": "ac8739f5-f616-488e-b23f-e6a715868cba",
}
NATURAL_EARTH = {
    "coastline": "https://naciscdn.org/naturalearth/10m/physical/ne_10m_coastline.zip",
    "countries": "https://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_0_countries.zip",
}

# Study area: South Africa's mainland coast and the sea off it (lon/lat).
STUDY_BBOX = (14.0, -40.0, 36.0, -25.0)

# Coast reaches, split at river mouths and capes (lon, lat).
# West: Orange River mouth to Cape Point
# South: Cape Point to the Great Kei River mouth
# Wild Coast: Great Kei River mouth to the Mtamvuna River mouth
# KwaZulu-Natal: Mtamvuna River mouth to Kosi Bay (Mozambique border)
CAPE_POINT = (18.47, -34.36)
KEI_MOUTH = (28.38, -32.68)
MTAMVUNA_MOUTH = (30.19, -31.08)
REACH_ORDER = ["West", "South", "Wild Coast", "KwaZulu-Natal"]


def download(url, path):
    """Download a file once and keep it in data/."""
    path = Path(path)
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Downloading {url}")
        urllib.request.urlretrieve(url, path)
    return path


def load_gsfm(name):
    """Load one GSFM layer from ODP (open data, no API key), clipped to the study area.

    ODP's bbox filter returned features from outside the box when tested
    (22 Nov 2026), so the whole layer is downloaded once and clipped here.
    """
    path = download(ODP_FEATURES.format(id=GSFM_LAYERS[name]), DATA / f"gsfm_{name}.geojson")
    layer = gpd.read_file(path)
    return gpd.clip(layer, box(*STUDY_BBOX)).reset_index(drop=True)


def load_south_africa():
    """South Africa's mainland outline, without the Prince Edward Islands."""
    path = download(NATURAL_EARTH["countries"], DATA / "ne_10m_admin_0_countries.zip")
    countries = gpd.read_file(path)
    rsa = countries[countries["ADM0_A3"] == "ZAF"]
    return gpd.clip(rsa, box(*STUDY_BBOX))[["ADMIN", "geometry"]]


def load_coastline(rsa):
    """South Africa's mainland coastline as lines, in the metric CRS."""
    path = download(NATURAL_EARTH["coastline"], DATA / "ne_10m_coastline.zip")
    coast = gpd.read_file(path).to_crs(CRS_METRIC)
    land = rsa.to_crs(CRS_METRIC).buffer(2_000).union_all()
    coast = gpd.clip(coast, land)
    coast = coast[coast.geometry.length > 0]
    return coast[["geometry"]].reset_index(drop=True)


def reach_of(lon, lat):
    """Name the coast reach that a coastal point belongs to."""
    if lon <= CAPE_POINT[0]:
        return "West"
    if lon <= KEI_MOUTH[0]:
        return "South"
    if lat <= MTAMVUNA_MOUTH[1]:
        return "Wild Coast"
    return "KwaZulu-Natal"


def coast_points(coast, spacing_m=10_000):
    """Points every `spacing_m` metres along the coastline, each tagged with its reach."""
    points = []
    for line in coast.geometry.explode(index_parts=False):
        n = int(line.length // spacing_m)
        for i in range(n + 1):
            points.append(line.interpolate(i * spacing_m))
    pts = gpd.GeoDataFrame(geometry=points, crs=CRS_METRIC)
    lonlat = pts.to_crs(4326)
    pts["lon"] = lonlat.geometry.x
    pts["lat"] = lonlat.geometry.y
    pts["reach"] = [reach_of(x, y) for x, y in zip(pts["lon"], pts["lat"])]
    return pts


def nearest_distance_km(points, features):
    """Distance in km from each point to the nearest feature."""
    joined = gpd.sjoin_nearest(points[["geometry"]], features[["geometry"]], distance_col="d")
    # sjoin_nearest repeats a point when two features are equally near
    d = joined.groupby(level=0)["d"].min()
    return (d / 1000).reindex(points.index)


def assign_to_reach(features, points, coast, max_km):
    """Give each feature the reach of its nearest coast point, if within `max_km`.

    `coast_km` is the distance from the feature to the coastline itself,
    not to the nearest sample point.
    """
    joined = gpd.sjoin_nearest(
        features, points[["reach", "geometry"]], distance_col="point_m", max_distance=max_km * 1000
    )
    joined = joined[~joined.index.duplicated(keep="first")]
    shoreline = coast.union_all()
    joined["coast_km"] = joined.geometry.distance(shoreline) / 1000
    return joined.drop(columns=["index_right", "point_m"])
