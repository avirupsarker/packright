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

# Niseko Items
niseko_clothing = [
    get_item_html("GORE-TEX Ski Shell Jacket", "crucial — keeps the deep Hokkaido powder and moisture out", "gore-tex ski jacket winter"),
    get_item_html("Waterproof Ski Bibs/Pants", "essential — bibs prevent powder from getting down your back", "waterproof ski bibs winter pants"),
    get_item_html("Merino Wool Base Layers", "mandatory — regulates body temperature without sweating", "merino wool base layer thermal"),
    get_item_html("Insulated Ski Gloves", "essential — temperatures drop to -15°C routinely", "insulated waterproof ski gloves winter"),
    get_item_html("Moisture-Wicking Ski Socks", "cultural norm — you'll take shoes off indoors, so have clean, warm socks", "merino wool ski socks")
]
niseko_gear = [
    get_item_html("Low-Light Ski Goggles", "mandatory — Niseko is cloudy, you need rose/yellow lenses for flat light", "ski goggles low light winter"),
    get_item_html("High-Capacity Power Bank", "essential — phone batteries die extremely fast in the freezing cold", "anker power bank 20000mah"),
    get_item_html("Slip-on Ice Cleats / Microspikes", "lifesaver — Hirafu village roads are sheets of solid ice", "ice cleats microspikes shoes"),
    get_item_html("Fleece Neck Gaiter", "crucial — blocks brutal wind chill on the upper chairlifts", "fleece neck gaiter warmer ski"),
    get_item_html("SPF Zinc Lip Balm", "essential — prevents severe windburn and sun reflection", "spf lip balm zinc")
]

# Fuji Items
fuji_clothing = [
    get_item_html("Sturdy Waterproof Hiking Boots", "essential — volcanic rock/scree is sharp and loose. Sneakers will tear.", "columbia waterproof hiking boots trekking"),
    get_item_html("Insulated Down Jacket", "crucial — pre-dawn summit temperatures drop below freezing", "packable down jacket winter"),
    get_item_html("GORE-TEX Rain Shell", "mandatory — weather on the mountain changes in minutes", "gore-tex rain jacket waterproof"),
    get_item_html("Thermal Base Layers", "essential — the hike spans multiple extreme climate zones", "thermal base layer winter"),
    get_item_html("Moisture-Wicking Hiking Socks", "crucial — prevents crippling blisters on the long descent", "merino wool hiking socks blister")
]
fuji_gear = [
    get_item_html("High-Lumen Headlamp", "mandatory — required for the overnight hike to the summit in the dark", "high lumen led headlamp rechargeable"),
    get_item_html("Lightweight Trekking Poles", "lifesaver — saves your knees on the steep, loose volcanic descent", "lightweight trekking poles carbon fiber"),
    get_item_html("100-Yen Coins", "essential — mountain toilets are private and require coin payment", None),
    get_item_html("Portable Oxygen Canister", "recommended — altitude sickness is the #1 reason climbers fail", "portable oxygen canister hiking"),
    get_item_html("Small First-Aid & Blister Kit", "essential — moleskin or blister plasters are a must", "hiking first aid blister kit")
]

niseko_html = f'<div class="grid grid-cols-1 md:grid-cols-2 gap-8">\n{get_category_html("Clothing", niseko_clothing)}\n{get_category_html("Gear &amp; Essentials", niseko_gear)}\n</div>'
fuji_html = f'<div class="grid grid-cols-1 md:grid-cols-2 gap-8">\n{get_category_html("Clothing", fuji_clothing)}\n{get_category_html("Gear &amp; Essentials", fuji_gear)}\n</div>'

def inject_html(filepath, new_content):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use regex to replace the entire <div class="grid grid-cols-1 md:grid-cols-2 gap-8">...</div>
    # that sits right after the Trip Details.
    pattern = re.compile(r'<div class="grid grid-cols-1 md:grid-cols-2 gap-8">.*?</div>\s*<div class="mt-8 text-center bg-surface-container-low', re.DOTALL)
    
    new_text = new_content + '\n<div class="mt-8 text-center bg-surface-container-low'
    
    replaced = pattern.sub(new_text, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(replaced)

inject_html(niseko_path, niseko_html)
inject_html(fuji_path, fuji_html)

print("Expanded lists and Amazon India links injected!")
