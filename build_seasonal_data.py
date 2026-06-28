"""
Builds seasonal_produce.json from the USDA / Administration for Community Living (ACL)
"Seasonal Produce List by Region" chart, sourced from:
https://acl.gov/sites/default/files/nutrition/SeasonalProduceChartByRegion.pdf

Produced in partnership with NANASP (National Association of Nutrition and Aging
Services Programs), using data compiled from the Farmer's Almanac, Alaska Grown,
and the Hawaii Agricultural and Food Products Directory.

Run: python3 build_seasonal_data.py
Output: seasonal_produce.json
"""

import json

# A light classifier so the app can filter to "fruits" specifically (your original
# use case) or show everything (fruits + vegetables). Anything not listed here
# falls back to "vegetable" -- the chart is vegetable-heavy, so that's the safer default.
FRUITS = {
    "apples", "apricots", "asparagus", "atemoya", "avocados", "avocado", "bananas", "banana",
    "blackberries", "blueberries", "boysenberries", "cantaloupe", "cherries", "cranberries",
    "currants", "dates", "figs", "figs (early)", "gooseberries", "grapefruit", "grapes",
    "grapes & muscadines", "grapes & muscadines (late)", "honeydew", "honeydew melon",
    "key limes", "kiwifruit", "kumquats", "lemons", "limes", "lime", "longan", "lychee",
    "mandarins", "mangos", "mango", "melons", "nectarines", "okra", "oranges", "orange",
    "papaya", "papaya (early)", "peaches", "pears", "pecans", "pecans (early)", "persimmons",
    "persimmon", "pineapples", "pineapple", "plantains", "plums", "plums (late)",
    "plums (early)", "pomegranates", "quince", "rambutan (late)", "raspberries", "rhubarb",
    "rhubarb (late)", "rhubarb (early)", "strawberries", "strawberries (early)",
    "strawberries (late)", "strawberry", "sunchokes", "tangerines", "tangerine",
    "tomatoes", "tomato", "tomato (early)", "walnuts", "watermelon", "almonds",
}

