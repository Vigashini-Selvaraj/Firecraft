import re

with open('products.html', 'r', encoding='utf-8') as f:
    content = f.read()

mappings = {
    'The Everyday Trio': 'daily-blaze',
    'Heat Seeker Set': 'ghost-pepper',
    'Sweet \+ Smoky': 'mango-habanero'
}

def replace_href(match):
    block = match.group(0)
    for title, id in mappings.items():
        if f"<h3>{title}</h3>" in block or (title == 'Sweet \+ Smoky' and "Sweet + Smoky" in block):
            block = re.sub(r'href=\"product-detail\.html[^"]*\"', f'href="product-detail.html?id={id}"', block)
            return block
    return block

content = re.sub(r'<div class=\"bundle-card\">.*?</a>\s*</div>', replace_href, content, flags=re.DOTALL)

with open('products.html', 'w', encoding='utf-8') as f:
    f.write(content)
