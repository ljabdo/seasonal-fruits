export type RegionId =
  | "pacific-northwest"
  | "southern-california"
  | "mountain-west"
  | "midwest"
  | "northeast"
  | "south"
  | "southeast"
  | "hawaii";

export interface Region {
  id: RegionId;
  name: string;
}

export const REGIONS: Region[] = [
  { id: "pacific-northwest", name: "Pacific Northwest" },
  { id: "southern-california", name: "Southern California" },
  { id: "mountain-west", name: "Mountain West" },
  { id: "midwest", name: "Midwest" },
  { id: "northeast", name: "Northeast" },
  { id: "south", name: "South" },
  { id: "southeast", name: "Southeast" },
  { id: "hawaii", name: "Hawaii" },
];

export const DEFAULT_REGION: RegionId = "southern-california";

const REGION_NAME_BY_ID = new Map(REGIONS.map((r) => [r.id, r.name]));

export function regionName(id: RegionId): string {
  return REGION_NAME_BY_ID.get(id) ?? "your area";
}

export function isRegionId(value: string | null): value is RegionId {
  return value != null && REGION_NAME_BY_ID.has(value as RegionId);
}
