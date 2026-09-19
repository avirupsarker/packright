import os
import re
import codecs

files = [
    'index.html',
    'packing-list/europe/index.html',
    'packing-list/japan/index.html',
    'packing-list/japan/niseko-skiing/index.html'
]

for filepath in files:
    if not os.path.exists(filepath):
        continue
    
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    parts = html.split('sample-category-header')
    new_html = parts[0]

    for i in range(1, len(parts)):
        part = parts[i]
        
        # Count the number of sample-item-row in this chunk (which corresponds to one category)
        count = part.count('sample-item-row')
        
        if count > 0:
            # Replace the badge
            part = re.sub(r'(<span class="[^"]*bg-primary/10 rounded-full">)\d+\s+[Ii]tems(</span>)', r'\g<1>' + str(count) + r' items\2', part)
        
        new_html += 'sample-category-header' + part

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(new_html)

print("Done fixing badges!")
