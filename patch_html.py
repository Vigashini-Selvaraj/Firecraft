import re

with open('recipes.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the stamp with mascot
mascot = '''                <div style="flex: 1; max-width: 400px; display: flex; justify-content: center; align-items: center;">
                    <img src="assets/images/chili_mascot_transparent.png" alt="Firecraft Mascot" style="width: 100%; max-width: 300px; animation: bounce 3s infinite ease-in-out;">
                </div>'''
html = re.sub(
    r'<div class="rc-hero-stamp">.*?</div>',
    mascot,
    html,
    flags=re.DOTALL
)

# Remove explicitly white color from h1
html = html.replace('line-height: .99; letter-spacing: -.035em; color: #f7f2ea;"', 'line-height: .99; letter-spacing: -.035em;"')

# Remove rc-eyebrow white color class if any (wait, it's in css)
# Remove rc-hero-overlay just to clean up HTML
html = html.replace('<div class="rc-hero-overlay"></div>', '')

with open('recipes.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Patched HTML for hero section.')
