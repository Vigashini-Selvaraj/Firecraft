import re

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Firecraft | Product Detail</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">

    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/navbar.css">
    <link rel="stylesheet" href="css/footer.css">
    <link rel="stylesheet" href="css/product-detail.css">
</head>

<body>

<!-- NAVBAR -->
<header class="navbar">
    <div class="container navbar-container">
        <a href="index.html" class="logo">
            <img src="assets/images/firecraft_logo.png" alt="Firecraft Hot Sauces">
            <span class="logo-text">Firecraft</span>
        </a>
        <nav class="nav-menu">
            <a href="index.html">Home</a>
            <a href="home2.html">Home 2</a>
            <a href="about.html">About Us</a>
            <a href="products.html" class="active">Products</a>
            <a href="recipes.html">Recipes</a>
            <a href="services.html">Service</a>
            <a href="blog.html">Blog</a>
            <a href="contact.html">Contact</a>
        </nav>
        <div class="nav-actions">
            <button class="mobile-menu-btn" aria-label="Open Menu"><i class="fa-solid fa-bars"></i></button>
            <button class="nav-icon theme-toggle-btn" aria-label="Toggle Theme"><i class="fa-solid fa-moon"></i></button>
            <button class="nav-icon dir-toggle-btn" aria-label="Toggle Direction">LTR</button>
            <div class="profile-dropdown-container desktop-only">
                <button class="nav-icon profile-btn" aria-label="Profile"><i class="fa-solid fa-user"></i></button>
                <div class="profile-dropdown">
                    <a href="#">Login</a>
                    <a href="#">Register</a>
                </div>
            </div>
        </div>
    </div>
</header>

