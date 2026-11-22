# Module 2: GIS

**In progress, started 22 November 2026.** Opened on Thursday 19 November. 4 of 8 lessons done. Exercise: [The Wild Coast seafloor](module-2-wild-coast.md).

## Lessons

### Start here

- [x] Welcome to GIS
- [x] Choose your tool: QGIS or ArcGIS (I use QGIS)
- [x] Data formats and connections, with an assignment (submitted)

### GIS: QGIS

- [x] Installing QGIS
- [ ] From Download to Map (QGIS)

### GIS: ArcGIS

- [ ] From Download to Map (ArcGIS), the alternative path; I skip it if time runs short

A quick test of ODP data in ArcGIS Online, 22 November 2026: [test-ODP](https://scgismaps.maps.arcgis.com/apps/mapviewer/index.html?webmap=d3ca11ce0490483a8960d364291a1f6a).

### Lab 2 and wrap-up

- [ ] Lab 2: Map my place
- [ ] Final Remarks

## Notes: data formats and connections

ODP data comes as files, and a GIS can also connect to it live.

| Format | Best suited for |
| --- | --- |
| **CSV** | General tables. It opens in any spreadsheet, but it is not the best choice for maps. |
| **GeoJSON** | Shapes and their attributes in one file. It opens directly in QGIS, geojson.io and most web maps. Used in Lab 2. |
| **Parquet** | Compact and fast for large tables. Used in the Code module. |

Not every dataset offers every format; the dataset page shows which ones it has.

**Three ways to read ODP data in a GIS**, all on open standards, so the same data works in QGIS, ArcGIS, web maps and SeaSketch:

1. **Download** a file from the dataset page, or from the Explore table after filtering. A copy that works anywhere, offline too. Best for small or filtered data.
2. **OGC API Features**: a live connection to the shapes and their data. One connection gives every dataset you can see on ODP. Best when you need only your own area of a large dataset.
3. **Vector tiles**: map tiles that draw fast at any zoom. Best for looking at very large datasets, not for analysis. ODP's Map Explorer is built on them.

In short: look with vector tiles, then take your area with a filtered download or OGC API Features. The links are under *Use Dataset* on each dataset page. Open data needs no login or key; private datasets need your API key from your ODP account page.

## The dataset I downloaded: global seamounts

For the assignment I downloaded one ODP dataset in all three formats. It is a global layer of **9,951 seamounts**, all polygons (31 of them multipolygons), from 75° S to 77° N. Each seamount has an ID, a peak depth (2 to 7,589 m, median 2,314 m), a height above the seafloor (953 to 7,570 m) and an area (3 to 15,509 km², median 592 km²). The count and the 1,000 m height threshold match the seamount layer of the global seafloor geomorphic features map by Harris et al. (2014).

The same 9,951 seamounts take three different sizes:

| File | Size | How the shapes are stored |
| --- | --- | --- |
| CSV | 9.2 MB | One text column, `geometry`, with each polygon written as WKT, `POLYGON ((lon lat, …))` |
| GeoJSON | 10.8 MB | A `FeatureCollection`: each seamount is a feature with its geometry as nested coordinate arrays, and its attributes under `properties` |
| Parquet | 6.1 MB | Binary and compressed, column by column |

My next step is to open the CSV and the GeoJSON side by side in QGIS before I write the assignment answer.
