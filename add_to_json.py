import json
import os

file_path = 'data/affiliates.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_products = [
    {
        "id": "gore-tex-ski-jacket",
        "name": "GORE-TEX Ski Shell Jacket",
        "label": "Find on Amazon →",
        "keywords": ["ski jacket", "gore-tex jacket", "snow jacket", "waterproof shell", "winter coat", "skiing coat"],
        "links": {
            "IN": "https://www.amazon.in/s?k=gore-tex+ski+jacket+winter&tag=PACKRIGHT-IN-21",
            "AE": "https://www.amazon.ae/s?k=gore-tex+ski+jacket+winter&tag=PACKRIGHT-AE-21",
            "GB": "https://www.amazon.co.uk/s?k=gore-tex+ski+jacket+winter&tag=PACKRIGHT-GB-21",
            "default": "https://www.amazon.com/s?k=gore-tex+ski+jacket+winter&tag=PACKRIGHT-21"
        }
    },
    {
        "id": "merino-base-layers",
        "name": "Merino Wool Base Layers",
        "label": "Find on Amazon →",
        "keywords": ["base layer", "thermal underwear", "merino wool", "thermals", "long johns", "ski base layer"],
        "links": {
            "IN": "https://www.amazon.in/s?k=merino+wool+base+layer+thermal&tag=PACKRIGHT-IN-21",
            "AE": "https://www.amazon.ae/s?k=merino+wool+base+layer+thermal&tag=PACKRIGHT-AE-21",
            "GB": "https://www.amazon.co.uk/s?k=merino+wool+base+layer+thermal&tag=PACKRIGHT-GB-21",
            "default": "https://www.amazon.com/s?k=merino+wool+base+layer+thermal&tag=PACKRIGHT-21"
        }
    },
    {
        "id": "ski-goggles",
        "name": "Ski Goggles (Low-Light Lens)",
        "label": "Find on Amazon →",
        "keywords": ["ski goggles", "snow goggles", "snowboard goggles", "winter goggles", "low light goggles"],
        "links": {
            "IN": "https://www.amazon.in/s?k=ski+goggles+low+light+winter&tag=PACKRIGHT-IN-21",
            "AE": "https://www.amazon.ae/s?k=ski+goggles+low+light+winter&tag=PACKRIGHT-AE-21",
            "GB": "https://www.amazon.co.uk/s?k=ski+goggles+low+light+winter&tag=PACKRIGHT-GB-21",
            "default": "https://www.amazon.com/s?k=ski+goggles+low+light+winter&tag=PACKRIGHT-21"
        }
    },
    {
        "id": "ice-cleats",
        "name": "Slip-on Ice Cleats",
        "label": "Find on Amazon →",
        "keywords": ["ice cleats", "microspikes", "crampons", "snow grips", "ice grips", "shoe spikes"],
        "links": {
            "IN": "https://www.amazon.in/s?k=ice+cleats+microspikes+shoes&tag=PACKRIGHT-IN-21",
            "AE": "https://www.amazon.ae/s?k=ice+cleats+microspikes+shoes&tag=PACKRIGHT-AE-21",
            "GB": "https://www.amazon.co.uk/s?k=ice+cleats+microspikes+shoes&tag=PACKRIGHT-GB-21",
            "default": "https://www.amazon.com/s?k=ice+cleats+microspikes+shoes&tag=PACKRIGHT-21"
        }
    },
    {
        "id": "hiking-boots",
        "name": "Waterproof Hiking Boots",
        "label": "Find on Amazon →",
        "keywords": ["hiking boots", "trekking shoes", "waterproof boots", "trail boots", "hiking shoes"],
        "links": {
            "IN": "https://www.amazon.in/s?k=waterproof+hiking+boots+trekking&tag=PACKRIGHT-IN-21",
            "AE": "https://www.amazon.ae/s?k=waterproof+hiking+boots+trekking&tag=PACKRIGHT-AE-21",
            "GB": "https://www.amazon.co.uk/s?k=waterproof+hiking+boots+trekking&tag=PACKRIGHT-GB-21",
            "default": "https://www.amazon.com/s?k=waterproof+hiking+boots+trekking&tag=PACKRIGHT-21"
        }
    },
    {
        "id": "trekking-poles",
        "name": "Lightweight Trekking Poles",
        "label": "Find on Amazon →",
        "keywords": ["trekking poles", "hiking poles", "walking sticks", "hiking sticks"],
        "links": {
            "IN": "https://www.amazon.in/s?k=lightweight+trekking+poles+carbon+fiber&tag=PACKRIGHT-IN-21",
            "AE": "https://www.amazon.ae/s?k=lightweight+trekking+poles+carbon+fiber&tag=PACKRIGHT-AE-21",
            "GB": "https://www.amazon.co.uk/s?k=lightweight+trekking+poles+carbon+fiber&tag=PACKRIGHT-GB-21",
            "default": "https://www.amazon.com/s?k=lightweight+trekking+poles+carbon+fiber&tag=PACKRIGHT-21"
        }
    }
]

# Insert before the last two items (insurance and esim)
data["products"] = data["products"][:-2] + new_products + data["products"][-2:]

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Updated affiliates.json")
