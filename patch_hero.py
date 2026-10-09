import re

with open('css/recipes.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the hero background image and gradient overlay, reduce min-height
css = re.sub(
    r'\.rc-hero\s*\{[^}]*\}',
    '.rc-hero {\n    padding-top: 50px;\n    display: flex;\n    align-items: center;\n    isolation: isolate;\n}',
    css
)

css = re.sub(
    r'\.rc-hero-overlay\s*\{[^}]*\}',
    '.rc-hero-overlay {\n    display: none;\n}',
    css
)

# Fix rc-hero-inner padding
css = re.sub(
    r'\.rc-hero-inner\s*\{[^}]*\}',
    '.rc-hero-inner {\n    display: flex;\n    align-items: center;\n    justify-content: space-between;\n    gap: 45px;\n    padding-top: 20px;\n    padding-bottom: 50px;\n}',
    css
)

with open('css/recipes.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Patched hero css.')