<main>
    <!-- SPLIT SCREEN HERO & PRODUCT INFO -->
    <section class="pd-hero-split">
        <div class="pd-hero-sticky-image">
            <div class="image-wrapper">
                <img id="pd-image" src="" alt="Product Image">
                <div class="glass-badge" id="pd-heat-badge">
                    <i class="fa-solid fa-fire"></i> <span id="pd-heat">MILD</span>
                </div>
            </div>
        </div>
        
        <div class="pd-hero-scroll-content">
            <!-- Breadcrumbs -->
            <div class="breadcrumbs">
                <a href="products.html">All Products</a> / <span id="pd-breadcrumb-name">Loading...</span>
            </div>

            <!-- Header Info -->
            <h1 class="pd-title" id="pd-name">Loading...</h1>
            <div class="pd-rating-block">
                <div class="stars">
                    <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star-half-stroke"></i>
                </div>
                <span id="pd-rating" class="rating-num">4.8</span> 
                <span id="pd-reviews" class="review-count">(0 Reviews)</span>
            </div>
            
            <p class="pd-short-desc" id="pd-desc">Loading description...</p>
            
            <div class="pd-tags-container" id="pd-tags"></div>

            <div class="pd-price-row">
                <div class="pd-price" id="pd-price">$0</div>
            </div>
            
            <!-- Actions -->
            <div class="pd-actions-block">
                <div class="qty-control">
                    <button id="qty-minus"><i class="fa-solid fa-minus"></i></button>
                    <input type="text" id="qty-input" value="1" readonly>
                    <button id="qty-plus"><i class="fa-solid fa-plus"></i></button>
                </div>
                <button class="btn btn-primary btn-add-cart">
                    <span>Add to Cart</span> <i class="fa-solid fa-cart-shopping"></i>
                </button>
                <button class="btn btn-favorite"><i class="fa-regular fa-heart"></i></button>
            </div>
            
            <div class="pd-shipping-perk">
                <i class="fa-solid fa-truck-fast"></i> Free wholesale shipping on orders over $500.
            </div>

            <!-- FLAVOR & HEAT (Redesigned inside scroll area) -->
            <div class="pd-details-grid">
                <div class="detail-box flavor-box">
                    <h3>Taste, Decoded.</h3>
                    <p id="pd-flavor-desc">Loading...</p>
                    <ul id="pd-flavor-notes" class="custom-list"></ul>
                </div>
                
                <div class="detail-box heat-box">
                    <h3>The Burn.</h3>
                    <div class="heat-stat">
                        <span>Primary Pepper</span>
                        <strong id="pd-pepper">Loading...</strong>
                    </div>
                    <div class="heat-stat">
                        <span>Scoville Rating</span>
                        <strong id="pd-scoville">Loading...</strong>
                    </div>
                    <div class="heat-stat">
                        <span>Intensity Meter</span>
                        <div class="heat-meter" id="pd-heat-meter">
                            <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- WHAT'S INSIDE (Redesigned as Tabs) -->
            <div class="pd-tabs-section">
                <h3>What's Inside</h3>
                <div class="tabs-header">
                    <button class="tab-btn active" data-target="tab-ingredients">Ingredients</button>
                    <button class="tab-btn" data-target="tab-texture">Texture</button>
                    <button class="tab-btn" data-target="tab-shelf">Storage</button>
                    <button class="tab-btn" data-target="tab-allergens">Allergens</button>
                </div>
                <div class="tabs-content">
                    <div class="tab-pane active" id="tab-ingredients"><p id="pd-ingredients"></p></div>
                    <div class="tab-pane" id="tab-texture"><p id="pd-texture"></p></div>
                    <div class="tab-pane" id="tab-shelf"><p id="pd-shelf"></p></div>
                    <div class="tab-pane" id="tab-allergens"><p id="pd-allergens"></p></div>
                </div>
            </div>

        </div>
    </section>

    <!-- PAIRINGS SECTION (3 IMAGES) -->
    <section class="pd-pairings-section">
        <div class="container text-center">
            <span class="section-label">CULINARY SYNERGY</span>
            <h2>Best <em>Pairings.</em></h2>
            <p class="section-subtitle">Elevate your meals with the perfect flavor match.</p>
            
            <div class="pairings-grid-3" id="pd-pairings">
                <!-- JS WILL INJECT 3 PAIRINGS HERE -->
            </div>
        </div>
    </section>

    <!-- HOW TO USE IT / TUTORIAL -->
    <section class="pd-tutorial-section">
        <div class="container">
            <div class="tutorial-grid">
                <div class="tutorial-text">
                    <span class="section-label">MASTER THE HEAT</span>
                    <h2>How to <em>Use It.</em></h2>
                    <p class="tutorial-desc">Don't just blind your tastebuds. Use our sauce to enhance the natural flavors of your dish.</p>
                    
                    <div class="tutorial-steps">
                        <div class="step">
                            <div class="step-num">01</div>
                            <div class="step-info">
                                <h4>Start Small</h4>
                                <p>Begin with a few drops to test your tolerance before committing.</p>
                            </div>
                        </div>
                        <div class="step">
                            <div class="step-num">02</div>
                            <div class="step-info">
                                <h4>Taste First</h4>
                                <p>Let the flavor profile coat your tongue before the heat kicks in.</p>
                            </div>
                        </div>
                        <div class="step">
                            <div class="step-num">03</div>
                            <div class="step-info">
                                <h4>Apply Generously</h4>
                                <p>Drizzle, dip, or mix into marinades for maximum impact.</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="tutorial-image">
                    <img src="assets/images/about_story.jpg" alt="Using Firecraft Sauce">
                </div>
            </div>
        </div>
    </section>

    <!-- TESTIMONIALS (Redesigned) -->
    <section class="pd-reviews-section">
        <div class="container text-center">
            <span class="section-label">COMMUNITY VERDICT</span>
            <h2>What They're <em>Saying.</em></h2>
            
            <div class="reviews-slider">
                <div class="review-card">
                    <div class="review-stars">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>
                    <h3>Absolute perfection!</h3>
                    <p>"This is exactly what I was looking for. The flavor is incredible and the heat level is spot on. I'll be buying a case next time!"</p>
                    <div class="reviewer">
                        <div class="avatar">M</div>
                        <div class="reviewer-info">
                            <strong>Marcus T.</strong>
                            <span>Verified Buyer</span>
                        </div>
                    </div>
                </div>
                <div class="review-card">
                    <div class="review-stars">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star-half-stroke"></i>
                    </div>
                    <h3>New staple in my kitchen.</h3>
                    <p>"I put this on my eggs every single morning. It's not just hot, it actually makes the food taste better. Highly recommended."</p>
                    <div class="reviewer">
                        <div class="avatar">S</div>
                        <div class="reviewer-info">
                            <strong>Sarah J.</strong>
                            <span>Verified Buyer</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- FAQs (Redesigned) -->
    <section class="pd-faq-section">
        <div class="container pd-faq-grid">
            <div class="faq-intro">
                <span class="section-label">CURIOUS?</span>
                <h2>Frequently <em>Asked.</em></h2>
                <p>Everything you need to know about our ingredients, heat levels, and shipping.</p>
            </div>
            <div class="faq-accordion custom-accordion">
                <div class="faq-item">
                    <button class="faq-header">How spicy is this sauce? <i class="fa-solid fa-chevron-down"></i></button>
                    <div class="faq-content"><p>Please refer to our Heat Breakdown section. We use the Scoville scale to provide an accurate estimate of the burn, paired with a visual intensity meter.</p></div>
                </div>
                <div class="faq-item">
                    <button class="faq-header">How should I store the bottle? <i class="fa-solid fa-chevron-down"></i></button>
                    <div class="faq-content"><p>Store in a cool, dry place before opening. We highly recommend refrigerating after opening to preserve the vibrant flavor and natural color.</p></div>
                </div>
                <div class="faq-item">
                    <button class="faq-header">Does it contain artificial preservatives? <i class="fa-solid fa-chevron-down"></i></button>
                    <div class="faq-content"><p>Absolutely not. We rely on natural vinegars, salts, and high-quality ingredients to preserve our sauces naturally without chemicals.</p></div>
                </div>
            </div>
        </div>
    </section>

    <!-- RELATED PRODUCTS -->
    <section class="pd-related-section">
        <div class="container">
            <div class="section-heading text-center">
                <span class="section-label">DISCOVER MORE</span>
                <h2>You May Also <em>Love.</em></h2>
            </div>
            <div class="related-grid-3" id="pd-related">
                <!-- Injected via JS -->
            </div>
        </div>
    </section>

    <!-- BOLD FINAL CTA -->
    <section class="pd-final-cta">
        <div class="cta-inner container text-center">
            <span class="section-label" style="color: rgba(255,255,255,0.7);">NO COMPROMISES. JUST FLAVOR.</span>
            <h2>Ready to feel the <em>Heat?</em></h2>
            <p>Elevate your everyday meals with the perfect balance of premium ingredients and unapologetic fire.</p>
            <div class="cta-buttons">
                <button class="btn btn-primary" onclick="window.scrollTo({top: 0, behavior: 'smooth'});">Add to Cart Now</button>
                <a href="products.html" class="btn btn-outline" style="border-color: rgba(255,255,255,0.3); color: white;">Explore Collection</a>
            </div>
        </div>
    </section>

