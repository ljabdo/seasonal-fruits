import {
  SEASON_GLYPH,
  seasonLabel,
  type Season,
} from "@/lib/season";

export function Hero({
  season,
  month,
  region,
}: {
  season: Season;
  month: string;
  region: string;
}) {
  return (
    <header className="mx-auto max-w-3xl text-center">
      <p className="text-sm font-semibold uppercase tracking-[0.2em] text-cyan">
        Seasonal produce guide
      </p>

      <h1 className="mt-3 font-display text-5xl font-semibold leading-[1.05] text-ink sm:text-6xl">
        Eat with the
        <br className="hidden sm:block" /> seasons
      </h1>

      <p className="mx-auto mt-5 max-w-xl text-lg leading-relaxed text-ink-soft">
        Produce tastes best and costs least at its peak. Pick your region to see
        the fruits and vegetables ripe near you right now — each with a quick tip
        for choosing the good ones.
      </p>

      {/* Signature: the season ribbon */}
      <div className="mt-8 inline-flex items-center gap-3 rounded-full bg-gradient-to-r from-jasmine via-canary to-pumpkin px-6 py-3 text-ink shadow-[0_10px_30px_-12px_rgba(250,131,52,0.7)]">
        <span className="text-2xl" aria-hidden="true">
          {SEASON_GLYPH[season]}
        </span>
        <span className="font-display text-lg font-semibold">
          It&rsquo;s {seasonLabel(season)} in {region}
        </span>
        <span className="hidden text-sm font-medium text-ink/70 sm:inline">
          · {month}
        </span>
      </div>
    </header>
  );
}
