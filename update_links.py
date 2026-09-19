import re

fuji_path = 'packing-list/japan/mount-fuji-climbing/index.html'
niseko_path = 'packing-list/japan/niseko-skiing/index.html'

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Update Niseko
niseko_html = read_file(niseko_path)
# GORE-TEX Ski Shell Jacket
niseko_html = re.sub(
    r'<a href="https://www\.amazon\.in/s\?k=gore-tex\+ski\+jacket\+winter&tag=packright-21" target="_blank"',
    r'<a href="https://link.amazon/B04Y0kHJZ" target="_blank"',
    niseko_html
)
# Low-Light Ski Goggles
niseko_html = re.sub(
    r'<a href="https://www\.amazon\.in/s\?k=ski\+goggles\+low\+light\+winter&tag=packright-21" target="_blank"',
    r'<a href="https://link.amazon/B0aGPczzX" target="_blank"',
    niseko_html
)
write_file(niseko_path, niseko_html)

# Update Fuji
fuji_html = read_file(fuji_path)
# Sturdy Waterproof Hiking Boots
fuji_html = re.sub(
    r'<a href="https://www\.amazon\.in/s\?k=waterproof\+hiking\+boots\+trekking&tag=packright-21" target="_blank"',
    r'<a href="https://link.amazon/B04qUaj9i" target="_blank"',
    fuji_html
)
# High-Lumen Headlamp
fuji_html = re.sub(
    r'<a href="https://www\.amazon\.in/s\?k=high\+lumen\+led\+headlamp\+rechargeable&tag=packright-21" target="_blank"',
    r'<a href="https://link.amazon/B0fXrU7wn" target="_blank"',
    fuji_html
)

# Portable Oxygen Canister didn't have an affiliate link in the previous restructuring. Let's add it.
fuji_html = re.sub(
    r'(<span class="font-body-md text-body-md text-text-rich block mb-1 group-hover:text-primary transition-colors">Portable Oxygen Canister)(</span>)',
    r'\1 <a href="https://link.amazon/B0dVZ235R" target="_blank" class="text-primary text-sm font-medium hover:underline ml-1 inline-block" onclick="event.stopPropagation()">View on Amazon.in &rarr;</a>\2',
    fuji_html
)

# Power Bank didn't have an affiliate link either. Let's add it.
fuji_html = re.sub(
    r'(<span class="font-body-md text-body-md text-text-rich block mb-1 group-hover:text-primary transition-colors">Power Bank)(</span>)',
    r'\1 <a href="https://link.amazon/B06gdsybU" target="_blank" class="text-primary text-sm font-medium hover:underline ml-1 inline-block" onclick="event.stopPropagation()">View on Amazon.in &rarr;</a>\2',
    fuji_html
)

write_file(fuji_path, fuji_html)

print("Links updated successfully!")