</main>

<script src="js/product-detail.js"></script>

<footer class="footer" style="background-color: var(--color-black); color: var(--color-white); padding-top: 60px;">
    <div class="container footer-container" style="display: grid; grid-template-columns: 2fr 1fr 1fr 1.5fr; gap: 40px; padding-bottom: 40px;">
        <!-- Brand & Socials -->
        <div class="footer-brand">
            <a href="index.html" class="footer-logo">
                <img src="assets/images/firecraft_logo.png" alt="Firecraft Logo" style="height: 65px; width: auto; object-fit: contain;">
            </a>
            <p style="margin-top: 20px; line-height: 1.6; color: var(--color-muted); font-size: 16px;">
                Crafting premium, small-batch hot sauces for serious flavor seekers. Elevate your everyday meals with the perfect balance of heat and taste.
            </p>
            <div class="social-links" style="display: flex; gap: 15px; margin-top: 25px;">
                <a href="#" style="color: var(--color-white); font-size: 18px;"><i class="fa-brands fa-facebook-f"></i></a>
                <a href="#" style="color: var(--color-white); font-size: 18px;"><i class="fa-brands fa-x-twitter"></i></a>
                <a href="#" style="color: var(--color-white); font-size: 18px;"><i class="fa-brands fa-instagram"></i></a>
            </div>
        </div>
        <!-- Quick Links -->
        <div class="footer-column">
            <h3 style="font-family: var(--font-body); font-size: 12px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 25px; color: white;">Quick Links</h3>
            <div style="display: flex; flex-direction: column; gap: 16px;">
                <a href="index.html" style="color: var(--color-muted); font-size: 12px; font-weight: 700; text-transform: uppercase; text-decoration: none;">Home</a>
                <a href="products.html" style="color: var(--color-muted); font-size: 12px; font-weight: 700; text-transform: uppercase; text-decoration: none;">Products</a>
                <a href="about.html" style="color: var(--color-muted); font-size: 12px; font-weight: 700; text-transform: uppercase; text-decoration: none;">About Us</a>
            </div>
        </div>
        <!-- Support -->
        <div class="footer-column">
            <h3 style="font-family: var(--font-body); font-size: 12px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 25px; color: white;">Support</h3>
            <div style="display: flex; flex-direction: column; gap: 16px;">
                <a href="contact.html" style="color: var(--color-muted); font-size: 12px; font-weight: 700; text-transform: uppercase; text-decoration: none;">Contact</a>
                <a href="#" style="color: var(--color-muted); font-size: 12px; font-weight: 700; text-transform: uppercase; text-decoration: none;">FAQs</a>
            </div>
        </div>
        <!-- Contact -->
        <div class="footer-column">
            <h3 style="font-family: var(--font-body); font-size: 12px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 25px; color: white;">Contact</h3>
            <div style="display: flex; flex-direction: column; gap: 20px;">
                <div style="display: flex; gap: 15px; align-items: flex-start;">
                    <i class="fa-solid fa-phone" style="color: var(--color-red);"></i>
                    <span style="color: var(--color-muted); font-size: 13px;">+1 (800) 123-4567</span>
                </div>
                <div style="display: flex; gap: 15px; align-items: flex-start;">
                    <i class="fa-solid fa-envelope" style="color: var(--color-red);"></i>
                    <span style="color: var(--color-muted); font-size: 13px;">hello@firecraft.com</span>
                </div>
            </div>
        </div>
    </div>
    <div class="footer-bottom">
        <div class="container footer-bottom-container" style="display: flex; justify-content: center; padding: 20px 0; border-top: 1px solid var(--color-border-dark);">
            <p style="color: var(--color-muted); font-size: 13px; font-weight: 500; letter-spacing: 0.02em;">
                © 2026 Firecraft. All rights reserved.
            </p>
        </div>
    </div>
