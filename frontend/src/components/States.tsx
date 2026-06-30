export function SkeletonGrid({ count = 8 }: { count?: number }) {
  return (
    <ul
      className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4"
      aria-hidden="true"
    >
      {Array.from({ length: count }).map((_, i) => (
        <li
          key={i}
          className="overflow-hidden rounded-2xl border border-violet/10 bg-white"
        >
          <div className="skeleton aspect-[4/3]" />
          <div className="flex flex-col gap-3 p-4">
            <div className="skeleton h-5 w-2/3 rounded" />
            <div className="skeleton h-3 w-full rounded" />
            <div className="skeleton h-3 w-5/6 rounded" />
            <div className="skeleton mt-1 h-5 w-1/2 rounded-full" />
          </div>
        </li>
      ))}
    </ul>
  );
}

export function ErrorState({ onRetry }: { onRetry: () => void }) {
  return (
    <div className="mx-auto max-w-md rounded-2xl border border-pumpkin/30 bg-pumpkin/5 p-8 text-center">
      <p className="text-3xl" aria-hidden="true">
        🧺
      </p>
      <h2 className="mt-3 font-display text-2xl font-semibold text-ink">
        We couldn&rsquo;t load the produce list
      </h2>
      <p className="mt-2 text-ink-soft">
        Something went wrong reaching the server. Check your connection and try
        again.
      </p>
      <button
        type="button"
        onClick={onRetry}
        className="mt-5 rounded-xl bg-pumpkin px-5 py-2.5 font-semibold text-white shadow-sm transition-colors hover:bg-pumpkin/90"
      >
        Try again
      </button>
    </div>
  );
}

export function EmptyState({ region }: { region: string }) {
  return (
    <div className="mx-auto max-w-md rounded-2xl border border-cyan/25 bg-cyan/5 p-8 text-center">
      <p className="text-3xl" aria-hidden="true">
        🌱
      </p>
      <h2 className="mt-3 font-display text-2xl font-semibold text-ink">
        Nothing&rsquo;s peaking in {region} right now
      </h2>
      <p className="mt-2 text-ink-soft">
        This season is quiet here. Try another region to see what&rsquo;s ripe
        elsewhere.
      </p>
    </div>
  );
}
