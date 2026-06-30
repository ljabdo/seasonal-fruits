"""Synthesizes the presentation fields the frontend's ProduceCard needs but that the
source `seasonal_produce.json` lacks: image URL, description, and a slug id.

IMG_FILE is keyed by the produce's *base name* (qualifiers like "(early)"/"(late)"
stripped, lowercased) and maps to the filename of a locally-bundled photo. Every
produce item in the source chart has a matching image in the frontend's public/produce/
directory (originally from Spoonacular / Wikimedia Commons); unmatched names fall back
to a slug guess.

Image URLs are root-relative (e.g. "/produce/strawberries.jpg") so the browser loads
them same-origin from the frontend — nothing is fetched from the web at runtime.
"""

import os
import re

# Images are served as static files from the frontend's public/produce/ directory
# (downloaded copies — nothing is pulled from the web at runtime). The path is
# root-relative so it resolves against the page origin. Override with IMAGE_BASE_URL
# if the images are hosted elsewhere.
_IMAGE_BASE = os.getenv("IMAGE_BASE_URL", "/produce").rstrip("/")

# Spoonacular ingredient filenames. Entries reuse names known to exist on the CDN
# (notably the ones the frontend's curated dataset already relies on).
IMG_FILE: dict[str, str] = {
    "almonds": "almonds.jpg", "apples": "apple.jpg", "apricots": "apricot.jpg",
    "artichokes": "artichokes.jpg", "arugula": "arugula-or-rocket-salad.jpg",
    "asparagus": "asparagus.jpg", "avocado": "avocado.jpg", "banana": "bananas.jpg",
    "beets": "beets.jpg", "bell pepper": "bell-pepper-orange.jpg",
    "blackberries": "blackberries.jpg", "blueberries": "blueberries.jpg",
    "boysenberries": "blackberries.jpg", "broccoli": "broccoli.jpg",
    "brussels sprouts": "brussels-sprouts.jpg",
    "butternut squash": "butternut-squash.jpg", "cabbage": "cabbage.jpg",
    "cantaloupe": "cantaloupe.jpg", "carrot": "carrots.jpg", "carrots": "carrots.jpg",
    "cauliflower": "cauliflower.jpg", "celery": "celery.jpg", "chard": "swiss-chard.jpg",
    "cherries": "cherries.jpg", "collard greens": "collard-greens.jpg",
    "cranberries": "cranberries.jpg", "cucumber": "cucumber.jpg",
    "cucumbers": "cucumber.jpg", "currants": "currants.jpg", "dates": "dates.jpg",
    "bittermelon": "bitter-melon.jpg", "eggplant": "eggplant.jpg",
    "figs": "figs.jpg", "ginger root": "ginger.jpg", "grapefruit": "grapefruit.jpg",
    "grapes": "red-grapes.jpg", "grapes & muscadines": "red-grapes.jpg",
    "green onion": "spring-onions.jpg", "green pepper": "green-pepper.jpg",
    "gooseberries": "gooseberries.jpg", "honeydew": "honeydew-melon.jpg",
    "kale": "kale.jpg", "key limes": "lime.jpg", "kumquats": "kumquat.jpg",
    "daikon": "daikon.jpg", "leeks": "leeks.jpg", "lettuce": "iceberg-lettuce.jpg",
    "lettuce & greens": "iceberg-lettuce.jpg", "lettuces": "iceberg-lettuce.jpg",
    "lettuces & greens": "iceberg-lettuce.jpg", "lime": "lime.jpg", "lychee": "lychees.jpg",
    "mandarins": "tangerine.jpg", "mango": "mango.jpg", "melons": "cantaloupe.jpg",
    "mushrooms": "mushrooms.jpg", "nectarines": "nectarines.jpg", "okra": "okra.jpg",
    "onion": "brown-onion.jpg", "onions": "brown-onion.jpg", "orange": "orange.jpg",
    "oranges": "orange.jpg", "papaya": "papaya.jpg", "parsnips": "parsnip.jpg",
    "peaches": "peaches.jpg", "pears": "pear.jpg", "peas": "peas.jpg",
    "pecans": "pecans.jpg", "persimmon": "persimmon.jpg", "persimmons": "persimmon.jpg",
    "pineapple": "pineapple.jpg", "plums": "plum.jpg", "pomegranates": "pomegranate.jpg",
    "potatoes": "potatoes-yukon-gold.jpg", "pumpkin": "pumpkin.jpg",
    "pumpkins": "pumpkin.jpg", "pumpkins & gourds": "pumpkin.jpg",
    "pumpkins and gourds": "pumpkin.jpg", "radishes": "radishes.jpg",
    "raspberries": "raspberries.jpg", "rhubarb": "rhubarb.jpg", "spinach": "spinach.jpg",
    "sprouts": "bean-sprouts.jpg", "squash": "butternut-squash.jpg",
    "sunchokes": "jerusalem-artichoke.jpg",
    "strawberries": "strawberries.jpg",
    "strawberry": "strawberries.jpg", "summer squash": "yellow-squash.jpg",
    "summer & winter squash": "butternut-squash.jpg", "sweet corn": "corn-on-the-cob.jpg",
    "sweet potato": "sweet-potato.jpg", "sweet potatoes": "sweet-potato.jpg",
    "tangerine": "tangerine.jpg", "tangerines": "tangerine.jpg", "taro": "taro-root.jpg",
    "tomato": "tomato.jpg", "tomatoes": "tomato.jpg", "turnips": "turnips.jpg",
    "walnuts": "walnuts.jpg", "watermelon": "watermelon.jpg",
    "winter squash": "butternut-squash.jpg", "zucchini": "zucchini.jpg",
    # Less common items resolved from Wikimedia Commons (saved under these names).
    "beans": "green-beans.jpg", "string beans": "green-beans.jpg",
    "rutabagas": "rutabaga.jpg", "chicories": "chicory.jpg",
    "vidalia onions": "brown-onion.jpg",
}


def base_name(name: str) -> str:
    """Strip a trailing qualifier like " (early)" / " (late)" and lowercase."""
    return re.sub(r"\s*\(.*?\)\s*$", "", name).strip().lower()


def slug(name: str) -> str:
    base = base_name(name)
    return re.sub(r"[^a-z0-9]+", "-", base).strip("-")


def image_url_for(name: str) -> str:
    filename = IMG_FILE.get(base_name(name), f"{slug(name)}.jpg")
    return f"{_IMAGE_BASE}/{filename}"


def description_for(name: str, season: str, region_label: str) -> str:
    return f"{name} is in season this {season} in {region_label}."