</footer>

<script src="js/main.js"></script>
<script>
    // Tab functionality
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');
    
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            tabBtns.forEach(b => b.classList.remove('active'));
            tabPanes.forEach(p => p.classList.remove('active'));
            
            btn.classList.add('active');
            document.getElementById(btn.dataset.target).classList.add('active');
        });
    });

    // FAQ Accordion functionality
    const faqHeaders = document.querySelectorAll('.faq-header');
    faqHeaders.forEach(header => {
        header.addEventListener('click', () => {
            const content = header.nextElementSibling;
            const icon = header.querySelector('i');
            
            if (content.style.maxHeight) {
                content.style.maxHeight = null;
                header.classList.remove('active');
                icon.className = 'fa-solid fa-chevron-down';
            } else {
                content.style.maxHeight = content.scrollHeight + 'px';
                header.classList.add('active');
                icon.className = 'fa-solid fa-chevron-up';
            }
        });
    });
</script>
</body>
</html>
"""

css_content = """/* Premium Product Detail Styles */

body {
    background-color: var(--color-black);
}

/* 1. SPLIT SCREEN HERO */
.pd-hero-split {
    display: flex;
    min-height: 100vh;
    padding-top: 80px; /* Offset for navbar */
    position: relative;
}

.pd-hero-sticky-image {
    flex: 1;
    position: sticky;
    top: 80px;
    height: calc(100vh - 80px);
    background: var(--color-dark);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 40px;
    border-right: 1px solid var(--color-border-dark);
}

.image-wrapper {
    position: relative;
    width: 100%;
    max-width: 500px;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.image-wrapper img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    filter: drop-shadow(0 20px 40px rgba(0,0,0,0.5));
}

.glass-badge {
    position: absolute;
    top: 20px;
    right: 20px;
    background: rgba(20, 20, 20, 0.7);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
    color: var(--color-red);
    padding: 10px 20px;
    border-radius: 30px;
    font-weight: bold;
    font-size: 14px;
    letter-spacing: 1px;
    display: flex;
    align-items: center;
    gap: 8px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.3);
}

.pd-hero-scroll-content {
    flex: 1;
    padding: 60px 80px;
    background: var(--color-black);
    min-height: 100vh;
}

