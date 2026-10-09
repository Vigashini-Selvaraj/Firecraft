import re

with open('products.html', 'r', encoding='utf-8') as f:
    content = f.read()

def add_onclick(match):
    block = match.group(0)
    # Extract the id from the bulk order link
    m = re.search(r'href=\"product-detail\.html\?id=([^\"]+)\"', block)
    if m:
        id = m.group(1)
        # replace the <article class="product-card"> or <div class="bundle-card"> with onclick
        if '<article class="product-card">' in block:
            block = block.replace('<article class="product-card">', f'<article class="product-card" style="cursor: pointer;" onclick="window.location.href=\'product-detail.html?id={id}\'">')
        elif '<div class="bundle-card">' in block:
            block = block.replace('<div class="bundle-card">', f'<div class="bundle-card" style="cursor: pointer;" onclick="window.location.href=\'product-detail.html?id={id}\'">')
    return block

content = re.sub(r'<article class=\"product-card\">.*?</article>', add_onclick, content, flags=re.DOTALL)
content = re.sub(r'<div class=\"bundle-card\">.*?</a>\s*</div>', add_onclick, content, flags=re.DOTALL)

with open('products.html', 'w', encoding='utf-8') as f:
    f.write(content)
