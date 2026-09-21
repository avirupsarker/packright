import os

files = [
    r'c:\Users\HI\packright\index.html',
    r'c:\Users\HI\packright\packing-list\japan\index.html',
    r'c:\Users\HI\packright\packing-list\europe\index.html',
    r'c:\Users\HI\packright\packing-list\japan\niseko-skiing\index.html',
    r'c:\Users\HI\packright\packing-list\japan\mount-fuji-climbing\index.html'
]

notice_html = """
            <div id="unrelatedDestinationNotice" class="hidden m-4 md:mx-8 md:mt-8 p-4 bg-[#F5F0EB] text-[#D4735E] rounded-xl text-sm border border-[#D4735E]/30">
                This page is designed for Niseko trips. We used your details to adjust the checklist where possible, while keeping the destination-specific Niseko gear section visible.
            </div>
"""

niseko_html = """
                <!-- Permanent Niseko Module -->
                <div id="nisekoPermanentModule" class="hidden mx-4 md:mx-8 mb-8 p-6 bg-[#F5F0EB] rounded-xl border border-outline-variant">
                    <h3 class="font-headline-md text-on-surface mb-2">Niseko gear worth considering</h3>
                    <p class="font-body-md text-on-surface-variant mb-6 text-sm">These optional gear categories are especially relevant to Niseko’s snow, visibility, and village conditions. Skip anything you already own or plan to rent.</p>
                    <div id="nisekoModuleItems" class="flex flex-col gap-4">
                        <!-- JS will populate -->
                    </div>
                </div>
"""

for filepath in files:
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}, does not exist.")
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add nisekoLogic.js
    if 'nisekoLogic.js' not in content:
        content = content.replace('<script src="/app.js" defer></script>', '<script src="/nisekoLogic.js"></script>\n    <script src="/app.js" defer></script>')

    # Add unrelatedDestinationNotice
    if 'id="unrelatedDestinationNotice"' not in content:
        content = content.replace('<div id="packingListContainer"', notice_html + '            <div id="packingListContainer"')

    # Add nisekoPermanentModule
    if 'id="nisekoPermanentModule"' not in content:
        content = content.replace('<!-- Dynamically injected category cards -->\n            </div>', '<!-- Dynamically injected category cards -->\n            </div>\n' + niseko_html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("HTML injected.")
