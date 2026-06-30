import type { Produce } from "@/data/produce";
import type { Season } from "@/lib/season";
import { ProduceCard } from "@/components/ProduceCard";

export function ProduceGrid({
  produce,
  currentSeason,
}: {
  produce: Produce[];
  currentSeason: Season;
}) {
  return (
    <ul className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
      {produce.map((item) => (
        <li key={item.id} className="float-in">
          <ProduceCard item={item} currentSeason={currentSeason} />
        </li>
      ))}
    </ul>
  );
}
