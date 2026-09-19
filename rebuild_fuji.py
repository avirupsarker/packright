import os

niseko_path = 'packing-list/japan/niseko-skiing/index.html'
fuji_path = 'packing-list/japan/mount-fuji-climbing/index.html'

with open(niseko_path, 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    ("Niseko Skiing Packing List: 15 Essentials You're Forgetting", "Mount Fuji Climbing Gear List: 15 Safety Essentials"),
    ("generate personalized packing lists for Niseko skiing", "generate personalized packing lists for Mount Fuji climbing"),
    ("Your Packing Checklist for Niseko Skiing 🎿", "Your Packing Checklist for Mount Fuji Climbing 🌋"),
    ("Niseko offers world-class powder and a vibrant ski village atmosphere. Packing requires a mindful approach—from heavy-duty layers for the slopes to casual chic wear for the local izakayas and onsens.", "Mount Fuji is Japan's iconic peak. Climbing requires a mindful approach—from altitude-safe layers for the summit sunrise to sturdy footwear for the volcanic scree."),
    ("7 days in Tokyo and Kyoto in spring, temples, street food, lots of walking", "2 days climbing Mount Fuji via the Yoshida Trail in August, staying overnight in a mountain hut."),
    ("Expert Travel Tip: Pack heavy-duty touchscreen gloves", "Expert Travel Tip: Pack plenty of 100-yen coins"),
    ("Temperatures in Niseko routinely dip well below freezing. Keeping your hands warm while still being able to use your phone to navigate runs or take pictures is absolutely vital on the mountain.", "The toilets on Mt. Fuji are private and cost 200-300 yen. Coins are a genuine life-saver at 3,000 meters!"),
    ("Sample List: 7 Days Skiing in Niseko", "Sample List: 2 Days Climbing Mt. Fuji"),
    ("7 days ski trip to Niseko in peak winter (January), focusing on powder skiing, relaxing in local onsens, and exploring Hirafu village.", "2 days climbing Mt. Fuji via the Yoshida Trail, focusing on a safe sunrise summit and a stay in a mountain hut."),
    ("Slip-on walking shoes", "Sturdy waterproof hiking boots"),
    ("essential — you will take shoes off frequently at shrines, traditional restaurants, and ryokans", "essential — volcanic rock is sharp and loose"),
    ("Socks without holes (clean/neat)", "Insulated down jacket"),
    ("cultural norm — you'll walk on tatami mats in socks, make sure they are presentable", "crucial — summit temps drop below freezing at sunrise"),
    ("Versatile layering jacket", "GORE-TEX rain shell"),
    (">Documents &amp; Money<", ">Gear &amp; Essentials<"),
    ("Lift Pass Holder", "Headlamp with spare batteries"),
    ("essential — Niseko uses electronic lift passes that need to be scanned frequently", "mandatory — for the overnight hike to the summit in the dark"),
    ("IC Transit Card (Suica, Pasmo)", "100-Yen Coins"),
    ("Frequently Asked Questions — Niseko Skiing", "Frequently Asked Questions — Mount Fuji Climbing"),
    ("What kind of ski goggles are best for Niseko?", "Do I really need hiking boots?"),
    ("Low-Light or Rose-tinted lenses for flat-light powder days.", "Yes, the volcanic scree is sharp and loose. Sneakers will get destroyed."),
    ("Do I need formal clothes for Hirafu Village?", "How cold does it get at the summit?"),
    ("No, the vibe is 'Ski-Chic' and casual. Focus on warm boots and nice layers.", "Even in August, pre-dawn summit temperatures can drop below freezing, especially with wind chill."),
    ("Should I pack my own skis or rent?", "Do I need a headlamp?"),
    ("Renting is popular to avoid dragging bags on the Shinkansen; shops like Rhythm Japan carry top powder gear.", "Absolutely mandatory for the overnight hike to the summit for sunrise."),
    ("How do I handle luggage from the airport?", "What about altitude sickness?"),
    ("Use Yamato Transport (Takkyubin) to ship bags directly from New Chitose to your resort.", "Pack portable oxygen, hike slowly, stay hydrated, and take frequent breaks."),
    ("Will my electronics work?", "Can I buy water on the mountain?"),
    ("Yes, Type A/B plugs. Pack a cold-resistant power bank as batteries die fast in the Hokkaido cold.", "Yes, but it becomes much more expensive as you go higher. Bring plenty of cash."),
    ("Not going to Niseko?", "Not climbing Mt. Fuji?")
]

for old, new in replacements:
    html = html.replace(old, new)

with open(fuji_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Fuji page rebuilt!")
