import os
import glob
import re

files = glob.glob(r'c:\Users\HI\packright\**\*.html', recursive=True)

meta_tag = '<meta name="p:domain_verify" content="e865c335835af72535d69f504ed94085"/>'

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove old tag
    content = content.replace('    <meta name="p:domain_verify" content="e865c335835af72535d69f504ed94085"/>\n', '')
    content = content.replace('<meta name="p:domain_verify" content="e865c335835af72535d69f504ed94085"/>', '')
    
    # Add right after <head>
    content = re.sub(r'(<head>)', r'\1\n' + meta_tag, content, flags=re.IGNORECASE)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file}")
