import os
import re

fuji_path = 'packing-list/japan/mount-fuji-climbing/index.html'
niseko_path = 'packing-list/japan/niseko-skiing/index.html'

def fix_file(path, is_fuji):
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix JSON LD name for Fuji
    if is_fuji:
        html = html.replace('"name": "PackRight AI Packing List Generator - Niseko"', '"name": "PackRight AI Packing List Generator - Mount Fuji"')

    # Add canonical if missing
    url_slug = "mount-fuji-climbing" if is_fuji else "niseko-skiing"
    canonical_tag = f'<link rel="canonical" href="https://packright-20.vercel.app/packing-list/japan/{url_slug}" />'
    
    if 'rel="canonical"' not in html:
        html = html.replace('</title>', f'</title>\n<meta name="description" content="Prepare for your trip with a personalized AI-generated checklist. Expert tips and essentials.">\n{canonical_tag}')
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

fix_file(fuji_path, True)
fix_file(niseko_path, False)

print("Canonical and JSON-LD fixed!")
