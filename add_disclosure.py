import os
import glob
import re

files = glob.glob(r'c:\Users\HI\packright\packing-list\**\*.html', recursive=True)

disclosure_html = """
            <div class="px-6 py-4 mt-4 mb-4 text-xs text-on-surface-variant bg-surface-container-lowest border-t border-outline-variant/30 text-center">
                <strong>Affiliate disclosure:</strong> Some links on this page are affiliate links. If you purchase through them, PackRight may earn a commission at no additional cost to you. As an Amazon Associate, we earn from qualifying purchases.
            </div>
"""

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Inject just above the "I'm Done, Thanks!" button container if not already there
    if 'Affiliate disclosure:' not in html:
        html = html.replace('<div class="px-6 py-4 bg-white/95 backdrop-blur-md border-t border-outline-variant/10 z-10 sticky bottom-0">',
                            disclosure_html + '\n            <div class="px-6 py-4 bg-white/95 backdrop-blur-md border-t border-outline-variant/10 z-10 sticky bottom-0">')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Added disclosure to {file}")
