import re

html_path = r'c:\Users\vigas\Desktop\firecraft\about.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_hero_html = '''        <!-- 1. ABOUT HERO -->
        <section class="about-hero">
            <div class="about-hero-bg">
                <img src="assets/images/about-hero.jpg" alt="Premium hot sauce and chilies">
                <div class="about-hero-overlay"></div>
            </div>
            <div class="container hero-container">
                <div class="hero-content">
                    <span class="eyebrow">OUR STORY</span>
                    <h1 class="hero-title">
                        BORN FROM<br>
                        A LOVE OF<br>
                        <span class="text-accent">BOLD FLAVOR.</span>
                    </h1>
                    <p class="hero-text">
                        Firecraft began with a simple idea — great food deserves more than ordinary sauce.
                    </p>
                    <div class="hero-actions">
                        <a href="products.html" class="primary-btn">Explore Our Sauces</a>
                        <a href="#story" class="outline-btn">Meet The Story</a>
                    </div>
                </div>
            </div>
        </section>'''

html = re.sub(r'<!-- 1\. ABOUT HERO -->.*?<!-- 2\. OUR BELIEF -->', new_hero_html + '\n\n        <!-- 2. OUR BELIEF -->', html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

css_path = r'c:\Users\vigas\Desktop\firecraft\css\about.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace hero css
old_hero_css_pattern = r'/\* 1\. ABOUT HERO \*/.*?/\* 2\. OUR BELIEF \*/'
new_hero_css = '''/* 1. ABOUT HERO */
.about-hero {
    position: relative;
    min-height: 90vh;
    display: flex;
    align-items: center;
    padding-top: 100px;
    padding-bottom: 100px;
    overflow: hidden;
}
.about-hero-bg {
    position: absolute;
    inset: 0;
    z-index: 1;
}
.about-hero-bg img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.about-hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(to right, rgba(8,8,8,0.9) 0%, rgba(8,8,8,0.2) 100%);
}
.hero-container {
    position: relative;
    z-index: 2;
    display: block;
}
.hero-content {
    position: relative;
}
.eyebrow {
    display: inline-block;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 0.15em;
    color: var(--color-red);
    margin-bottom: 25px;
    text-transform: uppercase;
}
.hero-title {
    font-family: var(--font-display);
    font-size: clamp(40px, 5vw, 65px);
    line-height: 1.05;
    margin-bottom: 30px;
    color: var(--color-white);
}
.text-accent {
    color: var(--color-red);
}
.hero-text {
    font-size: 16px;
    line-height: 1.6;
    color: var(--color-muted);
    margin-bottom: 40px;
    max-width: 450px;
}
.hero-actions {
    display: flex;
    gap: 20px;
    align-items: center;
}

/* 2. OUR BELIEF */'''

css = re.sub(old_hero_css_pattern, new_hero_css, css, flags=re.DOTALL)

# Reduce other font sizes globally
css = css.replace('clamp(40px, 5vw, 65px)', 'clamp(32px, 4vw, 50px)')
css = css.replace('clamp(60px, 8vw, 120px)', 'clamp(45px, 6vw, 75px)')
css = css.replace('clamp(50px, 7vw, 90px)', 'clamp(40px, 5vw, 65px)')

# Also ensure .hero-title size was replaced correctly in the new block above, we did it explicitly so it's fine.

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print('REDESIGN DONE')
