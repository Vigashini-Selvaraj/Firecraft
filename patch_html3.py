import re

with open('recipes.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change the paragraph
html = html.replace('''                    <p>
                        Your favorite meals, reimagined with our bold,
                        flavor-packed sauces. From smoky and sweet to
                        unapologetically fiery, find your next favorite
                        dish — and the Firecraft sauce that makes it.
                    </p>''', '''                    <p style="max-width: 500px;">
                        From smoky and sweet to unapologetically fiery, find your next favorite dish — and the Firecraft sauce that makes it.
                    </p>''')

# Change the mascot size
html = html.replace('max-width: 400px;', 'max-width: 600px;')
html = html.replace('max-width: 450px;', 'max-width: 550px; transform: scale(1.15); transform-origin: center;')

# Remove rc-hero-bottom
html = re.sub(r'<div class="rc-hero-bottom">.*?</div>', '', html, flags=re.DOTALL)

with open('recipes.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated recipes.html')
