# Seasonal Fruits — Frontend

A single-page Next.js app that shows which fruits and vegetables are in season
right now, filtered by your region. Each item has a photo (or illustration) and
a quick tip for picking good ones.

## Stack

- Next.js 15 (App Router) · React 19 · TypeScript
- Tailwind CSS v4
- SWR for data fetching
- Fonts: Fraunces (display) + Hanken Grotesk (body)

## Run it

```bash
npm install
cp .env.example .env.local   # optional
npm run dev                  # http://localhost:3000
```

## Data source

The page fetches `GET /api/produce?region={id}`. By default that's a bundled
Next.js **route handler** (`src/app/api/produce/route.ts`) serving a curated
dataset, so the app works with no backend.

To point at a real backend, set `NEXT_PUBLIC_API_URL` to its base URL. The
backend must implement the same contract:

```
GET /produce?region={id}
→ { season, month, region, produce: Produce[] }
```

`produce` should already be filtered to what's in season for the current month
in the requested region. See `src/data/produce.ts` for the `Produce` shape and
`src/data/regions.ts` for valid region ids.

## Image modes

The card style toggle (Photos / Illustrated) is intentional: it lets you compare
real keyword-based photos against emoji illustrations and choose the final look.
Once decided, drop the unused mode and the toggle.
