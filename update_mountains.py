import re

with open('mountains.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the image path with the full path
content = re.sub(r'"image": "[^"]*"', '"image": "C:/Users/Fouad/Desktop/end edits/images/dawoud.jpg"', content)

with open('mountains.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated image paths in mountains.js")