.breadcrumbs {
    font-size: 13px;
    color: var(--color-muted);
    margin-bottom: 30px;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.breadcrumbs a {
    color: var(--color-text-light);
    text-decoration: none;
    transition: color 0.3s;
}
.breadcrumbs a:hover {
    color: var(--color-red);
}

.pd-title {
    font-family: var(--font-display);
    font-size: 64px;
    line-height: 1.1;
    color: var(--color-text-light);
    margin-bottom: 20px;
}

.pd-rating-block {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 30px;
}
.pd-rating-block .stars {
    color: var(--color-red);
}
.pd-rating-block .rating-num {
    color: var(--color-text-light);
    font-weight: bold;
}
.pd-rating-block .review-count {
    color: var(--color-muted);
    font-size: 14px;
}

.pd-short-desc {
    font-size: 18px;
    color: var(--color-muted);
    line-height: 1.7;
    margin-bottom: 30px;
    max-width: 90%;
}

.pd-tags-container {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-bottom: 40px;
}

.flavor-badge {
    background: var(--color-dark);
    border: 1px solid var(--color-border-dark);
    color: var(--color-text-light);
    padding: 8px 16px;
    border-radius: 4px;
    font-size: 12px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    font-weight: 600;
}

.pd-price-row {
    margin-bottom: 30px;
    padding-bottom: 30px;
    border-bottom: 1px solid var(--color-border-dark);
}

.pd-price {
    font-size: 42px;
    font-weight: bold;
    color: var(--color-red);
    font-family: var(--font-display);
}

/* Actions */
.pd-actions-block {
    display: flex;
    gap: 15px;
    margin-bottom: 20px;
}

.qty-control {
    display: flex;
    align-items: center;
    background: var(--color-dark);
    border: 1px solid var(--color-border-dark);
    border-radius: 4px;
    height: 56px;
}

.qty-control button {
    background: transparent;
    border: none;
    color: var(--color-text-light);
    width: 50px;
    height: 100%;
    cursor: pointer;
    transition: background 0.3s;
}
.qty-control button:hover {
    background: rgba(255,255,255,0.05);
}

.qty-control input {
    width: 40px;
    text-align: center;
    background: transparent;
    border: none;
    color: var(--color-text-light);
    font-size: 18px;
    font-weight: bold;
}

.btn-add-cart {
    flex: 1;
    height: 56px;
    font-size: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
}

.btn-favorite {
    width: 56px;
    height: 56px;
    background: var(--color-dark);
    border: 1px solid var(--color-border-dark);
    color: var(--color-text-light);
    border-radius: 4px;
    cursor: pointer;
    font-size: 20px;
    transition: all 0.3s;
}
.btn-favorite:hover {
    color: var(--color-red);
    border-color: var(--color-red);
}

.pd-shipping-perk {
    font-size: 14px;
    color: var(--color-muted);
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 60px;
}
.pd-shipping-perk i {
    color: var(--color-red);
}

/* Details Grid (Flavor & Heat) */
.pd-details-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
    margin-bottom: 60px;
}

.detail-box {
    background: var(--color-dark);
    border: 1px solid var(--color-border-dark);
    border-radius: 12px;
    padding: 30px;
}

.detail-box h3 {
    font-family: var(--font-display);
    font-size: 28px;
    color: var(--color-text-light);
    margin-bottom: 20px;
    padding-bottom: 15px;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}

.flavor-box p {
    color: var(--color-muted);
    margin-bottom: 20px;
    font-size: 15px;
    line-height: 1.6;
}

.custom-list {
    list-style: none;
    padding: 0;
    margin: 0;
}
.custom-list li {
    position: relative;
    padding-left: 20px;
    margin-bottom: 10px;
    color: var(--color-text-light);
    font-size: 15px;
}
.custom-list li::before {
    content: "•";
    color: var(--color-red);
    position: absolute;
    left: 0;
    top: 0;
    font-size: 20px;
    line-height: 1;
}

