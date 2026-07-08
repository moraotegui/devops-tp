# Build
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

#Runtime
FROM python:3.11-slim

RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup --home /home/appuser appuser

WORKDIR /app

COPY --from=builder /root/.local /home/appuser/.local
COPY . .

ENV PATH=/home/appuser/.local/bin:$PATH \
    HOME=/home/appuser

ARG APP_VERSION=dev
ENV APP_VERSION=$APP_VERSION

RUN chown -R appuser:appgroup /app /home/appuser
USER appuser

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
