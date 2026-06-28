import { NextResponse } from "next/server";
import { PRODUCE } from "@/data/produce";
import { DEFAULT_REGION, isRegionId } from "@/data/regions";
import { getMonthName, getSeason } from "@/lib/season";

// Stand-in for the future FastAPI backend. The frontend hits this same-origin
// route until NEXT_PUBLIC_API_URL points somewhere else. Contract:
// GET /api/produce?region={id} -> { season, month, region, produce[] }
export function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const regionParam = searchParams.get("region");
  const region = isRegionId(regionParam) ? regionParam : DEFAULT_REGION;

  const now = new Date();
  const season = getSeason(now);

  const produce = PRODUCE.filter(
    (item) => item.seasons.includes(season) && item.regions.includes(region),
  ).sort((a, b) => a.name.localeCompare(b.name));

  return NextResponse.json({
    season,
    month: getMonthName(now),
    region,
    produce,
  });
}
