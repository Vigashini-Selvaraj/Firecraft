import re

with open('recipe-details.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix image extensions for recipe images
html = re.sub(r'(assets/images/recipes/[^"]+\.jpg)"', r'\1.png"', html)

with open('recipe-details.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Fixed image paths.')
