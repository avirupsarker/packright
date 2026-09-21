import re
import os

pages_data = [
    {
        "id": "prague-christmas-markets",
        "url_path": "/packing-list/europe/prague-christmas-markets",
        "country": "Czech Republic",
        "region": "Europe",
        "links": [
            ("Vienna Christmas Markets", "/packing-list/europe/vienna-christmas-markets"),
            ("Strasbourg Christmas Markets", "/packing-list/europe/strasbourg-christmas-markets")
        ],
        "faqs": [
            {"q": "What shoes are suitable for Prague in winter?", "a": "Waterproof, insulated walking boots with thick rubber soles are essential. The cobblestones are extremely uneven and get dangerously slippery when wet or icy."},
            {"q": "Do I need thermal underwear?", "a": "Yes. If you plan to spend hours standing at the outdoor markets, merino wool or synthetic thermal base layers are highly recommended."},
            {"q": "Should I bring an umbrella?", "a": "A compact, wind-resistant umbrella is useful for freezing rain, but a waterproof coat with a good hood is often more practical in crowded markets."},
            {"q": "Are credit cards widely accepted at the markets?", "a": "While card acceptance is growing, many small market stalls still require cash (Czech Koruna). Carry small denominations."},
            {"q": "How should I carry my belongings safely?", "a": "Prague is generally safe, but pickpockets operate in crowded areas like the Old Town Square and Charles Bridge. Use a secure crossbody bag with zippers worn in front of you."},
            {"q": "What changes if I am travelling with kids?", "a": "Kids get cold faster when stationary. Pack extra hand warmers, insulated waterproof mittens (not knit gloves), and thick wool socks."}
        ]
    },
    {
        "id": "vienna-christmas-markets",
        "url_path": "/packing-list/europe/vienna-christmas-markets",
        "country": "Austria",
        "region": "Europe",
        "links": [
            ("Prague Christmas Markets", "/packing-list/europe/prague-christmas-markets"),
            ("Strasbourg Christmas Markets", "/packing-list/europe/strasbourg-christmas-markets")
        ],
        "faqs": [
            {"q": "What weather-specific layers are needed for Vienna?", "a": "Pack a stylish but heavily insulated winter coat, thermal tops, and a warm scarf, hat, and gloves. You want layers you can easily remove in warm museums."},
            {"q": "What should I wear to a classical concert or the opera?", "a": "Smart casual is the minimum. For men, a jacket (tie optional) and dress shoes; for women, an elegant dress, skirt, or dress trousers. Avoid sneakers and torn jeans."},
            {"q": "What are the best shoes for Vienna in December?", "a": "Waterproof, comfortable walking boots for the day, and a separate pair of dress shoes or smart ankle boots for the evening."},
            {"q": "Do I need cash for the Vienna markets?", "a": "Yes, while many accept cards now, having Euros in cash is essential for purchasing mug deposits (Pfand) and small snacks."},
            {"q": "What travelers commonly forget?", "a": "Skincare for cold weather. The combination of freezing wind outside and dry heating inside causes chapped lips and dry skin rapidly."},
            {"q": "Is a large suitcase necessary?", "a": "If you plan on buying heavy souvenirs like snow globes or extensive gifts, bring an expandable carry-on or a medium checked bag."}
        ]
    },
    {
        "id": "reykjavik-northern-lights",
        "url_path": "/packing-list/iceland/reykjavik-northern-lights",
        "country": "Iceland",
        "region": "Europe",
        "links": [
            ("Tromsø Northern Lights", "/packing-list/norway/tromso-northern-lights"),
            ("Rovaniemi Lapland", "/packing-list/finland/rovaniemi-lapland")
        ],
        "faqs": [
            {"q": "What weather-specific layers are needed for Iceland?", "a": "You need the 3-layer system: a Merino wool base layer, a thick fleece or wool sweater (like a traditional Lopapeysa), and a wind/waterproof outer shell jacket and trousers."},
            {"q": "What shoes are suitable for Northern Lights hunting?", "a": "Heavily insulated, waterproof winter boots with thick soles. The ground will freeze your feet quickly while standing still."},
            {"q": "Do I need traction cleats (microspikes)?", "a": "Yes. Sidewalks in Reykjavik and paths at waterfalls like Gullfoss get extremely icy. Slip-on traction cleats are highly recommended."},
            {"q": "How to pack for low-light photography?", "a": "Bring a sturdy travel tripod (essential for long exposures), spare batteries (keep them in an inside pocket to stay warm), and a remote shutter release."},
            {"q": "What should be rented versus brought?", "a": "Bring your own base and mid-layers. You can often rent heavy parkas and boots from tour operators if you don't want to buy them for one trip."},
            {"q": "What travelers commonly forget?", "a": "A sleep eye mask. If you are sleeping during the day after a long night of aurora hunting, a mask is essential, though less critical in the dark winter than in summer."}
        ]
    },
    {
        "id": "rovaniemi-lapland",
        "url_path": "/packing-list/finland/rovaniemi-lapland",
        "country": "Finland",
        "region": "Europe",
        "links": [
            ("Tromsø Northern Lights", "/packing-list/norway/tromso-northern-lights"),
            ("Sapporo Snow Festival", "/packing-list/japan/sapporo-snow-festival")
        ],
        "faqs": [
            {"q": "What weather-specific layers are needed for Lapland?", "a": "High-quality thermal base layers (Merino wool is best), thick fleece mid-layers, and a heavy winter coat for when you aren't wearing tour-supplied thermal suits."},
            {"q": "What should be rented versus brought?", "a": "Bring base layers, mid-layers, hats, and gloves. You can usually rely on tour operators to supply the heavy extreme-cold boots and thermal overalls for safaris."},
            {"q": "What changes for families or first-time visitors?", "a": "Kids need extra sets of gloves and socks, as theirs often get wet playing in the snow. Pack chemical hand warmers to prevent tantrums in the cold."},
            {"q": "What are the best gloves for Lapland?", "a": "Avoid fingered gloves. Wear thin liner gloves underneath thick, insulated mittens. Mittens trap heat much more effectively."},
            {"q": "Is an action camera necessary?", "a": "A chest-mounted action camera is great for capturing husky or snowmobile rides when your hands are busy and it's too cold to hold a phone."},
            {"q": "What do travelers commonly forget?", "a": "A good thermos flask to carry hot berry juice or tea during long outdoor excursions or Northern Lights waits."}
        ]
    },
    {
        "id": "varanasi-diwali",
        "url_path": "/packing-list/india/varanasi-diwali",
        "country": "India",
        "region": "Asia",
        "links": [
            ("Jaipur Diwali", "/packing-list/india/jaipur-diwali")
        ],
        "faqs": [
            {"q": "What shoes are suitable for Varanasi?", "a": "Comfortable, closed-toe walking shoes for navigating dirty, uneven streets, plus a pair of easy slip-on sandals for temple visits where footwear is prohibited."},
            {"q": "How should I dress for the ghats and temples?", "a": "Modestly. Both men and women should cover their shoulders and knees. Women often carry a lightweight dupatta or shawl to drape over their heads or shoulders."},
            {"q": "What health items are necessary?", "a": "Hand sanitizer, wet wipes, and an N95 mask (smoke from Diwali firecrackers and dust can heavily impact air quality)."},
            {"q": "Are gifts important to pack?", "a": "If visiting family, pack sweets, dry fruits, or gifts. Bring a foldable tote bag or leave extra room in your luggage."},
            {"q": "How should I manage cash?", "a": "Carry a hidden money belt or secure crossbody bag. You need small denomination Rupee notes for auto-rickshaws, small vendors, and temple donations."},
            {"q": "What travelers commonly forget?", "a": "A portable power bank. Taking photos and navigating the labyrinthine alleys with GPS will drain your phone battery quickly."}
        ]
    },
    {
        "id": "jaipur-diwali",
        "url_path": "/packing-list/india/jaipur-diwali",
        "country": "India",
        "region": "Asia",
        "links": [
            ("Varanasi Diwali", "/packing-list/india/varanasi-diwali")
        ],
        "faqs": [
            {"q": "What weather-specific layers are needed for Jaipur in November?", "a": "Days are warm and sunny; pack breathable cottons or linens. Evenings can get slightly chilly, so a light sweater or shawl is perfect."},
            {"q": "What shoes are suitable?", "a": "Comfortable, breathable walking shoes for exploring the massive courtyards of the forts and palaces, and smart sandals for evening dinners."},
            {"q": "How to pack for the signature activity (shopping)?", "a": "Bring an expandable suitcase or pack a foldable, lightweight duffel bag inside your main luggage to carry textiles, blue pottery, and gifts back home."},
            {"q": "How should I dress for sightseeing?", "a": "While more relaxed than religious hubs, modesty is still appreciated. Opt for loose, comfortable clothing that covers the knees and shoulders."},
            {"q": "What photography gear is necessary?", "a": "Jaipur is incredibly photogenic, especially illuminated for Diwali. Bring a good camera or clean your phone lenses, and a power bank is absolutely essential."},
            {"q": "What travelers commonly forget?", "a": "High SPF sunscreen and a sun hat. The Rajasthani sun is intense during midday fort tours, even in November."}
        ]
    },
    {
        "id": "tromso-northern-lights",
        "url_path": "/packing-list/norway/tromso-northern-lights",
        "country": "Norway",
        "region": "Europe",
        "links": [
            ("Reykjavik Northern Lights", "/packing-list/iceland/reykjavik-northern-lights"),
            ("Rovaniemi Lapland", "/packing-list/finland/rovaniemi-lapland")
        ],
        "faqs": [
            {"q": "What weather-specific layers are needed for Tromsø?", "a": "Merino wool thermal underwear, a thick wool sweater or heavy fleece, and a heavily insulated, windproof and waterproof parka or winter coat."},
            {"q": "What shoes are suitable for Tromsø?", "a": "Insulated, waterproof Arctic winter boots with heavy tread. Standard city boots or hiking boots will not keep your feet warm standing in the snow at night."},
            {"q": "What should be rented versus brought?", "a": "Tour operators almost always provide the extreme thermal suits and boots for dog sledding and snowmobiling. You must bring the high-quality base and mid-layers."},
            {"q": "What are the best gloves?", "a": "Bring thin touchscreen liner gloves to wear underneath heavy, insulated mittens. You can slip off the mitten to take a photo without exposing bare skin."},
            {"q": "How to pack for the signature activity?", "a": "For Northern lights photography, bring a sturdy tripod and a headlamp with a red-light setting (to preserve your night vision)."},
            {"q": "What changes for first-time Arctic visitors?", "a": "You'll need chemical hand and toe warmers, and you must remember to keep your phone and spare batteries in an inner pocket close to your body heat."}
        ]
    },
    {
        "id": "strasbourg-christmas-markets",
        "url_path": "/packing-list/france/strasbourg-christmas-markets",
        "country": "France",
        "region": "Europe",
        "links": [
            ("Prague Christmas Markets", "/packing-list/europe/prague-christmas-markets"),
            ("Vienna Christmas Markets", "/packing-list/europe/vienna-christmas-markets")
        ],
        "faqs": [
            {"q": "What weather-specific layers are needed?", "a": "Pack a warm, waterproof winter coat, a comfortable scarf, gloves, and thermal tops. The damp cold in the Alsace region can feel sharper than dry cold."},
            {"q": "What shoes are suitable for Strasbourg?", "a": "Waterproof walking boots or extremely comfortable, weather-treated sneakers. You will be walking miles on cobblestones each day."},
            {"q": "Is a large suitcase necessary?", "a": "No. Navigating train aisles and cobblestone streets with massive luggage is frustrating. Bring a smart carry-on and a foldable tote for purchases."},
            {"q": "How should I carry my belongings safely?", "a": "The markets get incredibly crowded. Wear a secure crossbody bag worn at the front to deter pickpockets and keep your hands free for food and drinks."},
            {"q": "Should I bring an umbrella?", "a": "Yes, a compact, wind-resistant travel umbrella is highly recommended as December can bring cold rain or wet snow."},
            {"q": "What travelers commonly forget?", "a": "A portable charger. The cold weather drains batteries quickly, and you will be taking countless photos of the spectacular decorations."}
        ]
    },
    {
        "id": "sapporo-snow-festival",
        "url_path": "/packing-list/japan/sapporo-snow-festival",
        "country": "Japan",
        "region": "Asia",
        "links": [
            ("Skiing in Niseko", "/packing-list/japan/niseko-skiing"),
            ("Rovaniemi Lapland", "/packing-list/finland/rovaniemi-lapland")
        ],
        "faqs": [
            {"q": "What shoes are suitable for Sapporo in winter?", "a": "Insulated, waterproof winter boots with aggressive, anti-slip treads. The compacted snow on the sidewalks is incredibly slippery."},
            {"q": "Do I need traction cleats (microspikes)?", "a": "Yes. If your boots lack specialized winter grip, slip-on traction cleats are essential to avoid falls. You can buy them cheaply in Sapporo."},
            {"q": "What weather-specific layers are needed?", "a": "Thermal base layers (Heattech or Merino wool), a thick sweater, and a wind/waterproof heavy winter coat. Snow pants are optional but useful for the Tsudome site."},
            {"q": "How to pack for the signature activity?", "a": "For photographing the illuminated ice sculptures at night, bring touchscreen-friendly gloves and keep a portable charger close to your body heat."},
            {"q": "What changes for first-time visitors?", "a": "The contrast between the freezing outdoors and the heavily heated indoor malls and subway is intense. Wear layers you can quickly unzip or remove."},
            {"q": "What travelers commonly forget?", "a": "Hand and toe warmers (Kairo). While you can buy them easily in Japan, having a few packs ready for your first night is very helpful."}
        ]
    }
]

