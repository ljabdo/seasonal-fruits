import Image from "next/image";
import type { Produce } from "@/data/produce";
import {
  SEASON_GLYPH,
  SEASONS,
  seasonLabel,
  type Season,
} from "@/lib/season";

const TYPE_TAG: Record<Produce["type"], { label: string; className: string }> = {
  fruit: { label: "Fruit", className: "bg-pumpkin/15 text-pumpkin" },
  vegetable: { label: "Vegetable", className: "bg-cyan/15 text-cyan" },
};

export function ProduceCard({
  item,
  currentSeason,
}: {
  item: Produce;
  currentSeason: Season;
}) {
  const tag = TYPE_TAG[item.type];

  return (
    <article className="group flex flex-col overflow-hidden rounded-2xl border border-violet/10 bg-white shadow-[0_1px_0_rgba(39,16,51,0.04),0_12px_28px_-18px_rgba(39,16,51,0.35)] transition-transform duration-200 hover:-translate-y-1">
      <div className="relative aspect-[4/3] overflow-hidden">
        <Image
          src={item.imageUrl}
          alt={item.name}
          fill
          sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 25vw"
          className="object-cover transition-transform duration-300 group-hover:scale-[1.04]"
        />
      </div>

      <div className="flex flex-1 flex-col gap-2 p-4">
        <div className="flex items-center justify-between gap-2">
          <h3 className="font-display text-xl font-semibold text-ink">
            {item.name}
          </h3>
          <span
            className={`shrink-0 rounded-full px-2 py-0.5 text-xs font-semibold ${tag.className}`}
          >
            {tag.label}
          </span>
        </div>

        <p className="flex-1 text-sm leading-relaxed text-ink-soft">
          {item.description}
        </p>

        <ul className="mt-1 flex flex-wrap gap-1.5" aria-label="In season during">
          {SEASONS.filter((s) => item.seasons.includes(s)).map((s) => {
            const isNow = s === currentSeason;
            return (
              <li
                key={s}
                className={`rounded-full px-2 py-0.5 text-[11px] font-medium ${
                  isNow
                    ? "bg-cyan text-white"
                    : "bg-violet/5 text-ink-soft"
                }`}
              >
                <span aria-hidden="true">{SEASON_GLYPH[s]}</span>{" "}
                {seasonLabel(s)}
                {isNow ? " · now" : ""}
              </li>
            );
          })}
        </ul>
      </div>
    </article>
  );
}