.heat-stat {
    margin-bottom: 20px;
}
.heat-stat:last-child { margin-bottom: 0; }
.heat-stat span {
    display: block;
    font-size: 11px;
    color: var(--color-muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 5px;
}
.heat-stat strong {
    font-size: 18px;
    color: var(--color-text-light);
}

.heat-meter {
    display: flex;
    gap: 6px;
    margin-top: 8px;
}
.heat-meter .bar {
    flex: 1;
    height: 6px;
    background: var(--color-border-dark);
    border-radius: 3px;
}
.heat-meter .bar.active {
    background: var(--color-red);
    box-shadow: 0 0 10px rgba(230, 57, 70, 0.5);
}

/* Tabs Section */
.pd-tabs-section {
    background: var(--color-dark);
    border-radius: 12px;
    border: 1px solid var(--color-border-dark);
    padding: 30px;
    margin-bottom: 60px;
}

.pd-tabs-section h3 {
    font-family: var(--font-display);
    font-size: 28px;
    color: var(--color-text-light);
    margin-bottom: 20px;
}

.tabs-header {
    display: flex;
    gap: 10px;
    border-bottom: 1px solid var(--color-border-dark);
    margin-bottom: 20px;
    overflow-x: auto;
}

.tab-btn {
    background: transparent;
    border: none;
    color: var(--color-muted);
    padding: 10px 15px;
    font-size: 14px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    cursor: pointer;
    position: relative;
    transition: color 0.3s;
    white-space: nowrap;
}

.tab-btn:hover {
    color: var(--color-text-light);
}

.tab-btn.active {
    color: var(--color-red);
}

.tab-btn.active::after {
    content: '';
    position: absolute;
    bottom: -1px;
    left: 0;
    width: 100%;
    height: 2px;
    background: var(--color-red);
}

.tab-pane {
    display: none;
    color: var(--color-muted);
    font-size: 16px;
    line-height: 1.6;
}
.tab-pane.active {
    display: block;
    animation: fadeIn 0.4s ease forwards;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(5px); }
    to { opacity: 1; transform: translateY(0); }
}


/* 2. PAIRINGS SECTION (3 IMAGES) */
.pd-pairings-section {
    padding: 100px 0;
    background: var(--color-dark-soft);
    border-top: 1px solid var(--color-border-dark);
}

.section-subtitle {
    color: var(--color-muted);
    font-size: 18px;
    max-width: 600px;
    margin: 0 auto 50px;
}

.pairings-grid-3, .related-grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
}

.pairing-card {
    background: var(--color-dark);
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid var(--color-border-dark);
    transition: transform 0.3s, border-color 0.3s;
}
.pairing-card:hover {
    transform: translateY(-10px);
    border-color: var(--color-red);
}

.pairing-card img {
    width: 100%;
    height: 220px;
    object-fit: cover;
}

.pairing-info {
    padding: 25px;
    text-align: left;
}

.pairing-info h4 {
    font-family: var(--font-display);
    font-size: 24px;
    color: var(--color-text-light);
    margin-bottom: 10px;
}

.pairing-info p {
    color: var(--color-muted);
    font-size: 15px;
    line-height: 1.5;
}


/* 3. TUTORIAL SECTION */
.pd-tutorial-section {
    padding: 100px 0;
    background: var(--color-black);
}

.tutorial-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
}

.tutorial-text h2 {
    font-family: var(--font-display);
    font-size: 48px;
    color: var(--color-text-light);
    margin-bottom: 20px;
}

.tutorial-desc {
    color: var(--color-muted);
    font-size: 18px;
    margin-bottom: 40px;
    line-height: 1.6;
}

.tutorial-steps {
    display: flex;
    flex-direction: column;
    gap: 30px;
}

.step {
    display: flex;
    gap: 20px;
}

.step-num {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: rgba(230, 57, 70, 0.1);
    color: var(--color-red);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 18px;
    flex-shrink: 0;
    border: 1px solid rgba(230, 57, 70, 0.3);
}

.step-info h4 {
    color: var(--color-text-light);
    font-size: 20px;
    margin-bottom: 8px;
}

.step-info p {
    color: var(--color-muted);
    line-height: 1.5;
}

.tutorial-image img {
    width: 100%;
    border-radius: 12px;
    border: 1px solid var(--color-border-dark);
}

/* 4. REVIEWS SECTION */
.pd-reviews-section {
    padding: 100px 0;
    background: var(--color-dark);
    border-top: 1px solid var(--color-border-dark);
}

.pd-reviews-section h2 {
    font-family: var(--font-display);
    font-size: 48px;
    color: var(--color-text-light);
    margin-bottom: 50px;
}

.reviews-slider {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
}

.review-card {
    background: var(--card-bg-light);
    padding: 40px;
    border-radius: 12px;
    border: 1px solid var(--color-border-dark);
    text-align: left;
}

.review-stars {
    color: var(--color-red);
    margin-bottom: 20px;
}

