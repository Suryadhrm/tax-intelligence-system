FROM python:3.11-slim

WORKDIR /app

# System deps needed for geopandas/psycopg2/xgboost
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gdal-bin libgdal-dev libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
