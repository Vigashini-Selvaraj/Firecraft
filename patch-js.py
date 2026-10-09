import re

with open('js/product-detail.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Update Breadcrumb name
if "document.title = product.name + ' - Firecraft';" in js_content and "pd-breadcrumb-name" not in js_content:
    js_content = js_content.replace(
        "document.title = product.name + ' - Firecraft';",
        "document.title = product.name + ' - Firecraft';\n    const bName = document.getElementById('pd-breadcrumb-name'); if(bName) bName.textContent = product.name;"
    )

# Update heat meter bars selector
js_content = js_content.replace(".querySelectorAll('.heat-meter-bar')", ".querySelectorAll('.heat-meter .bar')")

# Update styling for injected pairing card to match new design
js_content = js_content.replace(
    'div.className = \'pairing-card\';',
    'div.className = \'pairing-card\';'
)

with open('js/product-detail.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
