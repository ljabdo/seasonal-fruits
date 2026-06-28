import { REGIONS, type RegionId } from "@/data/regions";

export function RegionSelect({
  value,
  onChange,
  disabled,
}: {
  value: RegionId;
  onChange: (region: RegionId) => void;
  disabled?: boolean;
}) {
  return (
    <div className="flex flex-col gap-2.5">
      <span className="text-xs font-semibold uppercase tracking-wide text-ink-soft">
        Your location
      </span>
      <div role="group" aria-label="Select your region" className="flex flex-wrap gap-2">
        {REGIONS.map((region) => {
          const active = region.id === value;
          return (
            <button
              key={region.id}
              type="button"
              aria-pressed={active}
              disabled={disabled}
              onClick={() => onChange(region.id)}
              className={`rounded-full border px-4 py-2 text-sm font-semibold transition-colors disabled:cursor-not-allowed disabled:opacity-60 ${
                active
                  ? "border-cyan bg-cyan text-white shadow-sm"
                  : "border-violet/15 bg-white text-ink-soft hover:border-cyan/50 hover:text-ink"
              }`}
            >
              {region.name}
            </button>
          );
        })}
      </div>
    </div>
  );
}
