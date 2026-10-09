import re

with open('service-details.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add breadcrumbs to Hero
hero_old = '''<div class="container sd-hero-content">
            <h1 id="sd-title">Loading...</h1>'''
hero_new = '''<div class="container sd-hero-content">
            <div class="sd-breadcrumbs">
                <a href="index.html">Home</a> &gt; <a href="services.html">Services</a> &gt; <span id="sd-breadcrumb">Loading...</span>
            </div>
            <h1 id="sd-title">Loading...</h1>'''
html = html.replace(hero_old, hero_new)

# 2. Update Featured Sauces to be dynamic
sauces_old = '''<div class="sd-sauces-grid">
                <div class="sd-sauce-card">
                    <img src="assets/images/products/Classic-Hot-Sauce.png" alt="Classic Hot Sauce">
                    <h4>Classic Hot Sauce</h4>
                    <a href="product-detail.html">Shop Now <i class="fa-solid fa-arrow-right"></i></a>
                </div>
                <div class="sd-sauce-card">
                    <img src="assets/images/products/Mango-Habanero-Hot-Sauce.png" alt="Mango Habanero">
                    <h4>Mango Habanero</h4>
                    <a href="product-detail.html">Shop Now <i class="fa-solid fa-arrow-right"></i></a>
                </div>
                <div class="sd-sauce-card">
                    <img src="assets/images/products/Chipotle-BBQ-Sauce.png" alt="Chipotle BBQ">
                    <h4>Chipotle BBQ</h4>
                    <a href="product-detail.html">Shop Now <i class="fa-solid fa-arrow-right"></i></a>
                </div>
            </div>'''
sauces_new = '''<div class="sd-sauces-grid" id="sd-sauces">
                <!-- Injected via JS -->
            </div>'''
html = html.replace(sauces_old, sauces_new)

# 3. Update JS data
js_old = "benefits: [\n                { icon: 'fa-pepper-hot', title: 'Versatile Profiles', text: 'Perfect for marinades, dips, or finishing sauces.' },"
# Instead of complex regex for JS, I'll just rewrite the JS block entirely

with open('service-details.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated HTML")
