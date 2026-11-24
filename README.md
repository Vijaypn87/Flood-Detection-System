# Flood Detection System

A web application that maps flood-affected areas by comparing Sentinel-1 SAR
satellite images captured before and after a flood event. Radar imagery sees
through cloud cover, so floods can be mapped even during monsoon storms.

| Pre-flood | Post-flood |
|:---:|:---:|
| ![Pre-flood SAR image](Pre_flood.png) | ![Post-flood SAR image](Post_flood.png) |

## Features

- **Regional analysis** for six flood-prone regions of India: Assam, Kerala,
  Mumbai, Delhi, Chennai and Bihar
- **Custom detection**: upload your own pre-flood and post-flood images
  (TIF, PNG or JPG)
- **Interactive map** with the detected flood extent overlaid in red
- **Impact statistics**: percentage of area inundated, with a summary chart
- **Data pipeline** that downloads Sentinel-1 imagery from Google Earth Engine
- **U-Net segmentation model** in PyTorch for training on labelled flood masks

## How it works

1. Pre-flood and post-flood Sentinel-1 (VV polarisation) images are loaded
   and converted to grayscale.
2. Both images are smoothed and compared pixel by pixel.
3. Pixels whose backscatter changed significantly are marked as flooded, and
   image borders with no data are masked out.
4. Small isolated pixels are removed, and the result is drawn on the map with
   area statistics.

## Tech stack

| Area | Tools |
|---|---|
| Backend | Python, Flask, Gunicorn |
| Image processing | OpenCV, NumPy, Pillow |
| Visualisation | Leaflet, Matplotlib |
| Satellite data | Google Earth Engine, Sentinel-1 SAR |
| Deep learning | PyTorch (U-Net) |
| Deployment | Docker |

## Project structure

```
├── app/app.py                  # Flask web application
├── templates/index.html        # Web page
├── static/                     # CSS and JavaScript
├── data/
│   ├── raw/                    # Full-resolution GeoTIFFs
│   └── web/                    # Compressed copies used by the app
├── models/unet_model.py        # U-Net architecture
├── src/                        # Data download, training and analysis
├── scripts/make_web_images.py  # Builds data/web from data/raw
└── Dockerfile
```

## Getting started

```bash
git clone https://github.com/Vijaypn87/Flood-Detection-System.git
cd Flood-Detection-System
pip install -r requirements.txt
python app/app.py
```

Open http://localhost:5000 in your browser.

## Docker

```bash
docker build -t flood-detection .
docker run -p 7860:7860 flood-detection
```

Open http://localhost:7860.

## Downloading data and training

```bash
pip install -r requirements-ml.txt
python src/get_gee_data.py       # download Sentinel-1 images (Google Earth Engine account required)
python scripts/make_web_images.py
python src/pipeline.py           # train the U-Net on data/train/images and data/train/masks
```
