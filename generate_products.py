import re

def generate():
    # Read the header and footer from products.html
    with open('products.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Extract everything before <main> and after </main>
    head_match = re.search(r'(.*?<main>)', html, re.DOTALL)
    foot_match = re.search(r'(</main>.*)', html, re.DOTALL)
    
    header = head_match.group(1)
    footer = foot_match.group(1)
    
    # Generate the massive new main content
    main_content = """
<!-- =====================================================
     01. PRODUCT HERO
===================================================== -->
<section class="products-hero text-center">
    <div class="hero-bg"></div>
    <div class="container hero-content-wrapper">
        <span class="section-label">THE COLLECTION</span>
        <h1>Find Your<br><em>Perfect Heat.</em></h1>
        <p>Premium, small-batch hot sauces meticulously crafted for those who demand uncompromising flavor alongside their fire.</p>
        <div class="hero-buttons">
            <a href="#collection" class="btn btn-primary">Explore Sauces <i class="fa-solid fa-arrow-right"></i></a>
            <a href="#bundles" class="btn btn-outline">Build Your Collection <i class="fa-solid fa-box"></i></a>
        </div>
    </div>
</section>

<!-- =====================================================
     02. OUR SAUCE COLLECTION
===================================================== -->
<section id="collection" class="collection-section section">
    <div class="container">
        <div class="section-heading text-center">
            <span class="section-label">SIGNATURE SAUCES</span>
            <h2>Our Sauce <em>Collection.</em></h2>
        </div>
        
        <div class="collection-grid">
            <!-- Classic -->
            <article class="product-card">
                <div class="product-image"><img src="assets/images/products/Classic-Hot-Sauce.png" alt="Classic Hot Sauce"></div>
                <div class="product-info">
                    <div class="heat-bar"><span class="heat-level mild">MILD</span></div>
                    <h3>Classic Hot Sauce</h3>
                    <p class="flavor-profile"><strong>Flavor:</strong> Tangy, Bright, Peppery</p>
                    <p class="best-with"><strong>Best With:</strong> Pizza, Eggs, Tacos</p>
                    <div class="product-actions">
                        <span class="price">$12.00</span>
                        <a href="#" class="btn btn-outline">View Product</a>
                    </div>
                </div>
            </article>

            <!-- Mango Habanero -->
            <article class="product-card">
                <div class="product-image"><img src="assets/images/products/Mango-Habanero-Hot-Sauce.png" alt="Mango Habanero Hot Sauce"></div>
                <div class="product-info">
                    <div class="heat-bar"><span class="heat-level hot">HOT</span></div>
                    <h3>Mango Habanero</h3>
                    <p class="flavor-profile"><strong>Flavor:</strong> Sweet, Fruity, Intense Burn</p>
                    <p class="best-with"><strong>Best With:</strong> Grilled Chicken, Fish Tacos</p>
                    <div class="product-actions">
                        <span class="price">$14.00</span>
                        <a href="#" class="btn btn-outline">View Product</a>
                    </div>
                </div>
            </article>

            <!-- Chipotle BBQ -->
            <article class="product-card">
                <div class="product-image"><img src="assets/images/products/Chipotle-BBQ-Sauce.png" alt="Chipotle BBQ Sauce"></div>
                <div class="product-info">
                    <div class="heat-bar"><span class="heat-level medium">MEDIUM</span></div>
                    <h3>Chipotle BBQ</h3>
                    <p class="flavor-profile"><strong>Flavor:</strong> Smoky, Earthy, Sweet Molasses</p>
                    <p class="best-with"><strong>Best With:</strong> Burgers, Ribs, Pulled Pork</p>
                    <div class="product-actions">
                        <span class="price">$15.00</span>
                        <a href="#" class="btn btn-outline">View Product</a>
                    </div>
                </div>
            </article>

            <!-- Garlic Chili -->
            <article class="product-card">
                <div class="product-image"><img src="assets/images/products/Garlic-Chili-Sauce.png" alt="Garlic Chili Sauce"></div>
                <div class="product-info">
                    <div class="heat-bar"><span class="heat-level medium">MEDIUM</span></div>
                    <h3>Garlic Chili Sauce</h3>
                    <p class="flavor-profile"><strong>Flavor:</strong> Deeply Savory, Garlicky, Zesty</p>
                    <p class="best-with"><strong>Best With:</strong> Noodles, Stir-fry, Dumplings</p>
                    <div class="product-actions">
                        <span class="price">$14.00</span>
                        <a href="#" class="btn btn-outline">View Product</a>
                    </div>
                </div>
            </article>
        </div>
    </div>
</section>

<!-- =====================================================
     03. CHOOSE YOUR HEAT
===================================================== -->
<section class="heat-scale-section section section-dark" style="background: var(--color-black);">
    <div class="container">
        <div class="section-heading text-center" style="margin-bottom: 60px;">
            <span class="section-label">THE FIRE SCALE</span>
            <h2>Choose Your <em>Heat.</em></h2>
        </div>
        
        <div class="heat-scale-grid">
            <div class="heat-step mild">
                <div class="heat-icon"><i class="fa-solid fa-pepper-hot"></i></div>
                <h3>Mild</h3>
                <p>A gentle, warming tingle. Perfect for enhancing flavor without breaking a sweat.</p>
            </div>
            <div class="heat-step medium">
                <div class="heat-icon"><i class="fa-solid fa-pepper-hot"></i><i class="fa-solid fa-pepper-hot"></i></div>
                <h3>Medium</h3>
                <p>A satisfying, noticeable kick. The sweet spot for everyday heat seekers.</p>
            </div>
            <div class="heat-step hot">
                <div class="heat-icon"><i class="fa-solid fa-pepper-hot"></i><i class="fa-solid fa-pepper-hot"></i><i class="fa-solid fa-pepper-hot"></i></div>
                <h3>Hot</h3>
                <p>An aggressive, lingering burn. For those who want their endorphins racing.</p>
            </div>
            <div class="heat-step extra-hot">
                <div class="heat-icon"><i class="fa-solid fa-fire-flame-curved"></i></div>
                <h3>Extra Hot</h3>
                <p>Pure, unapologetic fire. A searing heat that challenges even the boldest palates.</p>
            </div>
        </div>
    </div>
</section>

<!-- =====================================================
     04. FLAVOR PROFILES & PAIRINGS
===================================================== -->
<section class="flavor-pairing-section section">
    <div class="container">
        <div class="fp-layout">
            <div class="fp-content">
                <span class="section-label">TASTE PROFILES</span>
                <h2>Flavor, Not Just <em>Fire.</em></h2>
                <p>We build our recipes around distinct taste profiles so you can perfectly match your sauce to your meal.</p>
                
                <div class="tags-grid">
                    <span class="flavor-tag">Tangy</span>
                    <span class="flavor-tag">Smoky</span>
                    <span class="flavor-tag">Sweet</span>
                    <span class="flavor-tag">Garlicky</span>
                    <span class="flavor-tag">Fruity</span>
                    <span class="flavor-tag">Bold</span>
                </div>
            </div>
            
            <div class="fp-pairings">
                <div class="pairing-item">
                    <i class="fa-solid fa-pizza-slice"></i>
                    <div>
                        <h4>Pizza</h4>
                        <p>Best with: <strong>Classic Hot Sauce</strong></p>
                    </div>
                </div>
                <div class="pairing-item">
                    <i class="fa-solid fa-drumstick-bite"></i>
                    <div>
                        <h4>Grilled Chicken</h4>
                        <p>Best with: <strong>Mango Habanero</strong></p>
                    </div>
                </div>
                <div class="pairing-item">
                    <i class="fa-solid fa-burger"></i>
                    <div>
                        <h4>Burgers</h4>
                        <p>Best with: <strong>Chipotle BBQ</strong></p>
                    </div>
                </div>
                <div class="pairing-item">
                    <i class="fa-solid fa-bowl-rice"></i>
                    <div>
                        <h4>Noodles</h4>
                        <p>Best with: <strong>Garlic Chili</strong></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- =====================================================
     05. FIND YOUR SAUCE / PREFERENCE SELECTOR
===================================================== -->
<section class="find-sauce-section section" style="background: var(--color-dark-soft);">
    <div class="container text-center">
        <div class="find-sauce-box">
            <h2>Find Your <em>Match.</em></h2>
            <p>Not sure where to start? Let us recommend the perfect bottle.</p>
            
            <div class="selector-form">
                <div class="selector-group">
                    <label>How much heat?</label>
                    <select><option>Mild & Flavorful</option><option>Medium Kick</option><option>Melt My Face</option></select>
                </div>
                <div class="selector-group">
                    <label>Flavor Vibe?</label>
                    <select><option>Sweet & Fruity</option><option>Deep & Smoky</option><option>Zesty & Garlicky</option></select>
                </div>
                <div class="selector-group">
                    <label>Eating with?</label>
                    <select><option>Tacos / Mexican</option><option>Pizza / Italian</option><option>BBQ / Meats</option></select>
                </div>
                <button class="btn btn-primary" style="margin-top:20px;">Find My Sauce</button>
            </div>
        </div>
    </div>
</section>

<!-- =====================================================
     06. BUNDLES & BEST SELLERS
===================================================== -->
<section id="bundles" class="bundles-section section">
    <div class="container">
        <div class="section-heading text-center">
            <span class="section-label">COMPLETE YOUR COLLECTION</span>
            <h2>Curated <em>Bundles.</em></h2>
        </div>
        
        <div class="bundles-grid">
            <div class="bundle-card">
                <div class="bundle-content">
                    <h3>The Everyday Trio</h3>
                    <p>Classic, Garlic Chili, and Chipotle BBQ. The essentials for any pantry.</p>
                    <span class="price">$38.00</span>
                    <a href="#" class="btn btn-outline">Add to Collection</a>
                </div>
            </div>
            <div class="bundle-card">
                <div class="bundle-content">
                    <h3>Heat Seeker Set</h3>
                    <p>Mango Habanero and our secret Ghost Pepper reserve. Not for the faint of heart.</p>
                    <span class="price">$32.00</span>
                    <a href="#" class="btn btn-outline">Add to Collection</a>
                </div>
            </div>
            <div class="bundle-card">
                <div class="bundle-content">
                    <h3>Sweet + Smoky</h3>
                    <p>Chipotle BBQ and Mango Habanero. The ultimate flavor contrast.</p>
                    <span class="price">$28.00</span>
                    <a href="#" class="btn btn-outline">Add to Collection</a>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- =====================================================
     07. FINAL CTA
===================================================== -->
<section class="final-cta section text-center" style="background: var(--color-dark-soft); padding: 120px 0;">
    <div class="container">
        <h2 style="font-family: var(--font-display); font-size: clamp(48px, 6vw, 72px); color: var(--color-text-light);">Ready to Find<br>Your <em>Heat?</em></h2>
        <p style="color: var(--color-muted); margin: 20px auto 40px; max-width: 500px; font-size: 18px;">Explore every flavor in the Firecraft collection and elevate your everyday meals.</p>
        <a href="#collection" class="btn btn-primary btn-large">Explore All Sauces</a>
    </div>
</section>

"""
    
    with open('products.html', 'w', encoding='utf-8') as f:
        f.write(header + main_content + footer)

if __name__ == "__main__":
    generate()
