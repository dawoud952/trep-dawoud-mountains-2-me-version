import re

# Read the mountains.js file
with open('mountains.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the full Windows path with relative path
# The path in the file is: "C:\Users\Fouad\Desktop\end edits\images\dawoud.jpg"
# We need to escape the backslashes for regex
content = re.sub(r'"image": "C:\\Users\\Fouad\\Desktop\\end edits\\images\\background\.jpg"', '"image": "./images/dawoud.jpg"', content)

# Write back to the file
with open('mountains.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed all image paths in mountains.js to use relative path './images/dawoud.jpg'")
