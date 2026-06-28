# Frontend — agent notes

Standard **Next.js 15** App Router + React 19 + TypeScript + Tailwind CSS v4.
(The repo runs on Node 18, so Next is pinned to 15.x rather than 16, which needs
Node 20+.) Nothing exotic here — the usual App Router conventions apply.

## Layout

- `src/app/page.tsx` — single-page client component; owns region + image-mode
  state, fetches via SWR.
- `src/app/api/produce/route.ts` — stand-in backend. Serves the curated dataset
  filtered by current season + region until a real backend exists.
- `src/lib/api.ts` — typed client. Reads `NEXT_PUBLIC_API_URL`; blank → same-origin
  `/api`. This is the seam to swap in the FastAPI backend.
- `src/data/` — `produce.ts` (dataset), `regions.ts` (US growing regions).
- `src/lib/season.ts` — month→season logic (matches PROJECT_SPEC.md).
- `src/components/` — presentational pieces (Hero, cards, selectors, states).

## Backend contract (for the future FastAPI service)

`GET /produce?region={id}` →
`{ season, month, region, produce: Produce[] }`, where `produce` is already
filtered to what's in season for the current month in that region.
