# Seasonal Fruits API

A small FastAPI service that tells the frontend which produce is in season **right
now** for a given US growing region.

## Endpoint

```
GET /api/produce?region={id}   (alias: GET /produce)
```

`region` is one of: `pacific-northwest`, `southern-california`, `mountain-west`,
`midwest`, `northeast`, `south`, `southeast`, `hawaii`. An invalid or missing region
falls back to `southern-california`.

Response:

```json
{
  "season": "summer",
  "month": "June",
  "region": "southern-california",
  "produce": [
    {
      "id": "apricots",
      "name": "Apricots",
      "type": "fruit",
      "imageUrl": "/produce/apricot.jpg",
      "description": "Apricots is in season this summer in Southern California.",
      "seasons": ["summer"],
      "regions": ["mountain-west", "northeast", "southern-california"]
    }
  ]
}
```

The `produce` array is already filtered to the current season for the requested region
and sorted by name — the frontend renders it as-is.

`GET /health` returns `{"status": "ok"}`.

## Run locally

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Then: `curl 'http://localhost:8000/api/produce?region=southern-california'`

To point the frontend at it, set `NEXT_PUBLIC_API_URL=http://localhost:8000` in
`frontend/.env.local` and run the frontend dev server.

## Configuration (environment variables)

See `.env.example`:

- `CORS_ORIGINS` — comma-separated allowed origins (default `*`).
- `DATA_FILE` — path to the produce JSON (default: bundled `data/seasonal_produce.json`).
- `IMAGE_BASE_URL` — base path for `imageUrl` values (default `/produce`).
- `PORT` — listen port when run via `python -m app.main` (default `8000`).

## Data source & known limitations

Data comes from the USDA/ACL "Seasonal Produce List by Region" chart
(`data/seasonal_produce.json`). Because that chart only lists each item's name and type,
this service **synthesizes** the presentation fields the UI needs:

- **`imageUrl`** — root-relative path (default `/produce/<file>`) to a photo bundled in
  the frontend's `public/produce/` directory. Every item in the chart has a downloaded
  photo (originally from Spoonacular / Wikimedia Commons). Nothing is fetched from the
  web at runtime.
- **`description`** — generated sentence.

The chart's region taxonomy differs from the frontend's, so regions are mapped to the
closest overlap (`REGION_MAP` in `app/data.py`); `mountain-west` and `south` are
approximations. The chart also classifies a few vegetables (e.g. asparagus, okra) as
"fruit"; that quirk is inherited from the source data.
