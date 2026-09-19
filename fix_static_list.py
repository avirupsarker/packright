import os
import re

files = [
    'packing-list/europe/index.html',
    'packing-list/japan/index.html',
    'packing-list/japan/niseko-skiing/index.html',
    'packing-list/japan/mount-fuji-climbing/index.html'
]

# We need to add the accordion JS before </body>
accordion_js = """
<script>
document.addEventListener('DOMContentLoaded', () => {
    // Select all category headers in the static sample list
    const headers = document.querySelectorAll('.cursor-pointer.hover\\\\:bg-surface-container');
    headers.forEach(header => {
        header.addEventListener('click', () => {
            // Find the content div right after the header
            const content = header.nextElementSibling;
            const icon = header.querySelector('.material-symbols-outlined');
            
            if (content.style.display === 'none') {
                content.style.display = 'block';
                if (icon) icon.textContent = 'expand_less';
            } else {
                content.style.display = 'none';
                if (icon) icon.textContent = 'expand_more';
            }
        });
    });
});
</script>
</body>
"""

for filepath in files:
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Split by the category wrapper
    cat_wrapper_split = html.split('<div class="border border-outline-variant rounded-xl overflow-hidden">')
    new_html = cat_wrapper_split[0]

    for i in range(1, len(cat_wrapper_split)):
        part = cat_wrapper_split[i]
        
        # Count the number of items (labels) in this category
        count = part.count('<label class="flex items-start')
        
        if count > 0:
            # Replace the badge
            part = re.sub(r'(<span class="[^"]*bg-primary-fixed[^"]*">)\d+\s+[Ii]tems(</span>)', r'\g<1>' + str(count) + r' items\2', part)
            
        new_html += '<div class="border border-outline-variant rounded-xl overflow-hidden">' + part

    # Add accordion JS if not present
    if "Select all category headers in the static sample list" not in new_html:
        new_html = new_html.replace('</body>', accordion_js)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)

print("Done fixing static lists and badges!")
