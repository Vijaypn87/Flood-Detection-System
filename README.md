<div align="center">

# 🌊 Flood Detection System

**Mapping flood-affected areas from Sentinel-1 SAR satellite imagery**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20App-2ea44f?style=for-the-badge&logo=render&logoColor=white)](https://flood-detection-system-m2iq.onrender.com/)

### Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Google Earth Engine](https://img.shields.io/badge/Google%20Earth%20Engine-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Leaflet](https://img.shields.io/badge/Leaflet-199900?style=for-the-badge&logo=leaflet&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=black)

</div>

---

## Overview

A web application that detects flooded areas by comparing Sentinel-1 radar
images taken before and after a flood. Radar sees through clouds, so floods
can be mapped even during heavy monsoon rain.

| Pre-flood | Post-flood |
|:---:|:---:|
| ![Pre-flood SAR image](Pre_flood.png) | ![Post-flood SAR image](Post_flood.png) |

## Features

- **Regional analysis** of six flood-prone regions in India
- **Custom detection** from your own pre-flood and post-flood images
- **Interactive map** with the flood extent highlighted in red
- **Impact statistics** showing the percentage of area inundated

## How It Works

1. Sentinel-1 images are downloaded from Google Earth Engine.
2. Pre-flood and post-flood images are converted to grayscale and smoothed.
3. Pixels with a significant change in radar backscatter are marked as flooded.
4. Noise is removed and the flood mask is shown on the map with statistics.

## Run Locally

```bash
git clone https://github.com/Vijaypn87/Flood-Detection-System.git
cd Flood-Detection-System
pip install -r requirements.txt
python app/app.py
```

Open **http://localhost:5000** in your browser.
