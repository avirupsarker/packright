import os
import glob
import re

files = glob.glob(r'c:\Users\HI\packright\**\*.html', recursive=True)

meta_tag = '    <meta name="p:domain_verify" content="e865c335835af72535d69f504ed94085"/>\n'

count = 0
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'name="p:domain_verify"' not in content:
        # find the closing </head> tag and insert before it
        content = re.sub(r'(</head>)', meta_tag + r'\1', content, flags=re.IGNORECASE)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Added meta tag to {file}")

print(f"Added to {count} files total.")
