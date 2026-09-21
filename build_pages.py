import os
import json
import urllib.parse

# 1. Configuration for the 9 pages
pages_data = [
    {
        "id": "prague-christmas-markets",
        "url_path": "/packing-list/europe/prague-christmas-markets",
        "title": "Your Packing Checklist for Prague Christmas Markets - PackRight",
        "meta_desc": "Get a personalized AI packing list for the Prague Christmas markets. Essential gear for cold-weather cobblestone walking, crowds, and winter evenings.",
        "h1": "Prague Christmas Market Packing List",
        "prompt": "4 days in Prague in December for the Christmas markets, lots of walking on cobblestones, carrying purchases, and evening sightseeing.",
        "expert_tip": "Cobblestone Reality: Prague's historic centre is beautiful but uneven. Ditch the heels and pack comfortable, waterproof walking boots with thick soles and good traction.",
        "context_block": "<p>Prague in winter is magical, with its world-famous Christmas markets transforming the Old Town Square and Wenceslas Square into winter wonderlands. However, the combination of sub-zero temperatures, potential snow or icy rain, and historic cobblestone streets means your packing list needs to prioritize practicality.</p><p>A successful Prague trip hinges on layering and footwear. You'll be spending long hours outdoors sipping hot wine (svařák) and browsing stalls, so a high-quality thermal base layer and a windproof, insulated coat are non-negotiable. Furthermore, navigating dense crowds requires a secure crossbody bag to protect your valuables.</p><p>Use PackRight to tailor this baseline checklist to your exact travel dates, whether you're adding a formal evening at the Estates Theatre or taking a day trip to Český Krumlov.</p>",
        "faqs": [
            {"q": "What shoes are suitable for Prague in winter?", "a": "Waterproof, insulated walking boots with thick rubber soles are essential. The cobblestones are extremely uneven and get dangerously slippery when wet or icy."},
            {"q": "Do I need thermal underwear?", "a": "Yes. If you plan to spend hours standing at the outdoor markets, merino wool or synthetic thermal base layers are highly recommended."},
            {"q": "Should I bring an umbrella?", "a": "A compact, wind-resistant umbrella is useful for freezing rain, but a waterproof coat with a good hood is often more practical in crowded markets."},
            {"q": "Are credit cards widely accepted at the markets?", "a": "While card acceptance is growing, many small market stalls still require cash (Czech Koruna). Carry small denominations."},
            {"q": "How should I carry my belongings safely?", "a": "Prague is generally safe, but pickpockets operate in crowded areas like the Old Town Square and Charles Bridge. Use a secure crossbody bag with zippers worn in front of you."},
            {"q": "What changes if I am travelling with kids?", "a": "Kids get cold faster when stationary. Pack extra hand warmers, insulated waterproof mittens (not knit gloves), and thick wool socks."}
        ],
        "categories": {
            "Clothing": ["Insulated winter coat", "Thermal base layer", "Warm sweater/fleece"],
            "Footwear": ["Waterproof walking boots", "Thick wool socks"],
            "Accessories": ["Secure crossbody bag", "Touchscreen gloves", "Warm hat & scarf"],
            "Tech & Gear": ["Portable charger (cold drains batteries)", "Foldable shopping tote"],
            "Documents & Health": ["Blister plasters", "Travel insurance", "Cash (Czech Koruna)"]
        },
        "rent_leave": "Leave at home: High heels (impossible on cobblestones) and bulky umbrellas (hard to use in crowds). Rent/Borrow: Nothing specific unless doing winter sports outside the city.",
        "breadcrumb": "<li><a class=\"hover:text-brand-terracotta transition-colors\" href=\"/packing-list/europe\">Europe</a></li>\n<li class=\"flex items-center\"><span class=\"material-symbols-outlined text-[16px] mx-1 opacity-50\">chevron_right</span></li>\n<li>Prague Christmas Markets</li>"
    },
    {
        "id": "vienna-christmas-markets",
        "url_path": "/packing-list/europe/vienna-christmas-markets",
        "title": "Your Packing Checklist for Vienna Christmas Markets - PackRight",
        "meta_desc": "Get a personalized AI packing list for the Vienna Christmas markets. Essential gear for elegant winter walking, opera nights, and market tours.",
        "h1": "Vienna Christmas Market Packing List",
        "prompt": "5 days in Vienna in December, visiting the Christmas markets, going to a classical concert, dining out, and visiting museums.",
        "expert_tip": "Smart-Casual Winter: Vienna is an elegant city. For evenings at the opera or upscale dining, you'll need smart-casual layers that fit comfortably under a heavy winter coat.",
        "context_block": "<p>Vienna offers a grand, imperial backdrop to its famous Christkindlmarkts. While you will face the same central European winter cold as other cities, Vienna's itinerary often mixes outdoor market browsing with indoor cultural events like concerts, museum tours, and visits to elegant coffee houses.</p><p>This means your packing list must bridge the gap between heavy-duty outdoor warmth and indoor refinement. You need a warm, stylish wool or insulated coat that looks appropriate over dinner wear, plus waterproof walking boots for daytime sightseeing. Since you'll frequently transition between freezing outdoor temperatures and heavily heated indoor spaces, breathable layers are critical.</p><p>Let PackRight customize this list based on your specific cultural itinerary and dining plans.</p>",
        "faqs": [
            {"q": "What weather-specific layers are needed for Vienna?", "a": "Pack a stylish but heavily insulated winter coat, thermal tops, and a warm scarf, hat, and gloves. You want layers you can easily remove in warm museums."},
            {"q": "What should I wear to a classical concert or the opera?", "a": "Smart casual is the minimum. For men, a jacket (tie optional) and dress shoes; for women, an elegant dress, skirt, or dress trousers. Avoid sneakers and torn jeans."},
            {"q": "What are the best shoes for Vienna in December?", "a": "Waterproof, comfortable walking boots for the day, and a separate pair of dress shoes or smart ankle boots for the evening."},
            {"q": "Do I need cash for the Vienna markets?", "a": "Yes, while many accept cards now, having Euros in cash is essential for purchasing mug deposits (Pfand) and small snacks."},
            {"q": "What travelers commonly forget?", "a": "Skincare for cold weather. The combination of freezing wind outside and dry heating inside causes chapped lips and dry skin rapidly."},
            {"q": "Is a large suitcase necessary?", "a": "If you plan on buying heavy souvenirs like snow globes or extensive gifts, bring an expandable carry-on or a medium checked bag."}
        ],
        "categories": {
            "Clothing": ["Elegant winter coat", "Smart-casual evening wear", "Thermal base layer"],
            "Footwear": ["Waterproof walking boots", "Dress shoes / Smart boots"],
            "Accessories": ["Leather gloves", "Warm scarf & beanie", "Secure crossbody bag"],
            "Tech & Gear": ["Portable charger", "Foldable shopping tote"],
            "Documents & Health": ["Cold-weather skincare (lip balm/moisturizer)", "Cash (Euros)"]
        },
        "rent_leave": "Leave at home: Light jackets (insufficient for December) and overly casual sportswear for evenings out. Rent/Borrow: N/A.",
        "breadcrumb": "<li><a class=\"hover:text-brand-terracotta transition-colors\" href=\"/packing-list/europe\">Europe</a></li>\n<li class=\"flex items-center\"><span class=\"material-symbols-outlined text-[16px] mx-1 opacity-50\">chevron_right</span></li>\n<li>Vienna Christmas Markets</li>"
    },
    {
        "id": "reykjavik-northern-lights",
        "url_path": "/packing-list/iceland/reykjavik-northern-lights",
        "title": "Your Packing Checklist for Reykjavik Northern Lights - PackRight",
        "meta_desc": "Get a personalized AI packing list for a Reykjavik Northern Lights trip. Essential gear for freezing winds, long outdoor waits, and low-light photography.",
        "h1": "Reykjavik Northern Lights Packing List",
        "prompt": "6 days in Reykjavik in January, hunting for the Northern Lights, doing the Golden Circle, renting a car, and doing some low-light photography.",
        "expert_tip": "Windproof Over Waterproof: In Iceland, the wind is your biggest enemy. Ensure your outermost layer is completely windproof to prevent the cold air from stripping your body heat.",
        "context_block": "<p>Hunting for the Northern Lights from Reykjavik means exposing yourself to Iceland's notoriously volatile winter weather. You will likely spend hours standing perfectly still in freezing, windy conditions in the middle of the night waiting for the aurora to appear. This requires a completely different packing strategy than a winter city break.</p><p>Your packing list must revolve around an extreme layering system: moisture-wicking thermal base layers, heavy fleece or wool mid-layers, and a totally windproof and waterproof outer shell. Furthermore, if you are driving the Golden Circle or South Coast, you need gear that handles sudden downpours, sleet, and slippery ice.</p><p>PackRight will generate a comprehensive list based on whether you are doing guided bus tours or driving yourself.</p>",
        "faqs": [
            {"q": "What weather-specific layers are needed for Iceland?", "a": "You need the 3-layer system: a Merino wool base layer, a thick fleece or wool sweater (like a traditional Lopapeysa), and a wind/waterproof outer shell jacket and trousers."},
            {"q": "What shoes are suitable for Northern Lights hunting?", "a": "Heavily insulated, waterproof winter boots with thick soles. The ground will freeze your feet quickly while standing still."},
            {"q": "Do I need traction cleats (microspikes)?", "a": "Yes. Sidewalks in Reykjavik and paths at waterfalls like Gullfoss get extremely icy. Slip-on traction cleats are highly recommended."},
            {"q": "How to pack for low-light photography?", "a": "Bring a sturdy travel tripod (essential for long exposures), spare batteries (keep them in an inside pocket to stay warm), and a remote shutter release."},
            {"q": "What should be rented versus brought?", "a": "Bring your own base and mid-layers. You can often rent heavy parkas and boots from tour operators if you don't want to buy them for one trip."},
            {"q": "What travelers commonly forget?", "a": "A sleep eye mask. If you are sleeping during the day after a long night of aurora hunting, a mask is essential, though less critical in the dark winter than in summer."}
        ],
        "categories": {
            "Clothing": ["Wind/Waterproof shell jacket", "Waterproof trousers", "Merino wool base layers", "Fleece/Wool mid-layer"],
            "Footwear": ["Insulated waterproof boots", "Thick wool socks"],
            "Accessories": ["Windproof gloves & liners", "Balaclava / Neck warmer", "Slip-on traction cleats (microspikes)"],
            "Tech & Gear": ["Headlamp (with red light option)", "Travel tripod", "Spare camera/phone batteries"],
            "Documents & Health": ["Eye mask (for daytime sleep)", "Swimwear (for geothermal pools)"]
        },
        "rent_leave": "Leave at home: Umbrellas (they will break instantly in the Icelandic wind). Rent/Borrow: Heavy parkas (if doing specialized tours).",
        "breadcrumb": "<li><a class=\"hover:text-brand-terracotta transition-colors\" href=\"#\">Iceland</a></li>\n<li class=\"flex items-center\"><span class=\"material-symbols-outlined text-[16px] mx-1 opacity-50\">chevron_right</span></li>\n<li>Reykjavik Northern Lights</li>"
    },
    {
        "id": "rovaniemi-lapland",
        "url_path": "/packing-list/finland/rovaniemi-lapland",
        "title": "Your Packing Checklist for Rovaniemi Lapland - PackRight",
        "meta_desc": "Get a personalized AI packing list for Rovaniemi, Lapland. Essential gear for Arctic cold, Santa Village, husky sledding, and family winter travel.",
        "h1": "Rovaniemi Lapland Packing List",
        "prompt": "5 days in Rovaniemi in December with two kids, visiting Santa Village, doing husky and reindeer rides, and hoping to see the Northern Lights.",
        "expert_tip": "Tour Supplied Gear: Most safari operators (for huskies or snowmobiles) provide heavy thermal overalls and boots. Focus your packing on the high-quality base and mid-layers that go underneath.",
        "context_block": "<p>A trip to Rovaniemi, the official hometown of Santa Claus, is a bucket-list family adventure set in extreme Arctic conditions. Temperatures frequently drop to -20°C (-4°F) or lower. Keeping yourself and your children warm is the absolute priority of this packing list.</p><p>Unlike Iceland, which is wet and windy, Lapland is usually characterized by dry, biting cold and deep snow. You will need exceptional thermal insulation. While tour operators provide the massive outer thermal suits for excursions, you are responsible for the layers underneath, your time walking around Santa Claus Village, and evening meals.</p><p>Tell PackRight the ages of your travelers, and we'll ensure the generated list accounts for kid-specific winter necessities and excursion plans.</p>",
        "faqs": [
            {"q": "What weather-specific layers are needed for Lapland?", "a": "High-quality thermal base layers (Merino wool is best), thick fleece mid-layers, and a heavy winter coat for when you aren't wearing tour-supplied thermal suits."},
            {"q": "What should be rented versus brought?", "a": "Bring base layers, mid-layers, hats, and gloves. You can usually rely on tour operators to supply the heavy extreme-cold boots and thermal overalls for safaris."},
            {"q": "What changes for families or first-time visitors?", "a": "Kids need extra sets of gloves and socks, as theirs often get wet playing in the snow. Pack chemical hand warmers to prevent tantrums in the cold."},
            {"q": "What are the best gloves for Lapland?", "a": "Avoid fingered gloves. Wear thin liner gloves underneath thick, insulated mittens. Mittens trap heat much more effectively."},
            {"q": "Is an action camera necessary?", "a": "A chest-mounted action camera is great for capturing husky or snowmobile rides when your hands are busy and it's too cold to hold a phone."},
            {"q": "What do travelers commonly forget?", "a": "A good thermos flask to carry hot berry juice or tea during long outdoor excursions or Northern Lights waits."}
        ],
        "categories": {
            "Clothing": ["Heavy winter coat", "Merino wool base layers", "Fleece/Wool mid-layer", "Snow pants"],
            "Footwear": ["Waterproof snow boots", "Thermal wool socks (multiple pairs)"],
            "Accessories": ["Insulated mittens & liner gloves", "Balaclava / Neck warmer", "Chemical hand warmers"],
            "Tech & Gear": ["Portable charger (kept inside coat)", "Headlamp", "Thermos flask"],
            "Documents & Health": ["Moisturizer & lip balm", "Child-specific entertainment (for travel)"]
        },
        "rent_leave": "Leave at home: Cotton layers (they retain moisture and make you freeze). Rent/Borrow: Extreme thermal overalls and boots (often provided by tour operators).",
        "breadcrumb": "<li><a class=\"hover:text-brand-terracotta transition-colors\" href=\"#\">Finland</a></li>\n<li class=\"flex items-center\"><span class=\"material-symbols-outlined text-[16px] mx-1 opacity-50\">chevron_right</span></li>\n<li>Rovaniemi Lapland</li>"
    },
    {
        "id": "varanasi-diwali",
        "url_path": "/packing-list/india/varanasi-diwali",
        "title": "Your Packing Checklist for Varanasi Diwali - PackRight",
        "meta_desc": "Get a personalized AI packing list for Diwali in Varanasi. Essential gear for the ghats, religious sites, family visits, and festive clothing.",
        "h1": "Varanasi Diwali Packing List",
        "prompt": "4 days in Varanasi during Diwali, visiting family, attending Ganga Aarti, taking a boat ride, and wearing festive clothing.",
        "expert_tip": "Respectful & Practical Dress: Pack modest, breathable clothing that covers shoulders and knees for temple visits, and wear slip-on shoes since you'll take them off frequently.",
        "context_block": "<p>Visiting Varanasi during Diwali and Dev Deepawali is a profoundly spiritual, chaotic, and beautiful experience. The ghats are illuminated by millions of diyas (oil lamps), and the crowds are immense. Your packing list must balance festive cultural participation with the gritty reality of navigating one of the world's oldest living cities.</p><p>November weather is generally pleasant (warm days, cool evenings), so breathable layers are ideal. You will need modest clothing for religious sites, and a secure crossbody bag to navigate the dense, narrow alleys safely. Because of the dust, smoke from fireworks, and general pollution during the festival, health and hygiene items are critical.</p><p>Use PackRight to generate a list that accommodates your specific festival plans, family gifts, and photography gear.</p>",
        "faqs": [
            {"q": "What shoes are suitable for Varanasi?", "a": "Comfortable, closed-toe walking shoes for navigating dirty, uneven streets, plus a pair of easy slip-on sandals for temple visits where footwear is prohibited."},
            {"q": "How should I dress for the ghats and temples?", "a": "Modestly. Both men and women should cover their shoulders and knees. Women often carry a lightweight dupatta or shawl to drape over their heads or shoulders."},
            {"q": "What health items are necessary?", "a": "Hand sanitizer, wet wipes, and an N95 mask (smoke from Diwali firecrackers and dust can heavily impact air quality)."},
            {"q": "Are gifts important to pack?", "a": "If visiting family, pack sweets, dry fruits, or gifts. Bring a foldable tote bag or leave extra room in your luggage."},
            {"q": "How should I manage cash?", "a": "Carry a hidden money belt or secure crossbody bag. You need small denomination Rupee notes for auto-rickshaws, small vendors, and temple donations."},
            {"q": "What travelers commonly forget?", "a": "A portable power bank. Taking photos and navigating the labyrinthine alleys with GPS will drain your phone battery quickly."}
        ],
        "categories": {
            "Clothing": ["Modest, breathable daywear", "Festive evening attire (Kurta/Sari)", "Light shawl / Dupatta"],
            "Footwear": ["Comfortable walking shoes", "Slip-on sandals (for temples)"],
            "Accessories": ["Secure crossbody bag / Money belt", "Sunglasses & hat"],
            "Tech & Gear": ["Power bank", "Universal adapter (Type D/C)"],
            "Documents & Health": ["Hand sanitizer & wet wipes", "N95 mask (for smoke/dust)", "Personal medication kit"]
        },
        "rent_leave": "Leave at home: Revealing clothing (shorts/tank tops) which are inappropriate for Varanasi's religious context. Rent/Borrow: N/A.",
        "breadcrumb": "<li><a class=\"hover:text-brand-terracotta transition-colors\" href=\"#\">India</a></li>\n<li class=\"flex items-center\"><span class=\"material-symbols-outlined text-[16px] mx-1 opacity-50\">chevron_right</span></li>\n<li>Varanasi Diwali</li>"
    },
    {
        "id": "jaipur-diwali",
        "url_path": "/packing-list/india/jaipur-diwali",
        "title": "Your Packing Checklist for Jaipur Diwali - PackRight",
        "meta_desc": "Get a personalized AI packing list for Diwali in Jaipur. Essential gear for palace tours, market shopping, festive events, and warm city walking.",
        "h1": "Jaipur Diwali Packing List",
        "prompt": "5 days in Jaipur for Diwali, staying in a heritage hotel, shopping in the bazaars, visiting forts, and doing photography.",
        "expert_tip": "Expandable Luggage: Jaipur is famous for its textiles, jewelry, and handicrafts. Pack a foldable duffel or use an expandable suitcase to bring your shopping home.",
        "context_block": "<p>Experiencing Diwali in Jaipur, the Pink City, is a visually stunning affair. The city's markets and heritage buildings are famously illuminated, creating a spectacular atmosphere for shopping and photography. Compared to the dense spiritual intensity of Varanasi, Jaipur during Diwali leans more toward heritage tourism, grand celebrations, and extensive bazaar shopping.</p><p>Your packing list should reflect warm, sunny daytime conditions for exploring the Amer Fort, and slightly cooler evenings for enjoying the festival lights. Comfortable walking shoes are a must for the expansive palaces. Since Jaipur is a shopper's paradise, optimizing your luggage space for souvenirs is highly recommended.</p><p>Tell PackRight about your itinerary, and it will ensure you have the right mix of sightseeing practicality and festive elegance.</p>",
        "faqs": [
            {"q": "What weather-specific layers are needed for Jaipur in November?", "a": "Days are warm and sunny; pack breathable cottons or linens. Evenings can get slightly chilly, so a light sweater or shawl is perfect."},
            {"q": "What shoes are suitable?", "a": "Comfortable, breathable walking shoes for exploring the massive courtyards of the forts and palaces, and smart sandals for evening dinners."},
            {"q": "How to pack for the signature activity (shopping)?", "a": "Bring an expandable suitcase or pack a foldable, lightweight duffel bag inside your main luggage to carry textiles, blue pottery, and gifts back home."},
            {"q": "How should I dress for sightseeing?", "a": "While more relaxed than religious hubs, modesty is still appreciated. Opt for loose, comfortable clothing that covers the knees and shoulders."},
            {"q": "What photography gear is necessary?", "a": "Jaipur is incredibly photogenic, especially illuminated for Diwali. Bring a good camera or clean your phone lenses, and a power bank is absolutely essential."},
            {"q": "What travelers commonly forget?", "a": "High SPF sunscreen and a sun hat. The Rajasthani sun is intense during midday fort tours, even in November."}
        ],
        "categories": {
            "Clothing": ["Breathable daytime clothing (cotton/linen)", "Festive evening outfit", "Light sweater or shawl"],
            "Footwear": ["Comfortable walking shoes", "Smart sandals"],
            "Accessories": ["Sunglasses & sun hat", "Secure day bag for markets"],
            "Tech & Gear": ["Power bank", "Camera equipment", "Universal adapter"],
            "Documents & Health": ["Foldable shopping duffel", "Sunscreen"]
        },
        "rent_leave": "Leave at home: Heavy winter jackets. Rent/Borrow: N/A.",
        "breadcrumb": "<li><a class=\"hover:text-brand-terracotta transition-colors\" href=\"#\">India</a></li>\n<li class=\"flex items-center\"><span class=\"material-symbols-outlined text-[16px] mx-1 opacity-50\">chevron_right</span></li>\n<li>Jaipur Diwali</li>"
    },
    {
        "id": "tromso-northern-lights",
        "url_path": "/packing-list/norway/tromso-northern-lights",
        "title": "Your Packing Checklist for Tromsø Northern Lights - PackRight",
        "meta_desc": "Get a personalized AI packing list for a Tromsø Northern Lights trip. Essential gear for Arctic excursions, dog sledding, snowmobiling, and extreme cold.",
        "h1": "Tromsø Northern Lights Packing List",
        "prompt": "5 days in Tromsø in February, doing Northern lights tours, dog sledding, staying in the city, and doing some photography.",
        "expert_tip": "The 3-Layer Rule: Arctic survival relies on layering. You need a wicking base layer (Merino wool), an insulating mid-layer (thick fleece/wool), and a wind/waterproof outer shell.",
        "context_block": "<p>Located high above the Arctic Circle, Tromsø is one of the premier destinations for Northern Lights hunting and snow-based excursions like dog sledding and snowmobiling. A trip here involves prolonged exposure to extreme Arctic elements, combining deep snow, biting winds, and plunging temperatures.</p><p>Your packing list must prioritize heavy-duty insulation. While Tromsø the city is relatively mild due to the Gulf Stream, the inland valleys where you hunt for the aurora are brutally cold. You need proper waterproof, insulated snow boots, high-quality mittens (which are much warmer than fingered gloves), and dedicated thermal layers.</p><p>PackRight will generate a list that ensures you stay warm on the sleds while keeping your camera batteries alive in the freezing conditions.</p>",
        "faqs": [
            {"q": "What weather-specific layers are needed for Tromsø?", "a": "Merino wool thermal underwear, a thick wool sweater or heavy fleece, and a heavily insulated, windproof and waterproof parka or winter coat."},
            {"q": "What shoes are suitable for Tromsø?", "a": "Insulated, waterproof Arctic winter boots with heavy tread. Standard city boots or hiking boots will not keep your feet warm standing in the snow at night."},
            {"q": "What should be rented versus brought?", "a": "Tour operators almost always provide the extreme thermal suits and boots for dog sledding and snowmobiling. You must bring the high-quality base and mid-layers."},
            {"q": "What are the best gloves?", "a": "Bring thin touchscreen liner gloves to wear underneath heavy, insulated mittens. You can slip off the mitten to take a photo without exposing bare skin."},
            {"q": "How to pack for the signature activity?", "a": "For Northern lights photography, bring a sturdy tripod and a headlamp with a red-light setting (to preserve your night vision)."},
            {"q": "What changes for first-time Arctic visitors?", "a": "You'll need chemical hand and toe warmers, and you must remember to keep your phone and spare batteries in an inner pocket close to your body heat."}
        ],
        "categories": {
            "Clothing": ["Insulated winter parka", "Merino wool base layers", "Heavy wool/fleece mid-layer", "Snow pants"],
            "Footwear": ["Insulated waterproof winter boots", "Thick wool socks (multiple pairs)"],
            "Accessories": ["Insulated mittens & touchscreen liners", "Balaclava / Neck warmer", "Chemical hand warmers"],
            "Tech & Gear": ["Headlamp (with red light)", "Travel tripod", "Spare batteries (keep warm)"],
            "Documents & Health": ["Lip balm & heavy moisturizer", "Small daypack"]
        },
        "rent_leave": "Leave at home: Cotton base layers (they trap sweat and make you cold). Rent/Borrow: Extreme Arctic outer suits (provided by tour companies).",
        "breadcrumb": "<li><a class=\"hover:text-brand-terracotta transition-colors\" href=\"#\">Norway</a></li>\n<li class=\"flex items-center\"><span class=\"material-symbols-outlined text-[16px] mx-1 opacity-50\">chevron_right</span></li>\n<li>Tromsø Northern Lights</li>"
    },
    {
        "id": "strasbourg-christmas-markets",
        "url_path": "/packing-list/france/strasbourg-christmas-markets",
        "title": "Your Packing Checklist for Strasbourg Christmas Markets - PackRight",
        "meta_desc": "Get a personalized AI packing list for the Strasbourg Christmas markets. Essential gear for walking the Capital of Christmas, train travel, and winter weather.",
        "h1": "Strasbourg Christmas Market Packing List",
        "prompt": "3 days in Strasbourg for the Christmas markets, travelling by train from Paris, lots of walking, and shopping for decorations.",
        "expert_tip": "Carry-On Agility: Strasbourg is best accessed via the TGV train. Pack a compact, easy-to-maneuver carry-on suitcase to navigate train stations and crowded market streets effortlessly.",
        "context_block": "<p>Known as the 'Capital of Christmas,' Strasbourg hosts one of the oldest and most spectacular markets in Europe. A trip here is highly concentrated: you will be walking extensively between the various themed markets spread across the Grande Île, enjoying Vin Chaud, and navigating dense, festive crowds.</p><p>Because many travelers visit Strasbourg via a fast train from Paris or Germany, luggage agility is paramount. Your packing list should focus on a compact, highly organized carry-on, coupled with exceptional walking boots and warm, stylish layers. The weather can be damp and chilly, so a waterproof coat and a compact umbrella are necessary additions to your daily daypack.</p><p>Input your exact travel style, and PackRight will build a list prioritizing both festive charm and logistical ease.</p>",
        "faqs": [
            {"q": "What weather-specific layers are needed?", "a": "Pack a warm, waterproof winter coat, a comfortable scarf, gloves, and thermal tops. The damp cold in the Alsace region can feel sharper than dry cold."},
            {"q": "What shoes are suitable for Strasbourg?", "a": "Waterproof walking boots or extremely comfortable, weather-treated sneakers. You will be walking miles on cobblestones each day."},
            {"q": "Is a large suitcase necessary?", "a": "No. Navigating train aisles and cobblestone streets with massive luggage is frustrating. Bring a smart carry-on and a foldable tote for purchases."},
            {"q": "How should I carry my belongings safely?", "a": "The markets get incredibly crowded. Wear a secure crossbody bag worn at the front to deter pickpockets and keep your hands free for food and drinks."},
            {"q": "Should I bring an umbrella?", "a": "Yes, a compact, wind-resistant travel umbrella is highly recommended as December can bring cold rain or wet snow."},
            {"q": "What travelers commonly forget?", "a": "A portable charger. The cold weather drains batteries quickly, and you will be taking countless photos of the spectacular decorations."}
        ],
        "categories": {
            "Clothing": ["Warm waterproof coat", "Layering sweaters/cardigans", "Thermal tops"],
            "Footwear": ["Waterproof walking boots", "Warm socks"],
            "Accessories": ["Scarf, gloves, and hat", "Secure crossbody bag", "Compact travel umbrella"],
            "Tech & Gear": ["Portable charger", "Foldable shopping tote (for market gifts)"],
            "Documents & Health": ["Blister care", "Cash (Euros)"]
        },
        "rent_leave": "Leave at home: Massive hard-shell suitcases (difficult on trains and cobblestones). Rent/Borrow: N/A.",
        "breadcrumb": "<li><a class=\"hover:text-brand-terracotta transition-colors\" href=\"/packing-list/europe\">Europe</a></li>\n<li class=\"flex items-center\"><span class=\"material-symbols-outlined text-[16px] mx-1 opacity-50\">chevron_right</span></li>\n<li>Strasbourg Christmas Markets</li>"
    },
    {
        "id": "sapporo-snow-festival",
        "url_path": "/packing-list/japan/sapporo-snow-festival",
        "title": "Your Packing Checklist for Sapporo Snow Festival - PackRight",
        "meta_desc": "Get a personalized AI packing list for the Sapporo Snow Festival. Essential gear for freezing city walking, ice sculptures, and Hokkaido winter conditions.",
        "h1": "Sapporo Snow Festival Packing List",
        "prompt": "4 days in Sapporo in February for the Snow Festival, exploring the ice sculptures at Odori Park, eating lots of ramen, mostly city walking.",
        "expert_tip": "Traction is Mandatory: Sapporo's sidewalks turn into sheets of compacted ice. If you don't have dedicated winter boots with deep treads, you MUST buy slip-on ice cleats at a local convenience store.",
        "context_block": "<p>The Sapporo Snow Festival is a spectacular urban winter event, drawing millions to see massive, intricate snow and ice sculptures. However, it takes place in February in Hokkaido, meaning you will face severe winter conditions, heavy snowfall, and dangerously icy city sidewalks.</p><p>Unlike a ski trip to Niseko, this is an urban walking holiday. Your packing list must focus on extreme cold-weather city gear: heavily insulated waterproof boots (with excellent grip), long thermal underwear, and a heavy winter coat. You'll spend hours standing still in Odori Park admiring the sculptures, so chemical hand warmers and thick mittens are lifesavers.</p><p>Let PackRight know if you are extending your trip to go skiing, and we will automatically adapt the list to include the necessary active sports gear.</p>",
        "faqs": [
            {"q": "What shoes are suitable for Sapporo in winter?", "a": "Insulated, waterproof winter boots with aggressive, anti-slip treads. The compacted snow on the sidewalks is incredibly slippery."},
            {"q": "Do I need traction cleats (microspikes)?", "a": "Yes. If your boots lack specialized winter grip, slip-on traction cleats are essential to avoid falls. You can buy them cheaply in Sapporo."},
            {"q": "What weather-specific layers are needed?", "a": "Thermal base layers (Heattech or Merino wool), a thick sweater, and a wind/waterproof heavy winter coat. Snow pants are optional but useful for the Tsudome site."},
            {"q": "How to pack for the signature activity?", "a": "For photographing the illuminated ice sculptures at night, bring touchscreen-friendly gloves and keep a portable charger close to your body heat."},
            {"q": "What changes for first-time visitors?", "a": "The contrast between the freezing outdoors and the heavily heated indoor malls and subway is intense. Wear layers you can quickly unzip or remove."},
            {"q": "What travelers commonly forget?", "a": "Hand and toe warmers (Kairo). While you can buy them easily in Japan, having a few packs ready for your first night is very helpful."}
        ],
        "categories": {
            "Clothing": ["Heavy insulated winter coat", "Thermal base layers", "Thick sweater/fleece", "Snow pants (optional)"],
            "Footwear": ["Insulated waterproof boots (high traction)", "Thick wool socks"],
            "Accessories": ["Mittens & touchscreen liners", "Warm hat & scarf", "Slip-on ice cleats"],
            "Tech & Gear": ["Portable charger", "Camera gear for night photography"],
            "Documents & Health": ["Hand & toe warmers (Kairo)", "Cash (Yen)"]
        },
        "rent_leave": "Leave at home: Standard sneakers or smooth-soled shoes (you will fall). Rent/Borrow: N/A unless renting ski gear nearby.",
        "breadcrumb": "<li><a class=\"hover:text-brand-terracotta transition-colors\" href=\"/packing-list/japan\">Japan</a></li>\n<li class=\"flex items-center\"><span class=\"material-symbols-outlined text-[16px] mx-1 opacity-50\">chevron_right</span></li>\n<li>Sapporo Snow Festival</li>"
    }
]

