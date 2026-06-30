"""Month -> season logic. Mirrors frontend/src/lib/season.ts so the backend and the
bundled Next.js route handler agree: Winter Dec-Feb, Spring Mar-May, Summer Jun-Aug,
Fall Sep-Nov."""

from datetime import datetime

Season = str  # one of: "winter", "spring", "summer", "fall"

SEASONS = ["winter", "spring", "summer", "fall"]

_MONTH_NAMES = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]


def get_season(now: datetime | None = None) -> Season:
    month = (now or datetime.now()).month  # 1-12
    if month == 12 or month <= 2:
        return "winter"
    if month <= 5:
        return "spring"
    if month <= 8:
        return "summer"
    return "fall"


def get_month_name(now: datetime | None = None) -> str:
    return _MONTH_NAMES[(now or datetime.now()).month - 1]
