import os
import shutil

destinations = [
    {
        "id": "thailand",
        "title": "Your Packing Checklist for Thailand - PackRight",
        "meta_desc": "Get a personalized AI packing list for Thailand. Essential gear for Bangkok, Chiang Mai, the islands, temple visits, and tropical climates.",
        "canonical": "https://packright-20.vercel.app/packing-list/thailand/",
        "h1": "Thailand Packing List",
        "prompt": "2 weeks in Thailand, staying in Bangkok and island hopping in Phuket, mostly budget travel.",
        "expert_tip": "Temple Dress Codes: Most temples (like the Grand Palace) strictly require shoulders and knees to be covered. Always carry a lightweight sarong or scarf.",
        "categories": {
            "Clothing": ["Lightweight linen shirt", "Breathable shorts", "Sarong/Scarf for temples"],
            "Toiletries & Health": ["Reef-safe sunscreen", "DEET mosquito repellent"],
            "Tech & Electronics": ["Universal adapter", "Power bank"],
            "Documents & Money": ["Travel insurance", "Cash (Baht)"]
        }
    },
    {
        "id": "dubai",
        "title": "Your Packing Checklist for Dubai - PackRight",
        "meta_desc": "Get a personalized AI packing list for Dubai. Essential gear for desert safaris, luxury dining, malls, and navigating the UAE heat.",
        "canonical": "https://packright-20.vercel.app/packing-list/dubai/",
        "h1": "Dubai Packing List",
        "prompt": "5 days in Dubai, luxury trip, desert safari, fine dining and shopping.",
        "expert_tip": "Cultural Modesty: While Dubai is very modern, modest dress is expected in public spaces like malls and souks. Pack light layers that cover shoulders and knees.",
        "categories": {
            "Clothing": ["Smart casual evening wear", "Modest day clothes", "Swimwear (for hotel pool)"],
            "Toiletries & Health": ["High SPF Sunscreen", "Hydration salts", "Lip balm with SPF"],
            "Tech & Electronics": ["Type G adapter (UK style)", "Camera/smartphone"],
            "Documents & Money": ["Travel insurance", "Credit cards (widely accepted)"]
        }
    },
    {
        "id": "bali",
        "title": "Your Packing Checklist for Bali - PackRight",
        "meta_desc": "Get a personalized AI packing list for Bali. Essential gear for Ubud jungles, Seminyak beaches, scooter riding, and tropical weather.",
        "canonical": "https://packright-20.vercel.app/packing-list/bali/",
        "h1": "Bali Packing List",
        "prompt": "10 days in Bali, exploring Ubud, surfing in Canggu, and relaxing at a villa.",
        "expert_tip": "Scooter Safety & Sun: If renting a scooter, wear closed shoes and proper eye protection. The sun is intense, so a good rash guard is essential for surfing.",
        "categories": {
            "Clothing": ["Rash guard (for surfing)", "Breathable activewear", "Flip flops / Sandals"],
            "Toiletries & Health": ["Reef-safe sunscreen", "Mosquito repellent", "After-sun aloe vera"],
            "Tech & Electronics": ["Universal adapter", "Waterproof phone pouch"],
            "Documents & Money": ["International Driving Permit (for scooters)", "Cash (Rupiah)"]
        }
    }
]

base_file = r'c:\Users\HI\packright\packing-list\japan\index.html'

with open(base_file, 'r', encoding='utf-8') as f:
    base_html = f.read()

for dest in destinations:
    dir_path = os.path.join(r'c:\Users\HI\packright\packing-list', dest['id'])
    os.makedirs(dir_path, exist_ok=True)
    
    html = base_html
    # Replace Meta Tags
    html = html.replace('<title>Your Packing Checklist for Japan - PackRight</title>', f'<title>{dest["title"]}</title>')
    html = html.replace('content="Get a personalized AI packing list for Japan.', f'content="{dest["meta_desc"]}')
    html = html.replace('https://packright-20.vercel.app/packing-list/japan/', dest["canonical"])
    
    # Replace Headers & Prompts
    html = html.replace('Japan Packing List', dest["h1"])
    html = html.replace('14 days in Japan, flying into Tokyo, visiting Kyoto and Osaka, mostly train travel, doing some hiking, staying in a mix of hotels and ryokans.', dest["prompt"])
    html = html.replace('Layers are Key: Japan’s weather can vary wildly. Bring layers that are easy to take on and off, especially since indoor spaces are heavily heated in winter.', dest["expert_tip"])
    
    # Optional: Update Breadcrumbs
    html = html.replace('<li>Japan</li>', f'<li>{dest["id"].title()}</li>')

    # Remove Niseko specific HTML if present (so it doesn't bleed into these static pages)
    # The actual checklist container should be preserved.
    # Niseko module is handled in JS dynamically, but the HTML scaffolding we injected earlier might be there.
    # We can leave the hidden scaffolding since JS relies on it.

    file_path = os.path.join(dir_path, 'index.html')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Created {file_path}")