# 2. Add products to affiliates.json
def update_affiliates():
    affiliates_path = r'c:\Users\HI\packright\data\affiliates.json'
    with open(affiliates_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    existing_ids = [p['id'] for p in data['products']]
    
    new_products = [
        {
            "id": "waterproof-walking-boots",
            "name": "Waterproof Winter Walking Boots",
            "label": "Find on Amazon →",
            "keywords": ["waterproof walking boots", "winter boots", "snow boots", "insulated boots"],
            "links": {"default": "https://www.amazon.com/s?k=waterproof+winter+walking+boots&tag=PACKRIGHT-21"}
        },
        {
            "id": "carry-on-suitcase",
            "name": "Expandable Carry-On Suitcase",
            "label": "Find on Amazon →",
            "keywords": ["carry-on suitcase", "expandable suitcase", "cabin luggage", "compact luggage"],
            "links": {"default": "https://www.amazon.com/s?k=expandable+carry-on+suitcase&tag=PACKRIGHT-21"}
        },
        {
            "id": "action-camera",
            "name": "Action Camera / GoPro",
            "label": "Find on Amazon →",
            "keywords": ["action camera", "gopro", "waterproof camera", "travel camera"],
            "links": {"default": "https://www.amazon.com/s?k=action+camera+travel&tag=PACKRIGHT-21"}
        },
        {
            "id": "arctic-parka",
            "name": "Insulated Arctic Parka",
            "label": "Find on Amazon →",
            "keywords": ["arctic parka", "heavy winter coat", "insulated winter coat"],
            "links": {"default": "https://www.amazon.com/s?k=insulated+arctic+parka+winter+coat&tag=PACKRIGHT-21"}
        },
        {
            "id": "garment-steamer",
            "name": "Portable Garment Steamer",
            "label": "Find on Amazon →",
            "keywords": ["garment steamer", "travel steamer", "clothes steamer"],
            "links": {"default": "https://www.amazon.com/s?k=portable+travel+garment+steamer&tag=PACKRIGHT-21"}
        }
    ]
    
    for product in new_products:
        if product['id'] not in existing_ids:
            data['products'].append(product)
            
    with open(affiliates_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

# 3. Generate HTML Pages
def generate_pages():
    template_path = r'c:\Users\HI\packright\packing-list\japan\index.html'
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    for page in pages_data:
        html = template
        
        # SEO & Meta
        html = html.replace('<title>Your Packing Checklist for Japan - PackRight</title>', f'<title>{page["title"]}</title>')
        html = html.replace('content="Get a personalized AI packing list for Japan. Essential gear for Tokyo, Kyoto, Mount Fuji, and navigating the seasons."', f'content="{page["meta_desc"]}"')
        html = html.replace('https://packright-20.vercel.app/packing-list/japan/', f'https://packright-20.vercel.app{page["url_path"]}')
        
        # Open Graph
        html = html.replace('content="Your Packing Checklist for Japan - PackRight"', f'content="{page["title"]}"')
        
        # Headers & Prompts
        html = html.replace('Japan Packing List', page["h1"])
        html = html.replace('14 days in Japan, flying into Tokyo, visiting Kyoto and Osaka, mostly train travel, doing some hiking, staying in a mix of hotels and ryokans.', page["prompt"])
        
        # Expert Tip & Context
        html = html.replace('Layers are Key: Japan’s weather can vary wildly. Bring layers that are easy to take on and off, especially since indoor spaces are heavily heated in winter.', page["expert_tip"])
        # We need to replace the context block. In the template, it's 2 paragraphs inside a specific div.
        # Let's do a simple string replace for the paragraphs.
        old_context = "<p class=\"text-body-md text-on-surface-variant mb-4\">\n                    Whether you're navigating the neon-lit streets of Shinjuku or walking the peaceful Nakasendo trail, Japan demands a versatile packing strategy. Your list will heavily depend on the season—summers are intensely hot and humid requiring breathable fabrics, while winters in Hokkaido or the Alps require serious snow gear.\n                </p>\n                <p class=\"text-body-md text-on-surface-variant\">\n                    A universal rule for Japan: pack shoes that are easy to slip on and off, as you will constantly remove them for temples, ryokans, and fitting rooms. Additionally, space is a premium. Opt for a compact, easy-to-carry suitcase as maneuvering massive luggage on the Shinkansen (bullet trains) or subway stations can be a major hassle.\n                </p>"
        html = html.replace(old_context, page["context_block"])
        
        # Breadcrumb
        old_breadcrumb = "<li><a class=\"hover:text-brand-terracotta transition-colors\" href=\"/packing-list/japan\">Japan</a></li>"
        html = html.replace(old_breadcrumb, page["breadcrumb"])
        
        # Rent / Leave
        old_rent_leave = "Leave at home: Heavy bath towels (ryokans and hotels provide excellent ones) and excessive cash (while cash is used, ATMs are everywhere). Rent/Borrow: Pocket Wi-Fi can be rented at the airport."
        html = html.replace(old_rent_leave, page["rent_leave"])

        # FAQs
        # We need to dynamically replace the FAQ section.
        # It's easier to find the div containing FAQs and replace its inner HTML.
        faq_html = ""
        faq_schema = []
        for i, faq in enumerate(page["faqs"]):
            faq_html += f"""
                <div class="border-b border-outline-variant/30 pb-4">
                    <h4 class="font-title-lg text-label-md font-bold mb-2 text-on-surface">{faq['q']}</h4>
                    <p class="text-body-md text-on-surface-variant text-sm">{faq['a']}</p>
                </div>"""
            faq_schema.append({
                "@type": "Question",
                "name": faq['q'],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": faq['a']
                }
            })
            
        # The easiest way to replace FAQs is to use regex or string markers.
        # In the template, there is a grid with FAQs.
        import re
        html = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">.*?</div>\n\s*<div class="mt-8 bg-surface-container', 
                      f'<div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">{faq_html}</div>\n                <div class="mt-8 bg-surface-container', 
                      html, flags=re.DOTALL)
                      
        # Replace FAQ schema
        schema_match = re.search(r'"@type": "FAQPage",\s*"@id": "https://packright-20.vercel.app/packing-list/japan/#faq",\s*"mainEntity": \[.*?\]', html, flags=re.DOTALL)
        if schema_match:
            new_schema = f'"@type": "FAQPage",\n      "@id": "https://packright-20.vercel.app{page["url_path"]}/#faq",\n      "mainEntity": {json.dumps(faq_schema, indent=6)}'
            html = html.replace(schema_match.group(0), new_schema)

        # Categories
        cat_html = ""
        for cat_name, items in page["categories"].items():
            cat_html += f"""
                    <div>
                        <h4 class="font-title-lg text-label-md font-bold mb-3 text-on-surface border-b border-outline-variant/30 pb-2">{cat_name}</h4>
                        <ul class="space-y-2">"""
            for item in items:
                cat_html += f"""
                            <li class="flex items-start">
                                <span class="material-symbols-outlined text-brand-terracotta text-[18px] mr-2 mt-0.5">check_circle</span>
                                <span class="text-body-md text-on-surface text-sm">{item}</span>
                            </li>"""
            cat_html += """
                        </ul>
                    </div>"""
                    
        html = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">.*?</div>\n\s*<!-- Rent or Leave -->',
                      f'<div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">{cat_html}</div>\n                <!-- Rent or Leave -->',
                      html, flags=re.DOTALL)

        # Make sure directory exists
        file_path = os.path.join(r'c:\Users\HI\packright', page["url_path"].lstrip('/'), 'index.html')
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Generated {file_path}")

update_affiliates()
generate_pages()
