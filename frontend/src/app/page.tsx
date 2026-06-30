"use client";

import { useEffect, useState, useTransition } from "react";
import useSWR from "swr";
import { Hero } from "@/components/Hero";
import { RegionSelect } from "@/components/RegionSelect";
import { ProduceGrid } from "@/components/ProduceGrid";
import { SkeletonGrid, ErrorState, EmptyState } from "@/components/States";
import { getProduce } from "@/lib/api";
import {
  DEFAULT_REGION,
  isRegionId,
  regionName,
  type RegionId,
} from "@/data/regions";
import { getMonthName, getSeason } from "@/lib/season";

const REGION_STORAGE_KEY = "in-season:region";

export default function Home() {
  const [region, setRegion] = useState<RegionId>(DEFAULT_REGION);
  const [, startTransition] = useTransition();

  // Restore the last-picked region after mount (avoids hydration mismatch).
  useEffect(() => {
    const saved = localStorage.getItem(REGION_STORAGE_KEY);
    if (isRegionId(saved)) setRegion(saved);
  }, []);

  const { data, error, isLoading, mutate } = useSWR(
    ["produce", region],
    () => getProduce(region),
    { keepPreviousData: true, revalidateOnFocus: false },
  );

  function handleRegionChange(next: RegionId) {
    localStorage.setItem(REGION_STORAGE_KEY, next);
    startTransition(() => setRegion(next));
  }

  const now = new Date();
  const season = getSeason(now);
  const month = getMonthName(now);
  const produce = data?.produce ?? [];

  return (
    <main className="mx-auto w-full max-w-6xl flex-1 px-4 pb-20 pt-10 sm:px-6 sm:pt-16">
      <Hero season={season} month={month} region={regionName(region)} />

      <section className="mt-12">
        <div className="rounded-2xl border border-violet/10 bg-white/70 p-5 backdrop-blur-sm">
          <RegionSelect
            value={region}
            onChange={handleRegionChange}
            disabled={isLoading && !data}
          />
        </div>

        <div className="mt-8 flex items-baseline justify-between gap-4">
          <h2 className="font-display text-2xl font-semibold text-ink">
            In season now
          </h2>
          {data ? (
            <p className="text-sm font-medium text-ink-soft">
              {produce.length} {produce.length === 1 ? "item" : "items"}
            </p>
          ) : null}
        </div>

        <div className="mt-5">
          {error ? (
            <ErrorState onRetry={() => mutate()} />
          ) : isLoading && !data ? (
            <SkeletonGrid />
          ) : produce.length === 0 ? (
            <EmptyState region={regionName(region)} />
          ) : (
            <ProduceGrid produce={produce} currentSeason={season} />
          )}
        </div>
      </section>

      <footer className="mt-20 border-t border-violet/10 pt-6 text-center text-sm text-ink-soft">
        Seasonality varies by year and microclimate — treat this as a starting
        point, then ask your local growers.
      </footer>
    </main>
  );
}
