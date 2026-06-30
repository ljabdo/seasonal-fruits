import type { Season } from "@/lib/season";
import type { RegionId } from "@/data/regions";

export type ProduceType = "fruit" | "vegetable";

export interface Produce {
  id: string;
  name: string;
  type: ProduceType;
  imageUrl: string;
  description: string;
  seasons: Season[];
  regions: RegionId[];
}

// Photos are bundled locally under public/produce/ (downloaded from Spoonacular's
// ingredient CDN and Wikimedia Commons) and served same-origin — nothing is fetched
// from the web at runtime.
function photo(file: string): string {
  return `/produce/${file}`;
}

const ALL_MAINLAND: RegionId[] = [
  "pacific-northwest",
  "southern-california",
  "mountain-west",
  "midwest",
  "northeast",
  "south",
  "southeast",
];

export const PRODUCE: Produce[] = [
  {
    id: "strawberry",
    name: "Strawberry",
    type: "fruit",
    imageUrl: photo("strawberries.jpg"),
    description:
      "Pick berries that are fully red to the stem — strawberries stop ripening the moment they're picked.",
    seasons: ["spring", "summer"],
    regions: ALL_MAINLAND,
  },
  {
    id: "watermelon",
    name: "Watermelon",
    type: "fruit",
    imageUrl: photo("watermelon.jpg"),
    description:
      "A creamy-yellow patch where it rested on the ground means it ripened in the field, not on a truck.",
    seasons: ["summer"],
    regions: ["southern-california", "south", "southeast", "midwest", "mountain-west"],
  },
  {
    id: "peach",
    name: "Peach",
    type: "fruit",
    imageUrl: photo("peaches.jpg"),
    description:
      "Smell the stem end — a ripe peach is fragrant and gives slightly to a gentle press.",
    seasons: ["summer"],
    regions: ["southern-california", "south", "southeast", "northeast", "midwest"],
  },
  {
    id: "cherry",
    name: "Cherry",
    type: "fruit",
    imageUrl: photo("cherries.jpg"),
    description:
      "Look for firm, glossy fruit with green, flexible stems still attached. The season is short, so don't wait.",
    seasons: ["summer"],
    regions: ["pacific-northwest", "mountain-west", "northeast", "midwest"],
  },
  {
    id: "blueberry",
    name: "Blueberry",
    type: "fruit",
    imageUrl: photo("blueberries.jpg"),
    description:
      "A silvery, dusty bloom on the skin is a good sign — it's natural and means they haven't been handled much.",
    seasons: ["summer"],
    regions: ["northeast", "southeast", "pacific-northwest", "midwest", "south"],
  },
  {
    id: "apricot",
    name: "Apricot",
    type: "fruit",
    imageUrl: photo("apricot.jpg"),
    description:
      "Apricots ripen only on the tree. Choose deep-orange, fragrant fruit with no green tinge.",
    seasons: ["summer"],
    regions: ["southern-california", "mountain-west", "pacific-northwest"],
  },
  {
    id: "fig",
    name: "Fig",
    type: "fruit",
    imageUrl: photo("figs.jpg"),
    description:
      "Ripe figs are soft, heavy, and may bead a drop of nectar at the base. They bruise fast, so handle gently.",
    seasons: ["summer", "fall"],
    regions: ["southern-california", "south", "southeast"],
  },
  {
    id: "grape",
    name: "Grape",
    type: "fruit",
    imageUrl: photo("red-grapes.jpg"),
    description:
      "Grapes won't sweeten after picking. Look for plump fruit firmly attached to green, pliable stems.",
    seasons: ["summer", "fall"],
    regions: ["southern-california", "pacific-northwest", "mountain-west"],
  },
  {
    id: "plum",
    name: "Plum",
    type: "fruit",
    imageUrl: photo("plum.jpg"),
    description:
      "A ripe plum yields slightly at the tip. The white bloom on the skin is natural and worth keeping.",
    seasons: ["summer"],
    regions: ["southern-california", "pacific-northwest", "northeast"],
  },
  {
    id: "raspberry",
    name: "Raspberry",
    type: "fruit",
    imageUrl: photo("raspberries.jpg"),
    description:
      "Check the bottom of the carton for stains — a sign of crushed fruit underneath. Eat within a day or two.",
    seasons: ["summer"],
    regions: ["pacific-northwest", "northeast", "mountain-west"],
  },
  {
    id: "cantaloupe",
    name: "Cantaloupe",
    type: "fruit",
    imageUrl: photo("cantaloupe.jpg"),
    description:
      "Ripe melons smell sweet at the stem end and feel heavy for their size, with a slight give where the vine attached.",
    seasons: ["summer"],
    regions: ["southern-california", "midwest", "south"],
  },
  {
    id: "apple",
    name: "Apple",
    type: "fruit",
    imageUrl: photo("apple.jpg"),
    description:
      "There are more than 7,500 varieties worldwide. Choose firm fruit with taut, unbruised skin.",
    seasons: ["fall", "winter"],
    regions: ["pacific-northwest", "northeast", "midwest", "mountain-west"],
  },
  {
    id: "pear",
    name: "Pear",
    type: "fruit",
    imageUrl: photo("pear.jpg"),
    description:
      "Pears ripen from the inside out. Buy them firm and let them soften at the neck on the counter.",
    seasons: ["fall", "winter"],
    regions: ["pacific-northwest", "northeast", "mountain-west"],
  },
  {
    id: "pomegranate",
    name: "Pomegranate",
    type: "fruit",
    imageUrl: photo("pomegranate.jpg"),
    description:
      "Heavier fruit holds more juice. Look for a deep color and a leathery skin that's taut, not shriveled.",
    seasons: ["fall", "winter"],
    regions: ["southern-california", "mountain-west"],
  },
  {
    id: "orange",
    name: "Orange",
    type: "fruit",
    imageUrl: photo("orange.jpg"),
    description:
      "Skin color isn't a ripeness cue for citrus. Pick fruit that feels heavy and firm for its size.",
    seasons: ["winter", "spring"],
    regions: ["southern-california", "south", "southeast"],
  },
  {
    id: "cranberry",
    name: "Cranberry",
    type: "fruit",
    imageUrl: photo("cranberries.jpg"),
    description:
      "Fresh cranberries should be firm and bounce. Discard any that are soft, sticky, or shriveled.",
    seasons: ["fall"],
    regions: ["northeast", "pacific-northwest", "midwest"],
  },
  {
    id: "rhubarb",
    name: "Rhubarb",
    type: "fruit",
    imageUrl: photo("rhubarb.jpg"),
    description:
      "Choose firm, crisp stalks. The leaves are toxic, so trim them off — only the stalk is eaten.",
    seasons: ["spring"],
    regions: ["pacific-northwest", "northeast", "midwest", "mountain-west"],
  },
  {
    id: "mango",
    name: "Mango",
    type: "fruit",
    imageUrl: photo("mango.jpg"),
    description:
      "Judge by feel and smell, not color. A ripe mango gives gently and is fragrant at the stem.",
    seasons: ["summer", "spring"],
    regions: ["hawaii", "southeast"],
  },
  {
    id: "pineapple",
    name: "Pineapple",
    type: "fruit",
    imageUrl: photo("pineapple.jpg"),
    description:
      "Pineapple won't get sweeter after harvest. Pick one that's fragrant at the base and heavy for its size.",
    seasons: ["spring", "summer"],
    regions: ["hawaii"],
  },
  {
    id: "papaya",
    name: "Papaya",
    type: "fruit",
    imageUrl: photo("papaya.jpg"),
    description:
      "Ready to eat when the skin is mostly yellow-orange and yields to gentle pressure. Let green ones ripen at home.",
    seasons: ["spring", "summer", "fall"],
    regions: ["hawaii"],
  },
  {
    id: "avocado",
    name: "Avocado",
    type: "fruit",
    imageUrl: photo("avocado.jpg"),
    description:
      "Pop off the small stem nub — green underneath means ready, brown means overripe.",
    seasons: ["spring", "summer"],
    regions: ["southern-california", "hawaii"],
  },
  {
    id: "banana",
    name: "Banana",
    type: "fruit",
    imageUrl: photo("bananas.jpg"),
    description:
      "Small flecks of brown signal peak sweetness. Buy a mix of green and yellow to ripen over the week.",
    seasons: ["spring", "summer", "fall", "winter"],
    regions: ["hawaii"],
  },
  {
    id: "asparagus",
    name: "Asparagus",
    type: "vegetable",
    imageUrl: photo("asparagus.jpg"),
    description:
      "Look for the thinnest stalks with tightly closed tips. Steer clear of any that are limp or wilted.",
    seasons: ["spring"],
    regions: ["midwest", "northeast", "pacific-northwest", "southern-california"],
  },
  {
    id: "tomato",
    name: "Tomato",
    type: "vegetable",
    imageUrl: photo("tomato.jpg"),
    description:
      "The best tomatoes smell like the vine at the stem. Keep them on the counter — the fridge kills the flavor.",
    seasons: ["summer"],
    regions: ALL_MAINLAND,
  },
  {
    id: "sweet-corn",
    name: "Sweet Corn",
    type: "vegetable",
    imageUrl: photo("corn-on-the-cob.jpg"),
    description:
      "Sugar turns to starch within hours of picking. Buy it the day you'll eat it and look for plump, milky kernels.",
    seasons: ["summer"],
    regions: ["midwest", "northeast", "south", "southeast"],
  },
  {
    id: "zucchini",
    name: "Zucchini",
    type: "vegetable",
    imageUrl: photo("zucchini.jpg"),
    description:
      "Smaller squash are sweeter and more tender. The skin should be glossy and firm, never spongy.",
    seasons: ["summer"],
    regions: ALL_MAINLAND,
  },
  {
    id: "bell-pepper",
    name: "Bell Pepper",
    type: "vegetable",
    imageUrl: photo("bell-pepper-orange.jpg"),
    description:
      "Heavy, firm peppers with taut skin are freshest. Red and orange are simply ripened-on longer than green.",
    seasons: ["summer", "fall"],
    regions: ["southern-california", "south", "southeast", "midwest"],
  },
  {
    id: "beet",
    name: "Beet",
    type: "vegetable",
    imageUrl: photo("beets.jpg"),
    description:
      "Smaller roots are sweeter and more tender. Fresh, perky greens on top mean a recent harvest — cook them too.",
    seasons: ["summer", "fall"],
    regions: ALL_MAINLAND,
  },
  {
    id: "kale",
    name: "Kale",
    type: "vegetable",
    imageUrl: photo("kale.jpg"),
    description:
      "A touch of frost makes kale sweeter. Choose deeply colored, crisp leaves with no yellowing.",
    seasons: ["fall", "winter", "spring"],
    regions: ["northeast", "pacific-northwest", "midwest"],
  },
  {
    id: "brussels-sprouts",
    name: "Brussels Sprouts",
    type: "vegetable",
    imageUrl: photo("brussels-sprouts.jpg"),
    description:
      "Sold on the stalk, they keep longest. Pick tight, bright-green heads — smaller ones are milder and sweeter.",
    seasons: ["fall", "winter"],
    regions: ["pacific-northwest", "northeast", "southern-california"],
  },
  {
    id: "sweet-potato",
    name: "Sweet Potato",
    type: "vegetable",
    imageUrl: photo("sweet-potato.jpg"),
    description:
      "Choose firm roots with smooth skin and no soft spots. Store them cool and dry, never in the fridge.",
    seasons: ["fall"],
    regions: ["south", "southeast"],
  },
  {
    id: "butternut-squash",
    name: "Butternut Squash",
    type: "vegetable",
    imageUrl: photo("butternut-squash.jpg"),
    description:
      "A matte, hard rind and a dry stem mean it's cured and will keep for months in a cool pantry.",
    seasons: ["fall"],
    regions: ["northeast", "midwest", "mountain-west"],
  },
  {
    id: "pumpkin",
    name: "Pumpkin",
    type: "vegetable",
    imageUrl: photo("pumpkin.jpg"),
    description:
      "For cooking, choose smaller sugar pumpkins — the big carving kind are stringy and watery. Keep the stem intact.",
    seasons: ["fall"],
    regions: ALL_MAINLAND,
  },
  {
    id: "artichoke",
    name: "Artichoke",
    type: "vegetable",
    imageUrl: photo("artichokes.jpg"),
    description:
      "Look for a firm bulb with tightly closed leaves. Discoloration on the outer petals is usually harmless frost damage.",
    seasons: ["spring"],
    regions: ["southern-california"],
  },
  {
    id: "arugula",
    name: "Arugula",
    type: "vegetable",
    imageUrl: photo("arugula-or-rocket-salad.jpg"),
    description:
      "Like most tender greens, arugula is perishable. Look for crisp, dry leaves and use within a few days.",
    seasons: ["spring", "fall"],
    regions: ["northeast", "pacific-northwest", "southern-california"],
  },
  {
    id: "carrot",
    name: "Carrot",
    type: "vegetable",
    imageUrl: photo("carrots.jpg"),
    description:
      "Smooth, firm roots without cracks are freshest. If the greens are attached, twist them off so they don't draw moisture.",
    seasons: ["fall", "winter", "spring"],
    regions: ALL_MAINLAND,
  },
  {
    id: "spinach",
    name: "Spinach",
    type: "vegetable",
    imageUrl: photo("spinach.jpg"),
    description:
      "Choose springy, deep-green leaves. Pass on any bunch that looks slimy, yellowed, or wilted.",
    seasons: ["spring", "fall"],
    regions: ALL_MAINLAND,
  },
];
