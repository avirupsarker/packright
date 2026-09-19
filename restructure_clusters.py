import re

niseko_path = 'packing-list/japan/niseko-skiing/index.html'
fuji_path = 'packing-list/japan/mount-fuji-climbing/index.html'

def get_item_html(name, subtext, affiliate_kw=None):
    affiliate_link = ""
    if affiliate_kw:
        url = f"https://www.amazon.in/s?k={affiliate_kw.replace(' ', '+')}&tag=packright-21"
        affiliate_link = f' <a href="{url}" target="_blank" class="text-primary text-sm font-medium hover:underline ml-1 inline-block" onclick="event.stopPropagation()">View on Amazon.in &rarr;</a>'
    
    subtext_html = ""
    if subtext:
        subtext_html = f'<span class="font-label-sm text-label-sm text-on-surface-variant block italic">{subtext}</span>'
        
    return f"""
<!-- Item -->
<label class="flex items-start gap-3 p-3 hover:bg-[#fcf5f3] rounded-lg transition-colors cursor-pointer group border-t border-surface-variant first:border-t-0">
<div class="relative flex items-center justify-center w-5 h-5 mt-0.5">
<input class="w-5 h-5 border-2 border-outline-variant rounded text-primary focus:ring-primary focus:ring-offset-0 transition-colors peer cursor-pointer bg-transparent" type="checkbox">
</div>
<div class="flex-grow">
<span class="font-body-md text-body-md text-text-rich block mb-1 group-hover:text-primary transition-colors">{name}{affiliate_link}</span>
{subtext_html}
</div>
</label>
"""

def get_category_html(title, items):
    items_html = "".join(items)
    return f"""
<!-- Category: {title} -->
<div class="border border-outline-variant rounded-xl overflow-hidden">
<div class="bg-surface-container-low p-4 flex justify-between items-center border-b border-outline-variant cursor-pointer hover:bg-surface-container transition-colors">
<div class="flex items-center gap-3">
<h3 class="font-title-lg text-title-lg text-text-rich">{title}</h3>
<span class="bg-primary-fixed text-on-primary-fixed-variant px-2 py-0.5 rounded-full font-label-sm text-label-sm">X items</span>
</div>
<span class="material-symbols-outlined text-on-surface-variant">expand_less</span>
</div>
<div class="p-2">
{items_html}
</div>
</div>
"""

# Niseko Items - Max 3 affiliate links
niseko_clothing = [
    get_item_html("GORE-TEX Ski Shell Jacket", "crucial — keeps the deep Hokkaido powder out", "gore-tex ski jacket winter"), # Affiliate 1
    get_item_html("Waterproof Ski Bibs", "bibs prevent powder from getting down your back", None),
    get_item_html("Merino Wool Base Layers", "regulates body temperature without sweating", None),
    get_item_html("Casual Evening Outfit", "for exploring Hirafu village and izakayas", None)
]
niseko_tech = [
    get_item_html("Universal Travel Adapter", "Type A/B plugs for Japanese outlets", None),
    get_item_html("High-Capacity Power Bank", "phone batteries die extremely fast in the cold", None),
    get_item_html("Low-Light Ski Goggles", "mandatory — Niseko is cloudy, you need rose/yellow lenses", "ski goggles low light winter") # Affiliate 2
]
niseko_toiletries = [
    get_item_html("SPF Zinc Lip Balm", "prevents severe windburn and sun reflection", None),
    get_item_html("Heavy-duty Moisturizer", "Hokkaido's winter air is incredibly dry", None),
    get_item_html("Pain Relievers (Ibuprofen)", "for muscle soreness after a long day of skiing", None)
]
niseko_documents = [
    get_item_html("Passport & Insurance", "carry copies and proof of winter sports coverage", None),
    get_item_html("Japanese Yen (Cash)", "many small ramen shops and buses are cash-only", None),
    get_item_html("IC Transit Card (Suica/Pasmo)", "for seamless train/bus travel across Japan", None)
]

# Fuji Items - Max 3 affiliate links
fuji_clothing = [
    get_item_html("Sturdy Waterproof Hiking Boots", "essential — volcanic rock/scree is sharp and loose", "waterproof hiking boots trekking"), # Affiliate 1
    get_item_html("Insulated Down Jacket", "pre-dawn summit temperatures drop below freezing", None),
    get_item_html("GORE-TEX Rain Shell", "weather on the mountain changes in minutes", None),
    get_item_html("Moisture-Wicking Hiking Socks", "prevents crippling blisters on the long descent", None)
]
fuji_tech = [
    get_item_html("High-Lumen Headlamp", "mandatory — required for the overnight hike to the summit", "high lumen led headlamp rechargeable"), # Affiliate 2
    get_item_html("Spare AAA/AA Batteries", "bring extra batteries just in case the cold drains them", None),
    get_item_html("Power Bank", "to keep your phone charged for the summit sunrise photos", None)
]
fuji_health = [
    get_item_html("Portable Oxygen Canister", "altitude sickness is a major challenge above 3,000m", "portable oxygen canister hiking"), # Affiliate 3
    get_item_html("Blister Plasters / Moleskin", "crucial for the long descent down the mountain", None),
    get_item_html("Ibuprofen", "helps with altitude headaches and muscle pain", None)
]
fuji_docs = [
    get_item_html("Mountain Hut Reservation", "print it out, signal is spotty on the trail", None),
    get_item_html("100-Yen Coins", "essential — mountain toilets are private and require coin payment", None),
    get_item_html("High-Energy Snacks", "Calorie Mate, energy bars, and onigiri from a combini", None)
]

niseko_html = f'<div class="grid grid-cols-1 md:grid-cols-2 gap-8">\n{get_category_html("Clothing", niseko_clothing)}\n{get_category_html("Tech &amp; Electronics", niseko_tech)}\n{get_category_html("Toiletries &amp; Health", niseko_toiletries)}\n{get_category_html("Documents &amp; Money", niseko_documents)}\n</div>'
fuji_html = f'<div class="grid grid-cols-1 md:grid-cols-2 gap-8">\n{get_category_html("Clothing", fuji_clothing)}\n{get_category_html("Tech &amp; Electronics", fuji_tech)}\n{get_category_html("Health &amp; First-Aid", fuji_health)}\n{get_category_html("Documents &amp; Snacks", fuji_docs)}\n</div>'

def inject_html(filepath, new_content):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = re.compile(r'<div class="grid grid-cols-1 md:grid-cols-2 gap-8">.*?</div>\s*<div class="mt-8 text-center bg-surface-container-low', re.DOTALL)
    
    new_text = new_content + '\n<div class="mt-8 text-center bg-surface-container-low'
    
    replaced = pattern.sub(new_text, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(replaced)

inject_html(niseko_path, niseko_html)
inject_html(fuji_path, fuji_html)

print("Restructured lists to 4 categories with only 2-3 affiliate links each!")
