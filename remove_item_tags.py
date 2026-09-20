import os
import re

files = [
    r'c:\Users\HI\packright\packing-list\japan\index.html',
    r'c:\Users\HI\packright\packing-list\japan\niseko-skiing\index.html',
    r'c:\Users\HI\packright\packing-list\japan\mount-fuji-climbing\index.html'
]

pattern = re.compile(r'<span class="bg-primary-fixed[^>]*>.*?items</span>')

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the pattern with an empty string
        new_content = pattern.sub('', content)
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
        else:
            print(f"No changes in {filepath}")

