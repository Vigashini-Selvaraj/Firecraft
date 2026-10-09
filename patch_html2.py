import re

with open('recipes.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make mascot bigger and move up by adding margin-bottom or increasing max-width
html = html.replace('max-width: 300px; animation: bounce 3s infinite ease-in-out;', 'max-width: 450px; animation: bounce 3s infinite ease-in-out;')

# Remove rc-hero-note
html = re.sub(r'<div class="rc-hero-note">.*?</div>', '', html, flags=re.DOTALL)

with open('recipes.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated recipes.html mascot size and removed note.')
