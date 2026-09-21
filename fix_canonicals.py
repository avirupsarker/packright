import os
import glob
import re

files = glob.glob(r'c:\Users\HI\packright\packing-list\**\*.html', recursive=True)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Calculate correct canonical
    # file is like c:\Users\HI\packright\packing-list\europe\prague-christmas-markets\index.html
    rel_path = file.split("packright\\")[1].replace("\\", "/").replace("/index.html", "")
    
    # The home URL would be https://packright-20.vercel.app/packing-list/...
    canonical_url = f"https://packright-20.vercel.app/{rel_path}"
    
    # In some hubs it might just be the direct path
    html = re.sub(r'<link rel="canonical" href=".*?" />', f'<link rel="canonical" href="{canonical_url}" />', html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Fixed canonical in {file} to {canonical_url}")
