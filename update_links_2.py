import re

fuji_path = 'packing-list/japan/mount-fuji-climbing/index.html'
niseko_path = 'packing-list/japan/niseko-skiing/index.html'

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Update Fuji
fuji_html = read_file(fuji_path)

# Portable Oxygen Canister (was already an affiliate link)
fuji_html = re.sub(
    r'<a href="https://www\.amazon\.in/s\?k=portable\+oxygen\+canister\+hiking&tag=packright-21" target="_blank"',
    r'<a href="https://link.amazon/B0dVZ235R" target="_blank"',
    fuji_html
)

write_file(fuji_path, fuji_html)

print("Oxygen canister fixed!")
