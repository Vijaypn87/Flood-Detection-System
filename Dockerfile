# Container for the Flask web app (works on Hugging Face Spaces, Cloud Run,
# Render, Railway, ...). Uses the small images in data/web.
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MPLCONFIGDIR=/tmp/matplotlib \
    PORT=7860

# Hugging Face Spaces runs containers as user 1000.
RUN useradd -m -u 1000 user
WORKDIR /home/user/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=user app ./app
COPY --chown=user templates ./templates
COPY --chown=user static ./static
COPY --chown=user data/web ./data/web

USER user
EXPOSE 7860

# One worker keeps memory low; analysis can take a few seconds.
CMD gunicorn --bind 0.0.0.0:${PORT} --workers 1 --threads 4 --timeout 120 app.app:app
