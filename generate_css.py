def generate_css():
    css_content = """/* =====================================================
   PRODUCTS PAGE STYLES
===================================================== */

/* HERO SECTION */
.products-hero {
    position: relative;
    padding: 220px 0 160px;
    background: var(--color-dark);
    border-bottom: 1px solid var(--color-border-dark);
    overflow: hidden;
}
.products-hero .hero-bg {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: url('../assets/images/hero_fiery_hot_sauce_v2.jpg') center/cover no-repeat;
    opacity: 0.15;
    z-index: 0;
}
.hero-content-wrapper {
    position: relative;
    z-index: 1;
}
.products-hero h1 {
    font-family: var(--font-display);
    font-size: clamp(52px, 7vw, 90px);
    margin: 15px 0 20px;
    font-weight: 400;
    color: var(--color-text-light);
    line-height: 0.95;
    letter-spacing: -0.02em;
}
.products-hero h1 em {
    color: var(--color-red);
    font-style: normal;
}
.products-hero p {
    color: var(--color-muted);
    font-size: 18px;
    line-height: 1.7;
    max-width: 600px;
    margin: 0 auto;
}
.hero-buttons {
    margin-top: 40px;
    display: flex;
    gap: 15px;
    justify-content: center;
}

/* SECTION HEADING */
.section-heading {
    margin-bottom: 70px;
}
.section-heading h2 {
    font-family: var(--font-display);
    font-size: clamp(40px, 5vw, 60px);
    color: var(--color-text-light);
    margin-top: 15px;
}
.section-heading h2 em {
    color: var(--color-red);
    font-style: normal;
}

/* COLLECTION GRID */
.collection-section {
    padding: 120px 0;
}
.collection-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 60px;
}
.product-card {
    display: flex;
    flex-direction: column;
}
.product-image {
    background: var(--color-dark-soft);
    border: 1px solid var(--color-border-dark);
    border-radius: 4px;
    padding: 60px;
    text-align: center;
    transition: border-color 0.4s ease;
}
.product-image img {
    height: 350px;
    width: auto;
    object-fit: contain;
    transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);
}
.product-card:hover .product-image {
    border-color: var(--color-red);
}
.product-card:hover .product-image img {
    transform: scale(1.05) translateY(-10px);
}
.product-info {
    padding: 30px 0;
}
.heat-bar {
    margin-bottom: 15px;
}
.heat-level {
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 0.15em;
    padding: 4px 10px;
    border-radius: 2px;
}
.heat-level.mild { background: #333; color: #fff; }
.heat-level.medium { background: #8B4513; color: #fff; }
.heat-level.hot { background: var(--color-red); color: #fff; }
.heat-level.extra-hot { background: #800000; color: #fff; }

.product-info h3 {
    font-family: var(--font-display);
    font-size: 32px;
    color: var(--color-text-light);
    margin-bottom: 15px;
}
.product-info p {
    font-size: 15px;
    color: var(--color-muted);
    margin-bottom: 10px;
    line-height: 1.6;
}
.product-info p strong {
    color: var(--color-text-light);
}
.product-actions {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 25px;
    padding-top: 25px;
    border-top: 1px solid var(--color-border-dark);
}
.price {
    font-size: 20px;
    font-weight: 600;
    color: var(--color-text-light);
}

/* HEAT SCALE */
.heat-scale-section {
    padding: 100px 0;
}
.heat-scale-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 30px;
}
.heat-step {
    background: var(--color-dark-soft);
    padding: 40px 30px;
    border-radius: 4px;
    border: 1px solid var(--color-border-dark);
    text-align: center;
    transition: transform 0.3s;
}
.heat-step:hover {
    transform: translateY(-5px);
    border-color: var(--color-red);
}
.heat-icon {
    font-size: 24px;
    color: var(--color-red);
    margin-bottom: 20px;
    display: flex;
    justify-content: center;
    gap: 5px;
}
.heat-step h3 {
    font-family: var(--font-display);
    font-size: 24px;
    color: var(--color-text-light);
    margin-bottom: 15px;
}
.heat-step p {
    font-size: 14px;
    color: var(--color-muted);
    line-height: 1.6;
}

/* FLAVOR PROFILES & PAIRINGS */
.flavor-pairing-section {
    padding: 120px 0;
}
.fp-layout {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 80px;
    align-items: center;
}
.fp-content h2 {
    font-family: var(--font-display);
    font-size: 48px;
    color: var(--color-text-light);
    margin: 15px 0 20px;
}
.fp-content h2 em {
    color: var(--color-red);
    font-style: normal;
}
.fp-content p {
    color: var(--color-muted);
    font-size: 16px;
    line-height: 1.7;
    margin-bottom: 40px;
}
.tags-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
}
.flavor-tag {
    background: var(--color-dark-soft);
    border: 1px solid var(--color-border-dark);
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 14px;
    font-weight: 600;
    color: var(--color-text-light);
    letter-spacing: 0.05em;
    text-transform: uppercase;
}
.fp-pairings {
    display: grid;
    grid-template-columns: 1fr;
    gap: 20px;
}
.pairing-item {
    display: flex;
    align-items: center;
    gap: 20px;
    background: var(--color-dark-soft);
    padding: 25px;
    border: 1px solid var(--color-border-dark);
    border-radius: 4px;
}
.pairing-item i {
    font-size: 28px;
    color: var(--color-red);
    width: 40px;
    text-align: center;
}
.pairing-item h4 {
    color: var(--color-text-light);
    font-size: 18px;
    margin-bottom: 5px;
}
.pairing-item p {
    color: var(--color-muted);
    font-size: 14px;
}
.pairing-item p strong {
    color: var(--color-red);
}

/* FIND YOUR SAUCE SELECTOR */
.find-sauce-section {
    padding: 100px 0;
}
.find-sauce-box {
    max-width: 700px;
    margin: 0 auto;
    background: var(--color-dark);
    padding: 60px;
    border-radius: 4px;
    border: 1px solid var(--color-border-dark);
}
.find-sauce-box h2 {
    font-family: var(--font-display);
    font-size: 42px;
    color: var(--color-text-light);
    margin-bottom: 10px;
}
.find-sauce-box h2 em {
    color: var(--color-red);
    font-style: normal;
}
.find-sauce-box p {
    color: var(--color-muted);
    margin-bottom: 40px;
}
.selector-form {
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.selector-group {
    display: flex;
    flex-direction: column;
    text-align: left;
}
.selector-group label {
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--color-muted);
    margin-bottom: 8px;
}
.selector-group select {
    background: var(--color-dark-soft);
    border: 1px solid var(--color-border-dark);
    color: var(--color-text-light);
    padding: 15px;
    font-size: 16px;
    border-radius: 4px;
    outline: none;
    font-family: inherit;
}
.selector-group select:focus {
    border-color: var(--color-red);
}

/* BUNDLES */
.bundles-section {
    padding: 120px 0;
}
.bundles-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 40px;
}
.bundle-card {
    background: var(--color-dark-soft);
    border: 1px solid var(--color-border-dark);
    padding: 40px;
    border-radius: 4px;
    text-align: center;
    transition: transform 0.3s;
}
.bundle-card:hover {
    transform: translateY(-5px);
    border-color: var(--color-red);
}
.bundle-content h3 {
    font-family: var(--font-display);
    font-size: 28px;
    color: var(--color-text-light);
    margin-bottom: 15px;
}
.bundle-content p {
    color: var(--color-muted);
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 25px;
}
.bundle-content .price {
    display: block;
    font-size: 24px;
    color: var(--color-red);
    margin-bottom: 25px;
}

/* RESPONSIVE */
@media (max-width: 992px) {
    .collection-grid, .fp-layout, .heat-scale-grid {
        grid-template-columns: 1fr;
    }
    .bundles-grid {
        grid-template-columns: 1fr;
    }
    .heat-scale-grid {
        grid-template-columns: 1fr 1fr;
    }
}
@media (max-width: 768px) {
    .heat-scale-grid {
        grid-template-columns: 1fr;
    }
    .hero-buttons {
        flex-direction: column;
    }
}
"""
    with open('css/products.css', 'w', encoding='utf-8') as f:
        f.write(css_content)

if __name__ == "__main__":
    generate_css()
