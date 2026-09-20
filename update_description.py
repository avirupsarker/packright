import os

file_path = r'c:\Users\HI\packright\packing-list\japan\niseko-skiing\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_text = "7 days in Tokyo and Kyoto in spring, temples, street food, lots of walking"
new_text = "7 days in Niseko in January, skiing and snowboarding, staying near Hirafu, renting skis, and exploring the village"

if old_text in content:
    content = content.replace(old_text, new_text)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced text successfully!")
else:
    print("Old text not found in the file.")
