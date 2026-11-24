---
title: Flood Detection System
emoji: 🌊
colorFrom: blue
colorTo: red
sdk: docker
app_port: 7860
pinned: false
---

# Flood Detection System

A Flask web app that maps flooding by comparing pre-flood and post-flood
Sentinel-1 SAR images from Google Earth Engine. Pick one of six Indian
regions or upload your own image pair; the app highlights changed areas in
red on a Leaflet map and reports the share of the area affected.

Detection currently uses image differencing (grayscale difference with a
fixed threshold). A U-Net segmentation model for future training is in
`models/` and `src/`.

## Run locally

```bash
pip install -r requirements.txt
python app/app.py            # http://localhost:5000
```

Set `FLASK_DEBUG=1` to enable debug mode during development.

## Data

- `data/raw/` – full-resolution GeoTIFFs (~190 MB)
- `data/web/` – small copies (≤1024 px, ~6 MB) used by default

Regenerate the small copies after changing the raw data:

```bash
python scripts/make_web_images.py
```

Set `FLOOD_DATA_DIR=data/raw` to analyze the full-resolution files instead.

## Deploy (Docker / Hugging Face Spaces)

```bash
docker build -t flood-detection .
docker run -p 7860:7860 flood-detection   # http://localhost:7860
```

On Hugging Face, create a **Docker** Space and push this repository to it.
The metadata block at the top of this README configures the Space. Leave out
`data/raw/` (the image only uses `data/web/`), or track it with Git LFS,
because Hugging Face rejects files over 10 MB without LFS.

## Model training (optional)

```bash
pip install -r requirements-ml.txt
python src/get_gee_data.py   # download Sentinel-1 images (needs a GEE account)
python src/pipeline.py       # train the U-Net (needs data/train/images + masks)
```

## Known limitations

- The Chennai and Mumbai post-flood images are blank and need to be
  downloaded again.
- Flooded area in km² assumes a fixed 500 km² region, and map overlays use a
  fixed extent around each region's centre instead of the image's real bounds.
