import re

html_path = r'c:\Users\vigas\Desktop\firecraft\home2.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacement = '''        <div class="interactive-pairing">
            <div class="pairing-sidebar">
                <button class="pairing-tab active" data-pairing="chicken">
                    <i class="fa-solid fa-drumstick-bite"></i> Chicken
                </button>
                <button class="pairing-tab" data-pairing="burgers">
                    <i class="fa-solid fa-burger"></i> Burgers
                </button>
                <button class="pairing-tab" data-pairing="tacos">
                    <i class="fa-solid fa-pepper-hot"></i> Tacos
                </button>
                <button class="pairing-tab" data-pairing="pizza">
                    <i class="fa-solid fa-pizza-slice"></i> Pizza
                </button>
            </div>

            <div class="pairing-display">
                <div class="pairing-pane active" id="pane-chicken">
                    <div class="pane-image"><img src="assets/images/products/Fire-Wings.png" alt="Chicken pairing"></div>
                    <div class="pane-info">
                        <span>FLAVOR DIRECTION</span>
                        <h3>Smoky · Tangy</h3>
                        <span>WHY IT WORKS</span>
                        <p>Adds depth without overpowering the meat. The perfect combination of tanginess and deep smoke complements grilled and fried chicken beautifully.</p>
                    </div>
                </div>

                <div class="pairing-pane" id="pane-burgers">
                    <div class="pane-image"><img src="assets/images/products/Chipotle-BBQ-Sauce.png" alt="Burger pairing"></div>
                    <div class="pane-info">
                        <span>FLAVOR DIRECTION</span>
                        <h3>Garlic · Smoky</h3>
                        <span>WHY IT WORKS</span>
                        <p>Cuts through rich, savory flavors. A bold, garlicky profile elevates the heavy umami flavors of a good burger.</p>
                    </div>
                </div>

                <div class="pairing-pane" id="pane-tacos">
                    <div class="pane-image"><img src="assets/images/products/Spicy-Chicken-Tacos.png" alt="Tacos pairing"></div>
                    <div class="pane-info">
                        <span>FLAVOR DIRECTION</span>
                        <h3>Fruity · Tangy</h3>
                        <span>WHY IT WORKS</span>
                        <p>Provides a bright, acidic contrast to fatty meats and heavy cheeses, while adding the perfect kick of heat.</p>
                    </div>
                </div>
                
                <div class="pairing-pane" id="pane-pizza">
                    <div class="pane-image"><img src="assets/images/products/Hot-Honey-Pizza.png" alt="Pizza pairing"></div>
                    <div class="pane-info">
                        <span>FLAVOR DIRECTION</span>
                        <h3>Sweet · Heat</h3>
                        <span>WHY IT WORKS</span>
                        <p>Sweetness cuts through the saltiness of cured meats like pepperoni, while the chili adds a lingering warmth.</p>
                    </div>
                </div>
            </div>
        </div>
'''

# Find the pairing table block
pattern = re.compile(r'<div class="pairing-table">.*?(?=</section>)', re.DOTALL)

if pattern.search(content):
    new_content = pattern.sub(replacement + '\n    </div>\n', content)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("HTML UPDATED")
else:
    print("PATTERN NOT FOUND")

# Update CSS
css_path = r'c:\Users\vigas\Desktop\firecraft\css\home2.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

css_replacement = '''/* =====================================================
   INTERACTIVE PAIRING
===================================================== */
.pairing-section { background: var(--color-dark); }
.interactive-pairing { display: grid; grid-template-columns: 250px 1fr; gap: 50px; align-items: start; border-top: 1px solid var(--color-border-dark); padding-top: 40px; }
.pairing-sidebar { display: flex; flex-direction: column; gap: 10px; }
.pairing-tab { background: transparent; border: 1px solid transparent; color: var(--color-muted); padding: 18px 25px; text-align: left; font-size: 15px; font-weight: 700; cursor: pointer; transition: var(--transition); display: flex; align-items: center; gap: 15px; font-family: var(--font-body); border-radius: 4px; }
.pairing-tab i { font-size: 18px; width: 25px; text-align: center; }
.pairing-tab:hover { background: var(--color-dark-soft); color: var(--color-white); }
.pairing-tab.active { background: var(--color-dark-soft); color: var(--color-red); border-color: var(--color-border-dark); }

.pairing-pane { display: none; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center; animation: fadeIn 0.4s ease forwards; }
.pairing-pane.active { display: grid; }
.pane-image { border-radius: 4px; overflow: hidden; height: 350px; }
.pane-image img { width: 100%; height: 100%; object-fit: cover; }
.pane-info span { display: block; color: var(--color-red); font-size: 10px; font-weight: 800; letter-spacing: 0.15em; margin-bottom: 10px; font-family: var(--font-body); }
.pane-info h3 { font-family: var(--font-display); font-size: 38px; color: var(--color-white); margin: 0 0 35px 0; line-height: 1.1; }
.pane-info p { color: var(--color-muted); font-size: 15px; line-height: 1.6; }

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
@media (max-width: 992px) {
    .interactive-pairing { grid-template-columns: 1fr; }
    .pairing-sidebar { flex-direction: row; flex-wrap: wrap; }
    .pairing-tab { flex: 1; justify-content: center; min-width: 150px; }
    .pairing-pane { grid-template-columns: 1fr; }
}

'''

css_pattern = re.compile(r'/\* =====================================================\n   PAIRING\n===================================================== \*/.*?/\* =====================================================\n   STORY', re.DOTALL)

if css_pattern.search(css_content):
    new_css = css_pattern.sub(css_replacement + '/* =====================================================\n   STORY', css_content)
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(new_css)
    print("CSS UPDATED")
else:
    print("CSS PATTERN NOT FOUND")
