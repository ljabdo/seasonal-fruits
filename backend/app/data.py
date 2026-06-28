"""Loads the source produce chart and serves it in the shape the frontend expects.

Source: seasonal_produce.json (USDA/ACL "Seasonal Produce List by Region" chart),
organized region -> seasons -> [{name, type}]. The frontend, however, asks for its own
region IDs and expects richer produce objects, so this module maps regions and enriches
items (see enrich.py). Indexes are built once at import time."""

import json
import os
from datetime import datetime

from . import enrich
from .season import get_month_name, get_season

# Frontend region ID -> source JSON region key. The source has no direct equivalent for
# every frontend region, so a couple are mapped to the closest-overlapping chart region.
REGION_MAP: dict[str, str] = {
    "pacific-northwest": "northwest",
    "southern-california": "southwest",
    "mountain-west": "north_central",
    "midwest": "great_lakes_midwest",
    "northeast": "northeast",
    "south": "south_central",
    "southeast": "southeast",
    "hawaii": "hawaii",
}

REGION_LABELS: dict[str, str] = {
    "pacific-northwest": "Pacific Northwest",
    "southern-california": "Southern California",
    "mountain-west": "Mountain West",
    "midwest": "Midwest",
    "northeast": "Northeast",
    "south": "South",
    "southeast": "Southeast",
    "hawaii": "Hawaii",
}

DEFAULT_REGION = "southern-california"
FRONTEND_REGIONS = list(REGION_MAP.keys())

_DATA_FILE = os.getenv(
    "DATA_FILE",
    os.path.join(os.path.dirname(__file__), "..", "data", "seasonal_produce.json"),
)


def _load() -> dict:
    with open(_DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


_RAW = _load()
_REGIONS = _RAW["regions"]

# name -> set of frontend region IDs the item appears in (any season). Used for the
# contract's produce.regions[] field.
_REGIONS_BY_NAME: dict[str, set[str]] = {}
for _fid, _key in REGION_MAP.items():
    for _season_items in _REGIONS[_key]["seasons"].values():
        for _item in _season_items:
            _REGIONS_BY_NAME.setdefault(_item["name"], set()).add(_fid)


def _seasons_in_region(json_key: str, name: str) -> list[str]:
    """Seasons (ordered) in which `name` appears within the given source region."""
    order = ["winter", "spring", "summer", "fall"]
    seasons = _REGIONS[json_key]["seasons"]
    return [s for s in order if any(i["name"] == name for i in seasons.get(s, []))]


def _to_produce(item: dict, json_key: str, season: str, region_label: str) -> dict:
    name = item["name"]
    return {
        "id": enrich.slug(name),
        "name": name,
        "type": item["type"],
        "emoji": enrich.emoji_for(name),
        "imageUrl": enrich.image_url_for(name),
        "description": enrich.description_for(name, season, region_label),
        "seasons": _seasons_in_region(json_key, name),
        "regions": sorted(_REGIONS_BY_NAME.get(name, set())),
    }


def get_produce(region: str | None, now: datetime | None = None) -> dict:
    """Build the { season, month, region, produce[] } response for a frontend region.

    Invalid/missing regions fall back to DEFAULT_REGION, matching the bundled Next.js
    route handler."""
    region_id = region if region in REGION_MAP else DEFAULT_REGION
    json_key = REGION_MAP[region_id]
    label = REGION_LABELS[region_id]

    now = now or datetime.now()
    season = get_season(now)

    items = _REGIONS[json_key]["seasons"].get(season, [])
    produce = [_to_produce(item, json_key, season, label) for item in items]
    produce.sort(key=lambda p: p["name"])

    return {
        "season": season,
        "month": get_month_name(now),
        "region": region_id,
        "produce": produce,
    }
