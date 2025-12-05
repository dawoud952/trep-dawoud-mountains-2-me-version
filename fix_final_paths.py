import re

with open('mountains.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the full path with relative path
content = re.sub(r'"image": "C:\\\\Users\\\\Fouad\\\\Desktop\\\\end edits\\\\images\\\\dawoud\.jpg"', '"image": "./images/dawoud.jpg"', content)

with open('mountains.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed image paths to relative path in mountains.js")
