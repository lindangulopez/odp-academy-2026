# From Download to Map in ArcGIS Online

**A tutorial, 22 November 2026.** The Module 2 lesson *From Download to Map (ArcGIS)* is written for ArcGIS Pro, which needs a desktop licence. I don't have one, so this is the same exercise in **ArcGIS Online**, in the browser, with the Map Viewer. It follows the eight steps of the QGIS lesson and uses the Wild Coast layers from [my Module 2 exercise](module-2-wild-coast.md).

You need an ArcGIS Online account (an organisation account, or a free ArcGIS Location Platform or Learn account) and an ODP account. Open ODP data needs no key.

!!! note "Credits"
    In ArcGIS Online, storing hosted layers and running analysis tools can use your organisation's credits. Uploading a few small GeoJSON files costs very little. The analysis tools (*Clip*, *Extract data*) cost more, so step 5 gives a route without them.

## 1. Choose a dataset and download it as GeoJSON

On the [ODP Catalog](https://app.hubocean.earth/catalog), open a dataset, for example *Seafloor Geomorphic Features Map (GSFM) - Seamounts*, and download it as **GeoJSON** under *Use Dataset*. If you can, filter first in the Explore table: ArcGIS Online is happier with a small file than a global one.

## 2. Add the file to a map

1. In ArcGIS Online, open **Map Viewer** (the *Map* button at the top).
2. In the left toolbar, **Add** (the layers icon with a +) → **Add layer from file**.
3. Drag the GeoJSON in. Choose **Create a hosted feature layer and add it to the map**, give it a clear name and click **Create and add to map**.
4. Change the basemap with **Basemap** in the left toolbar, for example *Oceans*.

The layer now sits in **Content** as a hosted feature layer, so you can reuse it in other maps.

## 3. For large datasets, connect instead of downloading

The world's canyons or shelves are too big to upload comfortably. Connect to them live instead:

1. **Add** → **Add layer from URL**.
2. Paste ODP's OGC API Features address: `https://api.hubocean.earth/api/features`
3. ArcGIS detects an **OGC API - Features** service. Pick the collection by its ODP dataset id, for example `f9ac8c35-68f8-4c4c-b033-86188608507d` for GSFM Canyons, and click **Add to map**.

!!! warning "Count your features"
    In QGIS, the same connection stopped at 1,000 features out of 9,477 until I raised the page size. In ArcGIS, open the layer's **attribute table** (the *Show table* button) and compare the feature count with the number on the ODP dataset page. If it is short, use a download instead, filtered to your area.

Vector tiles, the lesson's third route, are for looking only. If ODP gives a vector tile link under *Use Dataset*, add it the same way with *Add layer from URL*. If ArcGIS refuses it, skip it: you don't need it for the rest.

## 4. Look at it on the map

Zoom to your area. A live layer loads what you see, so it can be slow at world scale and faster close up.

## 5. Keep only your area of interest

**Route A, no credits (recommended).** Clip in QGIS or Python and upload the result. My clipped Wild Coast layers are ready in the repository, in [`outputs/qgis/`](https://github.com/lindangulopez/odp-academy-2026/tree/main/outputs/qgis): `wild_coast_seamounts`, `wild_coast_canyons`, `wild_coast_shelf` and the box `wild_coast_aoi`. Download them (*Raw* → save) and add each one as in step 2.

**Route B, in ArcGIS Online, uses credits.**

1. Draw the area: **Add** → **Create sketch layer**, then draw a rectangle around your area.
2. **Analysis** (right toolbar) → **Tools** → **Clip layer**. Input: the large layer. Clip: the sketch. Give the result a name, check the **estimated credits**, then **Run**.
3. The clipped layer appears in the map and in *Content*.

## 6. Restyle and reorder

Select a layer, then **Styles** in the right toolbar:

- **Canyons**: choose the field `type` → style **Types (unique symbols)**. Give *shelf incising* a solid orange fill and *blind* an orange outline with no fill.
- **Seamounts**: one colour, or the field `Height` → **Counts and amounts (colour)**.
- **Shelf**: a light blue fill at about 60% transparency (**Properties** → *Transparency*).

Drag the layers in the **Layers** panel so the small features (seamounts, canyons) sit above the shelf.

## 7. Remove the global layers

In the **Layers** panel, open the layer's menu (⋯) → **Remove** for each large live layer. Your clipped layers and the basemap stay.

## 8. Save and share

1. **Save and open** (left toolbar) → **Save as**: a title, tags (*ODP, ocean data, Module 2*) and a one-line summary.
2. **Share map** (left toolbar): choose who can see it. *Everyone (public)* gives a link you can paste into ODP or your course group.
3. The layers used by a public map must be shared at the same level: ArcGIS offers to update them when you share.

The lesson shares maps through ODP, and later SeaSketch, rather than printed layouts, so you don't need a print layout.

## Check it worked

- The clipped layers show the same counts as QGIS: **1 seamount and 24 canyons** in the Wild Coast box.
- The map opens in a private browser window if you shared it publicly.

My first quick test: [test-ODP](https://scgismaps.maps.arcgis.com/apps/mapviewer/index.html?webmap=d3ca11ce0490483a8960d364291a1f6a).
