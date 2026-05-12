# Etapa 1: builder
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --target=/app/packages -r requirements.txt

# Etapa 2: runtime
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /app/packages /app/packages
COPY app/ ./app/
ENV PYTHONPATH=/app/packages
EXPOSE 8000
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
