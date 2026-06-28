"""FastAPI app serving the seasonal produce API the frontend consumes.

Contract (frontend/src/lib/api.ts): GET /api/produce?region={id}
  -> { season, month, region, produce: Produce[] }

Config via environment variables:
  CORS_ORIGINS  comma-separated allowed origins (default "*")
  DATA_FILE     path to the produce JSON (see data.py; default bundled copy)
  PORT          used by the __main__ runner below (default 8000)
"""

import os

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from . import data

app = FastAPI(title="Seasonal Fruits API", version="1.0.0")

_origins = [o.strip() for o in os.getenv("CORS_ORIGINS", "*").split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=_origins or ["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/api/produce")
@app.get("/produce")  # alias (covers the frontend AGENTS.md note)
def produce(region: str | None = Query(default=None)) -> dict:
    return data.get_produce(region)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
