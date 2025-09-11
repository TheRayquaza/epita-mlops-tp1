FROM python:3.12-slim

WORKDIR /app

USER root

ENV PATH=/home/appuser/.local/bin:$PATH
ENV MODEL_PATH=/app/regression.joblib

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY regression.joblib main.py index.html /app/

RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

CMD ["python3", "main.py"]
