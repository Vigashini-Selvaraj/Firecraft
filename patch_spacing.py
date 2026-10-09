import re

with open('css/recipes.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix spacing in hero
css = css.replace('.rc-hero {\n    padding-top: 50px;', '.rc-hero {\n    padding-top: 0px;')
css = css.replace('padding-top: 20px;\n    padding-bottom: 50px;', 'padding-top: 0px;\n    padding-bottom: 20px;')

# Fix the failed color replacements from earlier
css = re.sub(r'\.rc-recipe-body\s*>\s*p\s*\{[^}]*color:\s*#6d6258;', lambda m: m.group(0).replace('#6d6258', 'var(--color-muted)'), css)
css = re.sub(r'\.rc-recipe-link\s*\{[^}]*color:\s*var\(--color-text-dark\);', lambda m: m.group(0).replace('var(--color-text-dark)', 'var(--text-light-section)'), css)
css = re.sub(r'\.rc-inline-link\s*\{[^}]*color:\s*var\(--color-text-dark\);', lambda m: m.group(0).replace('var(--color-text-dark)', 'var(--text-light-section)'), css)

with open('css/recipes.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated spacing and remaining colors.')
