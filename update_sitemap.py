import re

urls = [
    "https://packright-20.vercel.app/packing-list/europe/prague-christmas-markets",
    "https://packright-20.vercel.app/packing-list/europe/vienna-christmas-markets",
    "https://packright-20.vercel.app/packing-list/iceland/reykjavik-northern-lights",
    "https://packright-20.vercel.app/packing-list/finland/rovaniemi-lapland",
    "https://packright-20.vercel.app/packing-list/india/varanasi-diwali",
    "https://packright-20.vercel.app/packing-list/india/jaipur-diwali",
    "https://packright-20.vercel.app/packing-list/norway/tromso-northern-lights",
    "https://packright-20.vercel.app/packing-list/france/strasbourg-christmas-markets",
    "https://packright-20.vercel.app/packing-list/japan/sapporo-snow-festival"
]

sitemap_path = r'c:\Users\HI\packright\sitemap.xml'

with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap = f.read()

urls_html = ""
for url in urls:
    urls_html += f"""
    <url>
        <loc>{url}</loc>
        <lastmod>2026-09-20</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>"""

sitemap = sitemap.replace('</urlset>', urls_html + '\n</urlset>')

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap)
    
print("Updated sitemap")
