# ---------- BUILDER STAGE ----------
FROM python:3.11-alpine3.19 AS builder

WORKDIR /app

RUN apk add --no-cache \
    build-base \
    postgresql-dev

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt


# ---------- FINAL STAGE ----------
FROM python:3.11-alpine3.19

WORKDIR /app

RUN apk add --no-cache postgresql-libs netcat-openbsd

RUN apk add --no-cache postgresql-libs netcat-openbsd

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY --from=builder /wheels /wheels
COPY requirements.txt .

RUN pip install --no-cache-dir /wheels/* \
    && rm -rf /wheels \
    && rm -rf /root/.cache

COPY . .

RUN mkdir -p /app/staticfiles /app/media

RUN chown -R appuser:appgroup /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh



USER appuser

ENTRYPOINT ["/entrypoint.sh"]

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2"]