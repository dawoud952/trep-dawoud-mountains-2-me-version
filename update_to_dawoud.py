import re

# Read the mountains.js file
with open('mountains.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the image path from background.jpg to dawoud.jpg
content = re.sub(r'"image": "\./images/background\.jpg"', '"image": "./images/dawoud.jpg"', content)

# Write back to the file
with open('mountains.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated all image paths in mountains.js to use './images/dawoud.jpg'")
