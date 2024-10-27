FROM python:3.10-slim

COPY app /src

WORKDIR /src

# Встановлення залежностей системи
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

CMD bash -c "sleep 15 && python create_db.py && python populate_tables.py && python run_queries.py"

