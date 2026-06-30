export type Season = "winter" | "spring" | "summer" | "fall";

export const SEASONS: Season[] = ["winter", "spring", "summer", "fall"];

const MONTH_NAMES = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
] as const;

// Spec season logic: Winter Dec–Feb, Spring Mar–May, Summer Jun–Aug, Fall Sep–Nov.
export function getSeason(date: Date = new Date()): Season {
  const month = date.getMonth(); // 0–11
  if (month === 11 || month <= 1) return "winter";
  if (month <= 4) return "spring";
  if (month <= 7) return "summer";
  return "fall";
}

export function getMonthName(date: Date = new Date()): string {
  return MONTH_NAMES[date.getMonth()];
}

export const SEASON_GLYPH: Record<Season, string> = {
  winter: "❄",
  spring: "✿",
  summer: "☀",
  fall: "🍂",
};

export function seasonLabel(season: Season): string {
  return season.charAt(0).toUpperCase() + season.slice(1);
}
