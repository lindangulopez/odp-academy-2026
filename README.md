# ODP Academy, Working with Ocean Data on ODP

My progress in *Working with Ocean Data on ODP*, a free online course from HUB Ocean, WIOMSA and SeaSketch, 12 November to 18 December 2026.

Site: https://lindangulopez.github.io/odp-academy-2026/

## Build locally

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve
```

The pages are in `docs/`. A push to `main` rebuilds and publishes the site through GitHub Actions. Course downloads (`data/`) and screenshots stay local and are not committed.
