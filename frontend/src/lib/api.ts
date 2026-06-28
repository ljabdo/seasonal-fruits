import type { Produce } from "@/data/produce";
import type { RegionId } from "@/data/regions";
import type { Season } from "@/lib/season";

export interface ProduceResponse {
  season: Season;
  month: string;
  region: RegionId;
  produce: Produce[];
}

// Empty -> same-origin /api (the bundled route handler). Set NEXT_PUBLIC_API_URL
// to the deployed backend's base URL to swap in the real API later.
const API_BASE = process.env.NEXT_PUBLIC_API_URL?.replace(/\/$/, "") ?? "";

export async function getProduce(region: RegionId): Promise<ProduceResponse> {
  const res = await fetch(`${API_BASE}/api/produce?region=${region}`);
  if (!res.ok) {
    throw new Error(`Request failed with status ${res.status}`);
  }
  return res.json();
}