for page in pages_data:
    file_path = os.path.join(r'c:\Users\HI\packright', page["url_path"].lstrip('/'), 'index.html')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # We need to completely remove the old Expert Tip and Sample List section
    # The old structure in the template starts from "<!-- Expert Tip -->" and goes up to right before "<!-- FAQ Section -->" or `<section class="flex flex-col gap-12">`
    # Let's target the exact string to remove.
    import re
    # We will strip out the "Expert Tip" block from the bottom.
    html = re.sub(r'<!-- Expert Tip -->.*?<!-- Sample List Structure -->', '<!-- Sample List Structure -->', html, flags=re.DOTALL)
    
    # We will strip out the "Sample List Structure" block from the bottom.
    html = re.sub(r'<!-- Sample List Structure -->.*?<section class="flex flex-col gap-12">', '<section class="flex flex-col gap-12">', html, flags=re.DOTALL)
    
    # We will fix "Doing something specific in Japan?"
    country = page["country"]
    links_html = ""
    for i, link in enumerate(page["links"]):
        if i > 0:
            links_html += ", " if i < len(page["links"]) - 1 else " or "
        links_html += f'<a class="text-primary hover:underline font-medium" href="{link[1]}">{link[0]}</a>'
        
    html = re.sub(r'Doing something specific in Japan\? View our specialized lists for.*?</p>', 
                  f'Doing something specific? View our specialized lists for {links_html}.</p>', html, flags=re.DOTALL)

    # We will fix "Frequently Asked Questions — Packing for Japan"
    html = re.sub(r'Frequently Asked Questions — Packing for Japan', f'Frequently Asked Questions — {country}', html)
    
    # We will fix "Not going to Japan?"
    html = re.sub(r'Not going to Japan\?', f'Not going to {country}?', html)
    
    # We need to fix the FAQ items at the bottom because there are still hardcoded Europe FAQs
    faq_html = ""
    for faq in page["faqs"]:
        faq_html += f"""<div class="flex justify-between items-center py-6 border-b border-outline-variant cursor-pointer group">
<span class="font-body-lg text-body-lg text-text-rich">{faq['q']}</span>
<span class="material-symbols-outlined text-on-surface-variant group-hover:text-primary transition-colors">expand_more</span>
</div>
<div class="hidden pb-6"><p class="font-body-md text-on-surface-variant">{faq['a']}</p></div>
"""
    
    html = re.sub(r'<div class="flex flex-col border-t border-outline-variant">.*?</div>\n</div>\n<!-- CTA Section -->',
                  f'<div class="flex flex-col border-t border-outline-variant">{faq_html}</div>\n</div>\n<!-- CTA Section -->', html, flags=re.DOTALL)

    # Some old FAQs were left over in the middle section because my previous regex replaced the grid.
    # Let's remove the first FAQ grid if there are two.
    # The first one is `<div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">` right above `<div class="mt-8 bg-surface-container`
    # Let's verify by just leaving the first one and removing the second, OR using the second as intended by the template.
    # The template intended the FAQs to be at the bottom (collapsible).
    # Since I injected `faq_html` in the middle during build_pages.py, I will remove it from the middle.
    html = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">\s*<div class="border-b.*?</div>\s*</div>\n\s*<div class="mt-8 bg-surface-container',
                  '<div class="mt-8 bg-surface-container', html, flags=re.DOTALL)


    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Fixed content in {file_path}")