.review-card h3 {
    color: var(--color-text-light);
    font-size: 24px;
    margin-bottom: 15px;
    font-family: var(--font-display);
}

.review-card p {
    color: var(--color-muted);
    font-size: 16px;
    line-height: 1.6;
    font-style: italic;
    margin-bottom: 30px;
}

.reviewer {
    display: flex;
    align-items: center;
    gap: 15px;
}

.reviewer .avatar {
    width: 40px;
    height: 40px;
    background: var(--color-red);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 18px;
}

.reviewer-info strong {
    display: block;
    color: var(--color-text-light);
    font-size: 14px;
}

.reviewer-info span {
    color: var(--color-muted);
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1px;
}


/* 5. FAQs SECTION */
.pd-faq-section {
    padding: 100px 0;
    background: var(--color-black);
}

.pd-faq-grid {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 60px;
}

.faq-intro h2 {
    font-family: var(--font-display);
    font-size: 48px;
    color: var(--color-text-light);
    margin-bottom: 20px;
}

.faq-intro p {
    color: var(--color-muted);
    font-size: 16px;
    line-height: 1.6;
}

.custom-accordion .faq-item {
    border-bottom: 1px solid var(--color-border-dark);
}

.custom-accordion .faq-item:first-child {
    border-top: 1px solid var(--color-border-dark);
}

.faq-header {
    width: 100%;
    text-align: left;
    background: transparent;
    border: none;
    color: var(--color-text-light);
    padding: 25px 0;
    font-size: 18px;
    font-weight: 600;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: color 0.3s;
}

.faq-header:hover, .faq-header.active {
    color: var(--color-red);
}

.faq-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease-out;
}

.faq-content p {
    padding-bottom: 25px;
    color: var(--color-muted);
    line-height: 1.6;
}


/* 6. RELATED */
.pd-related-section {
    padding: 100px 0;
    background: var(--color-dark-soft);
}

.related-card {
    background: var(--color-dark);
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid var(--color-border-dark);
    text-align: center;
    padding-bottom: 25px;
    cursor: pointer;
    transition: border-color 0.3s;
}

.related-card:hover {
    border-color: var(--color-red);
}

.related-card img {
    width: 100%;
    height: 250px;
    object-fit: contain;
    padding: 20px;
    background: var(--card-bg-light);
    margin-bottom: 20px;
}

.related-card h4 {
    font-family: var(--font-display);
    font-size: 24px;
    color: var(--color-text-light);
    margin-bottom: 10px;
}

.related-card .price {
    display: block;
    color: var(--color-red);
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 20px;
}


/* 7. FINAL CTA */
.pd-final-cta {
    padding: 120px 0;
    background: linear-gradient(135deg, var(--color-red) 0%, #900000 100%);
    position: relative;
}

.pd-final-cta::before {
    content: '';
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: url('../assets/images/noise.png');
    opacity: 0.1;
    pointer-events: none;
}

.cta-inner h2 {
    font-family: var(--font-display);
    font-size: 56px;
    color: white;
    margin-bottom: 20px;
}

.cta-inner p {
    color: rgba(255,255,255,0.9);
    font-size: 20px;
    max-width: 600px;
    margin: 0 auto 40px;
}

.cta-buttons {
    display: flex;
    justify-content: center;
    gap: 20px;
}

.cta-buttons .btn {
    padding: 18px 40px;
    font-size: 18px;
}
.cta-buttons .btn-primary {
    background: var(--color-black);
    color: white;
}
.cta-buttons .btn-primary:hover {
    background: #222;
}


/* Responsive */
@media (max-width: 1024px) {
    .pd-hero-split {
        flex-direction: column;
    }
    .pd-hero-sticky-image {
        position: static;
        height: 60vh;
        border-right: none;
        border-bottom: 1px solid var(--color-border-dark);
    }
    .pd-hero-scroll-content {
        padding: 40px 20px;
    }
    .pd-details-grid {
        grid-template-columns: 1fr;
    }
    .pairings-grid-3, .related-grid-3 {
        grid-template-columns: repeat(2, 1fr);
    }
    .tutorial-grid, .pd-faq-grid, .reviews-slider {
        grid-template-columns: 1fr;
    }
}
@media (max-width: 768px) {
    .pairings-grid-3, .related-grid-3 {
        grid-template-columns: 1fr;
    }
}
"""

with open('product-detail.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open('css/product-detail.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Redesign complete.")
