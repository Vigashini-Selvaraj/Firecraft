import re
import os

with open("service-details.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update JS data for 'hot-sauce-collections' to include images for benefits and steps
benefits_new = """benefits: [
          ["01", "Four distinctive flavors", "Explore classic heat, tropical sweetness, smoky richness, and garlic-chili character.", "assets/images/products/Classic-Hot-Sauce.png"],
          ["02", "Made for everyday food", "Bring a fresh flavor twist to snacks, lunches, dinners, and weekend favorites.", "assets/images/products/everyday-sauce.png"],
          ["03", "Find your own favorite", "Discover the sauce that matches your taste and the meals you love.", "assets/images/products/Fruit-Forward.png"],
          ["04", "More ways to experiment", "Try drizzling, dipping, mixing, and finishing dishes with your favorite sauce.", "assets/images/products/deep-and-smoky.png"]
        ]"""
html = re.sub(r'benefits:\s*\[[\s\S]*?\],\s*featuredTitle', benefits_new + ',\n        featuredTitle', html)

steps_new = """steps: [
          ["01", "Explore", "Get to know each sauce's distinctive flavor profile.", "assets/images/products/How to Choose the Right Hot Sauce.png"],
          ["02", "Pair", "Choose a sauce that complements the food you're making.", "assets/images/products/Spicy-Chicken-Tacos.png"],
          ["03", "Make it yours", "Experiment with your favorite meals and discover new combinations.", "assets/images/products/Fire-Wings.png"]
        ]"""
html = re.sub(r'steps:\s*\[[\s\S]*?\],\s*statementImage', steps_new + ',\n        statementImage', html)

products_data_new = """const products = {
      classic: {
        name: "Classic <em>Hot Sauce</em>",
        category: "CLASSIC & BOLD",
        description: "A chili-forward option for adding a familiar kick to your favorite meals.",
        image: "assets/images/products/Classic-Hot-Sauce.png"
      },
      mango: {
        name: "Mango <em>Habanero</em>",
        category: "FRUITY & FIERY",
        description: "A fruity flavor direction balanced with the distinctive heat of habanero.",
        image: "assets/images/products/Mango-Habanero-Hot-Sauce.png"
      },
      chipotle: {
        name: "Chipotle <em>Garlic</em>",
        category: "DEEP & SMOKY",
        description: "A smoky barbecue-style option for burgers, grilled foods, and more.",
        image: "assets/images/products/Chipotle-BBQ-Sauce.png"
      },
      garlic: {
        name: "Garlic <em>Chili Sauce</em>",
        category: "SAVORY & SPICY",
        description: "A garlic-forward chili option for noodles, savory snacks, and everyday dishes.",
        image: "assets/images/products/Garlic-Chili-Sauce.png"
      }
    };"""
html = re.sub(r'const products = \{[\s\S]*?\};\s*function renderBenefits', products_data_new + '\n\n    function renderBenefits', html)

render_benefits_new = """function renderBenefits(items) {
      document.getElementById("benefit-grid").innerHTML = items.map(item => `
        <article class="sd-benefit-card with-img">
          <div class="sd-benefit-img-wrap">
            <img src="${item[3] || 'assets/images/services/flavor-experiences.jpg'}" alt="${item[1]}" loading="lazy">
          </div>
          <div class="sd-benefit-content">
            <span class="sd-card-number">${item[0]}</span>
            <h3>${item[1].split(' ').map((w, i, arr) => i >= Math.ceil(arr.length/2) ? `<em>${w}</em>` : w).join(' ')}</h3>
            <p>${item[2]}</p>
          </div>
        </article>
      `).join("");
    }"""
html = re.sub(r'function renderBenefits.*?\}\s*function renderProducts', render_benefits_new + '\n\n    function renderProducts', html, flags=re.DOTALL)

render_steps_new = """function renderSteps(items) {
      document.getElementById("process-grid").innerHTML = items.map(item => `
        <article class="sd-process-card with-img">
          <div class="sd-process-img-wrap">
            <img src="${item[3] || 'assets/images/services/services-process.jpg'}" alt="${item[1]}" loading="lazy">
          </div>
          <div class="sd-process-content">
            <span class="sd-process-number">${item[0]}</span>
            <div class="sd-process-line"></div>
            <h3>${item[1].split(' ').map((w, i, arr) => i >= Math.ceil(arr.length/2) ? `<em>${w}</em>` : w).join(' ')}</h3>
            <p>${item[2]}</p>
          </div>
        </article>
      `).join("");
    }"""
html = re.sub(r'function renderSteps.*?\}\s*function renderFAQs', render_steps_new + '\n\n    function renderFAQs', html, flags=re.DOTALL)

# Let's fix processTitle inside HTML
html = html.replace('<h2 id="process-title">Your flavor journey, <em>made easy.</em></h2>', '<h2 id="process-title">Find your <em>kind of fire</em></h2>')

with open("service-details.html", "w", encoding="utf-8") as f:
    f.write(html)

# Update CSS to support these new images
with open("css/service-details.css", "r", encoding="utf-8") as f:
    css = f.read()

new_css = """
/* Added for redesign */
.sd-benefit-card.with-img {
    padding: 0;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    background: var(--sd-card);
    border: 1px solid var(--sd-border);
    border-radius: 8px;
    margin: 10px;
}
.sd-benefit-img-wrap {
    height: 200px;
    width: 100%;
    overflow: hidden;
}
.sd-benefit-img-wrap img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s;
}
.sd-benefit-card.with-img:hover .sd-benefit-img-wrap img {
    transform: scale(1.05);
}
.sd-benefit-content {
    padding: 20px;
}
.sd-benefit-content h3 {
    margin: 10px 0;
    font-size: 1.5rem;
}
.sd-benefit-content h3 em, .sd-process-content h3 em {
    color: var(--sd-red);
    font-style: normal;
}
.sd-benefit-grid {
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)) !important;
    gap: 20px;
    border: none !important;
}
.sd-benefit-card {
    border: none !important;
}

.sd-process-card.with-img {
    display: flex;
    flex-direction: column;
    background: var(--sd-card);
    border-radius: 8px;
    overflow: hidden;
    padding: 0;
    border: 1px solid var(--sd-border);
}
.sd-process-img-wrap {
    height: 220px;
    width: 100%;
    overflow: hidden;
}
.sd-process-img-wrap img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s;
}
.sd-process-card.with-img:hover .sd-process-img-wrap img {
    transform: scale(1.05);
}
.sd-process-content {
    padding: 25px;
}
.sd-process-grid {
    gap: 30px !important;
}

.sd-product-info h3 em {
    color: var(--sd-red);
    font-style: normal;
}
"""

if "/* Added for redesign */" not in css:
    with open("css/service-details.css", "a", encoding="utf-8") as f:
        f.write(new_css)
