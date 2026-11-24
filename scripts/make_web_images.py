"""Create small copies of the satellite images for deployment.

The web app resizes every image to 512x512 before analysis, so the
full-resolution GeoTIFFs in data/raw (~190 MB) aren't needed online.
This script writes copies whose longest side is at most MAX_SIDE pixels
to data/web, compressed with deflate. File names are kept, so the app can
read either folder.

Usage (from the repo root):
    python scripts/make_web_images.py
"""
import os
import sys

from PIL import Image

Image.MAX_IMAGE_PIXELS = None  # trusted local files only

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_DIR = os.path.join(BASE_DIR, "data", "raw")
DST_DIR = os.path.join(BASE_DIR, "data", "web")
MAX_SIDE = 1024


def main():
    total_in = total_out = 0
    for sub in ("pre_flood", "post_flood"):
        src_sub = os.path.join(SRC_DIR, sub)
        dst_sub = os.path.join(DST_DIR, sub)
        os.makedirs(dst_sub, exist_ok=True)
        for name in sorted(os.listdir(src_sub)):
            if not name.lower().endswith((".tif", ".tiff", ".png", ".jpg")):
                continue
            src = os.path.join(src_sub, name)
            dst = os.path.join(dst_sub, name)
            with Image.open(src) as img:
                img.load()
                if img.mode not in ("L", "RGB"):
                    img = img.convert("RGB")
                img.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
                if name.lower().endswith((".tif", ".tiff")):
                    img.save(dst, compression="tiff_deflate")
                else:
                    img.save(dst)
                size = img.size
            in_b, out_b = os.path.getsize(src), os.path.getsize(dst)
            total_in += in_b
            total_out += out_b
            print(f"{sub}/{name}: {size[0]}x{size[1]}  {in_b/1e6:.1f} MB -> {out_b/1e6:.2f} MB")
    print(f"Total: {total_in/1e6:.1f} MB -> {total_out/1e6:.2f} MB in {DST_DIR}")


if __name__ == "__main__":
    sys.exit(main())
