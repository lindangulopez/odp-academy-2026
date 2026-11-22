# Notebooks

## `wild_coast_seafloor.ipynb`

The Module 2 exercise: what the Wild Coast's seafloor has instead of seamounts, compared with South Africa's other coasts. Helper functions are in `wild_coast_analysis.py`.

### Run it

```bash
conda activate coa        # GeoPandas 1.1, matplotlib, Jupyter
cd notebooks
jupyter lab wild_coast_seafloor.ipynb
```

The first run downloads the data into `../data/` (about 160 MB, not committed): four GSFM layers from the Ocean Data Platform (open data, no key) and two Natural Earth layers. The results go to `../outputs/`.

### Data and licences

- Seafloor Geomorphic Features Map (GSFM): Seamounts, Canyons, Shelf and Slope, GRID-Arendal, CC BY 4.0, via the [Ocean Data Platform](https://app.hubocean.earth/). Harris, P.T., Macmillan-Lawler, M., Rupp, J., Baker, E.K. (2014), Geomorphology of the oceans, Marine Geology 352: 4-24, doi:10.1016/j.margeo.2014.01.011.
- [Natural Earth](https://www.naturalearthdata.com/) 1:10m coastline and countries, public domain.

The derived files in `../outputs/` keep the GSFM's CC BY 4.0 licence.
