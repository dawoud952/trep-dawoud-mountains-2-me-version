import re

# Read the file
with open('mountains.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all image paths
content = re.sub(r'"image": "\./images/background\.jpg"', r'"image": "./images/dawoud.jpg"', content)

# Write back
with open('mountains.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed all image paths in mountains.js")
