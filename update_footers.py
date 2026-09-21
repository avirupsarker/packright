import os
import glob

files = glob.glob(r'c:\Users\HI\packright\**\*.html', recursive=True)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '>Americas</a></li>' in content:
        # We replace the Americas link with Thailand, Dubai, Bali and Americas
        replacement = '>Americas</a></li>\n<li class=""><a class="text-on-surface-variant hover:text-primary transition-colors text-label-md hover:text-brand-terracotta" href="/packing-list/thailand">Thailand</a></li>\n<li class=""><a class="text-on-surface-variant hover:text-primary transition-colors text-label-md hover:text-brand-terracotta" href="/packing-list/dubai">Dubai</a></li>\n<li class=""><a class="text-on-surface-variant hover:text-primary transition-colors text-label-md hover:text-brand-terracotta" href="/packing-list/bali">Bali</a></li>'
        new_content = content.replace('>Americas</a></li>', replacement)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated footer in {file}")