REGIONS = {
    "northwest": {
        "label": "Northwest",
        "states": ["WA", "OR", "ID"],
        "spring": ["Asparagus", "Lettuces", "Radishes", "Rhubarb"],
        "summer": ["Apples", "Apricots", "Asparagus", "Beets", "Blackberries", "Blueberries",
                   "Boysenberries", "Cherries", "Cucumbers", "Eggplant", "Gooseberries",
                   "Lettuces & greens", "Nectarines", "Peaches", "Peas", "Raspberries",
                   "Rhubarb", "Strawberries", "String beans", "Summer squash", "Sweet corn",
                   "Tomatoes"],
        "fall": ["Apples", "Beets", "Brussels sprouts", "Cabbage", "Figs", "Grapes", "Leeks",
                 "Melons", "Pears", "Plums", "Pumpkins and gourds", "Rutabagas", "Tomatoes",
                 "Winter squash"],
        "winter": ["Apples", "Leeks", "Rutabagas", "Winter squash"],
    },
    "southwest": {
        "label": "Southwest",
        "states": ["CA", "NV", "AZ", "UT"],
        "spring": ["Asparagus", "Beets", "Broccoli", "Brussels sprouts", "Cabbage",
                   "Cauliflower", "Cucumbers", "Leeks", "Lettuces & greens", "Mandarins",
                   "Oranges", "Peas", "Radishes", "Strawberries", "Turnips"],
        "summer": ["Apricots", "Artichokes", "Beets", "Blackberries", "Blueberries",
                   "Boysenberries", "Broccoli", "Cabbage", "Cauliflower", "Cherries",
                   "Cucumbers", "Eggplant", "Figs", "Grapes", "Lettuces & greens", "Melons",
                   "Nectarines", "Okra", "Peaches", "Peas", "Plums (late)", "Radishes",
                   "Raspberries", "Rhubarb", "Strawberries", "String beans",
                   "Summer & Winter squash", "Sweet corn", "Tomatoes", "Turnips"],
        "fall": ["Almonds", "Apples", "Artichokes", "Beets", "Broccoli", "Cabbage", "Dates",
                 "Figs", "Grapes", "Lettuces & greens", "Mandarins", "Melons", "Parsnips",
                 "Pears", "Persimmons", "Plums", "Pumpkins & gourds", "Radishes",
                 "Rhubarb (early)", "Rutabagas", "Strawberries", "Summer & Winter squash",
                 "Sunchokes", "Sweet corn", "Tomatoes", "Turnips", "Walnuts"],
        "winter": ["Beets", "Broccoli", "Cabbage", "Grapefruit", "Horseradish", "Kumquats",
                   "Leeks", "Mandarins", "Oranges", "Parsnips", "Radishes", "Rutabagas",
                   "Salsify", "Tangerines", "Walnuts"],
    },
    "north_central": {
        "label": "North Central",
        "states": ["MT", "WY", "CO", "ND", "SD", "NE", "KS", "MN", "IA", "MO"],
        "spring": ["Asparagus", "Beets", "Horseradish", "Lettuces & greens", "Parsnips",
                   "Peas (late)"],
        "summer": ["Blackberries", "Blueberries", "Boysenberries", "Broccoli", "Cabbage",
                   "Cauliflower", "Cherries", "Cucumbers", "Eggplant", "Gooseberries",
                   "Grapes", "Melons", "Nectarines", "Peaches", "Peas", "Raspberries",
                   "Rhubarb", "Strawberries", "String beans", "Summer squash", "Sweet corn",
                   "Tomatoes"],
        "fall": ["Apples", "Beets", "Broccoli", "Cabbage", "Cauliflower", "Cucumbers",
                 "Eggplant", "Grapes", "Lettuces & greens", "Melons", "Okra", "Pears",
                 "Plums (early)", "Pumpkins", "Radishes", "Rhubarb (early)",
                 "String beans (early)", "Summer & Winter squash", "Sweet corn",
                 "Sweet potatoes", "Tomatoes", "Turnips"],
        "winter": ["Chicories", "Horseradish", "Salsify", "Winter squash (early)"],
    },
    "south_central": {
        "label": "South Central",
        "states": ["NM", "OK", "TX", "AR", "LA"],
        "spring": ["Asparagus", "Beets", "Broccoli", "Brussels sprouts", "Cabbage",
                   "Cucumbers", "Lettuces & greens", "Peas", "Radishes", "Rhubarb",
                   "Strawberries", "Turnips"],
        "summer": ["Apples", "Blackberries", "Blueberries", "Cherries", "Cucumbers",
                   "Eggplant", "Figs", "Grapes", "Melons", "Nectarines", "Okra", "Peaches",
                   "Plums", "Raspberries", "Strawberries (early)", "String beans",
                   "Summer & Winter squash", "Sweet corn", "Tomatoes"],
        "fall": ["Apples", "Beets", "Broccoli", "Brussels sprouts", "Cabbage", "Cauliflower",
                 "Cucumbers", "Eggplant", "Figs", "Grapes & Muscadines", "Lettuces & greens",
                 "Melons", "Okra", "Pears", "Pecans", "Persimmons", "Pomegranates",
                 "Pumpkins", "Radishes", "Squash", "Sweet corn", "Sweet potatoes", "Tomatoes"],
        "winter": ["Beets", "Cabbage (early)", "Cauliflower", "Chicories", "Grapefruit",
                   "Horseradish", "Kumquats", "Lettuces & greens", "Mandarins", "Oranges",
                   "Pecans (early)", "Radishes", "Salsify", "Sunchokes", "Tangerines",
                   "Turnips"],
    },
    "great_lakes_midwest": {
        "label": "Great Lakes, Ohio Valley, Midwest",
        "states": ["WI", "MI", "IL", "IN", "OH", "KY"],
        "spring": ["Asparagus", "Cabbage (late)", "Lettuces & greens", "Parsnips", "Peas",
                   "Radishes", "Rhubarb"],
        "summer": ["Apples", "Beets", "Blackberries", "Blueberries", "Broccoli", "Cabbage",
                   "Cherries", "Cucumbers", "Currants", "Eggplant", "Gooseberries",
                   "Lettuces & greens", "Melons", "Nectarines", "Okra", "Peaches", "Peas",
                   "Plums (late)", "Radishes", "Raspberries", "Rhubarb (early)",
                   "Strawberries (early)", "String beans", "Summer squash", "Sunchokes",
                   "Sweet corn", "Tomatoes", "Turnips"],
        "fall": ["Apples", "Beets", "Broccoli", "Brussels sprouts", "Cabbage", "Cauliflower",
                 "Cucumbers", "Eggplant (early)", "Grapes", "Leeks", "Lettuces & greens",
                 "Parsnips", "Paw paws (early)", "Pears", "Plums", "Pumpkins", "Radishes",
                 "Rutabagas", "Sorghum", "Summer & Winter squash", "Sweet corn",
                 "Sweet potatoes", "Tomatoes", "Turnips"],
        "winter": ["Chicories", "Horseradish", "Salsify", "Sweet potatoes (early)",
                   "Winter squash (early)"],
    },
    "northeast": {
        "label": "Northeast and New England",
        "states": ["ME", "VT", "NH", "MA", "CT", "RI", "NY", "NJ", "PA", "MD", "DE"],
        "spring": ["Asparagus", "Fiddleheads", "Garlic Scapes (late)", "Lettuces & greens",
                   "Radishes (late)", "Rhubarb (late)"],
        "summer": ["Beets", "Blackberries", "Blueberries", "Broccoli", "Cabbage", "Cherries",
                   "Lettuces & greens", "Lima beans", "Melons", "Nectarines", "Peaches",
                   "Peas", "Radishes", "Raspberries", "Rhubarb", "Strawberries",
                   "String beans", "Summer squash", "Sweet corn", "Tomatoes"],
        "fall": ["Apples", "Beets", "Broccoli", "Brussels sprouts", "Cabbage", "Cauliflower",
                 "Cranberries", "Eggplant", "Grapes", "Melons", "Parsnips", "Pears", "Plums",
                 "Pumpkins & gourds", "Radishes", "Rutabagas", "Sunchokes", "Sweet potatoes",
                 "Turnips", "Winter squash"],
        "winter": ["Brussels sprouts (early)", "Cranberries (early)", "Horseradish",
                   "Leeks (early)", "Parsnips", "Salsify", "Sweet potatoes (early)",
                   "Winter squash (early)"],
    },
    "southeast": {
        "label": "Southeast",
        "states": ["WV", "VA", "NC", "SC", "TN", "GA", "FL", "AL", "MS"],
        "spring": ["Asparagus", "Beets (late)", "Cabbage (late)", "Lettuces & greens", "Peas",
                   "Radishes", "Rhubarb (late)", "String beans (late)", "Turnips",
                   "Vidalia onions (late)"],
        "summer": ["Apples", "Apricots", "Beets", "Blackberries", "Blueberries", "Broccoli",
                   "Cabbage", "Cherries", "Cucumbers", "Eggplant (late)",
                   "Grapes & Muscadines (late)", "Key limes", "Leeks", "Lettuces & greens",
                   "Lima beans", "Melons", "Nectarines", "Okra", "Peaches", "Peas",
                   "Raspberries", "Rhubarb", "Strawberries", "String beans", "Summer squash",
                   "Sweet corn", "Tomatoes"],
        "fall": ["Beets", "Broccoli", "Brussels sprouts", "Cabbage", "Cucumbers",
                 "Eggplant (early)", "Figs (early)", "Grapefruit", "Grapes & Muscadines",
                 "Lettuces & greens", "Okra", "Oranges", "Paw paws", "Pears", "Peas",
                 "Pecans", "Persimmons", "Pumpkins", "Quince", "Radishes", "Rutabagas",
                 "Strawberries (late)", "String beans (early)", "Summer & winter squash",
                 "Sweet corn", "Sweet potatoes", "Tangerines", "Tomatoes", "Turnips"],
        "winter": ["Beets (early)", "Broccoli (early)", "Brussels sprouts (early)", "Cabbage",
                   "Grapefruit", "Kumquats", "Leeks", "Lettuces & greens", "Oranges",
                   "Radishes", "Sweet potatoes", "Tangerines", "Turnips"],
    },
    "alaska": {
        "label": "Alaska",
        "states": ["AK"],
        "note": "Spring and Winter items are largely from cold storage.",
        "spring": ["Beets", "Carrots", "Lettuce (late)", "Potatoes", "Rhubarb (late)",
                   "Tomatoes (late)"],
        "summer": ["Beans", "Beets", "Broccoli", "Brussels sprouts (late)", "Cabbage",
                   "Carrots (late)", "Cauliflower", "Celery (late)", "Chard",
                   "Collard greens", "Cucumbers", "Kale", "Lettuce", "Onions", "Peas",
                   "Potatoes", "Radishes", "Raspberries", "Rhubarb", "Spinach",
                   "Strawberries", "Tomatoes", "Turnips", "Winter squash (late)", "Zucchini"],
        "fall": ["Beans", "Beets", "Broccoli", "Brussels sprouts (late)", "Cabbage",
                 "Carrots (late)", "Cauliflower", "Celery (late)", "Chard", "Collard greens",
                 "Cucumbers", "Kale", "Lettuce", "Onions", "Peas", "Potatoes", "Radishes",
                 "Raspberries", "Rhubarb", "Spinach", "Strawberries", "Tomatoes", "Turnips",
                 "Winter squash (late)", "Zucchini"],
        "winter": ["Beets", "Cabbage (early)", "Carrots", "Onions", "Potatoes", "Turnips"],
    },
    "hawaii": {
        "label": "Hawaii",
        "states": ["HI"],
        "spring": ["Beans", "Bittermelon", "Cabbage", "Cantaloupe", "Celery", "Cucumber",
                   "Eggplant", "Ginger root", "Green pepper", "Heart of palm", "Honeydew",
                   "Lettuce & greens", "Lime", "Lychee", "Mango", "Mushrooms", "Onion",
                   "Orange", "Papaya", "Pineapple", "Sprouts", "Strawberry", "Sweet potato",
                   "Taro"],
        "summer": ["Banana", "Beans", "Bittermelon", "Cabbage", "Cantaloupe", "Celery",
                   "Cucumber", "Daikon (late)", "Eggplant (early)", "Ginger root",
                   "Green onion", "Green pepper", "Heart of palm", "Honeydew",
                   "Lettuce & greens", "Lime", "Lychee", "Mango", "Mushrooms", "Onion",
                   "Papaya", "Pineapple", "Sprouts", "Sweet potato", "Taro", "Tomato",
                   "Watermelon", "Zucchini (late)"],
        "fall": ["Banana", "Burdock", "Daikon", "Green onion", "Heart of palm",
                 "Lettuce & greens", "Lime", "Longan", "Mango", "Mushrooms", "Orange",
                 "Papaya (early)", "Persimmon", "Pumpkin", "Sprouts", "Tomato (early)",
                 "Zucchini"],
        "winter": ["Atemoya", "Avocado", "Burdock", "Heart of palm", "Lettuce & greens",
                   "Lime", "Mushrooms", "Orange", "Pumpkin", "Rambutan (late)", "Sprouts",
                   "Strawberry", "Tangerine"],
    },
}


def classify(item: str) -> str:
    key = item.split(" (")[0].strip().lower()
    return "fruit" if key in FRUITS else "vegetable"


def build():
    output = {"source": {
        "name": "Seasonal Produce List by Region",
        "publisher": "Administration for Community Living (ACL) / NANASP",
        "url": "https://acl.gov/sites/default/files/nutrition/SeasonalProduceChartByRegion.pdf",
        "underlying_sources": [
            "Farmer's Almanac",
            "Alaska Grown - Seasonal Produce Chart",
            "Hawaii Agricultural and Food Products Directory - Hawaii Seasonality Chart",
        ],
    }, "regions": {}}

    for key, region in REGIONS.items():
        seasons = {}
        for season in ("spring", "summer", "fall", "winter"):
            items = region[season]
            seasons[season] = [{"name": item, "type": classify(item)} for item in items]
        output["regions"][key] = {
            "label": region["label"],
            "states": region["states"],
            **({"note": region["note"]} if "note" in region else {}),
            "seasons": seasons,
        }
    return output


if __name__ == "__main__":
    data = build()
    with open("seasonal_produce.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"Wrote seasonal_produce.json with {len(data['regions'])} regions")
