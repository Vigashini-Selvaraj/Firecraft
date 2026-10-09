import re

with open('css/recipes.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(r'color:\s*var\(--color-ivory\);\s*/\*\s*eyebrow\s*\*/', 'color: var(--text-light-section);', css) # just in case
css = re.sub(r'\.rc-eyebrow\s*\{([^}]*)color:\s*var\(--color-ivory\);', r'.rc-eyebrow {\1color: var(--text-light-section);', css)
css = re.sub(r'\.rc-hero-note\s*\{([^}]*)color:\s*#b8afa4;', r'.rc-hero-note {\1color: var(--color-muted);', css)

with open('css/recipes.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Patched hero text colors.')
