FROM ghcr.io/astral-sh/uv:trixie-slim AS build_venv

WORKDIR /app

COPY pyproject.toml uv.lock .python-version ./

RUN uv sync


# FROM python:3.13.7-slim-trixie AS run

# WORKDIR /app

# COPY --from=build_venv /app/.venv ./.venv

# COPY pyproject.toml uv.lock .python-version ./

COPY src src

# RUN ls -alF src

# activate venv
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

# Confirma que el ejecutable existe antes de intentar ejecutarlo
RUN ls -alF /app/.venv/bin/waitress-serve || echo "El archivo waitress-serve no se encontró en la ruta especificada."

ENTRYPOINT [ "waitress-serve", "--listen=*:8000", "--call", "src.main:main" ]
