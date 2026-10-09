import os

html_content = '''        <!-- SECTION 03: THE FIRECRAFT HEAT GUIDE -->
        <section class="section-heat-guide-3 bg-dark text-white">
            <div class="container">
                <div class="heat-header-3 text-center">
                    <p class="eyebrow">FIND YOUR HEAT</p>
                    <h2 class="bold-heading">Not Every Fire Is The Same.</h2>
                    <p class="section-subtitle">Heat should add character to food, not hide it. FireCraft makes it easier to find the balance between flavor, intensity, and the foods you love.</p>
                </div>
                <div class="heat-spectrum">
                    <div class="spectrum-item">
                        <h4>MILD</h4>
                        <p>Flavor First</p>
                    </div>
                    <div class="spectrum-item">
                        <h4>MEDIUM</h4>
                        <p>Balanced Heat</p>
                    </div>
                    <div class="spectrum-item">
                        <h4>HOT</h4>
                        <p>Bold Intensity</p>
                    </div>
                    <div class="spectrum-item">
                        <h4>EXTRA HOT</h4>
                        <p>Serious Fire</p>
                    </div>
                </div>
                <div class="text-center" style="margin-top: 40px;">
                    <a href="products.html" class="btn btn-primary">Explore The Sauces</a>
                </div>
            </div>
        </section>

        <!-- SECTION 04: SAUCE COLLECTIONS -->
        <section class="section-collections bg-black text-white">
            <div class="container">
                <p class="eyebrow text-center">EXPLORE THE COLLECTION</p>
                <h2 class="bold-heading text-center">Different Foods. Different Fire.</h2>
                <div class="collection-grid">
                    <div class="collection-card" style="background-image: url('assets/images/product_sauces_1791360804955.jpg');">
                        <div class="collection-content">
                            <h3>EVERYDAY HEAT</h3>
                            <p>Sauces designed for everyday meals and easy pairing.</p>
                            <a href="#" class="link-btn">Explore &rarr;</a>
                        </div>
                    </div>
                    <div class="collection-card" style="background-image: url('assets/images/recipe_wings_1791360856984.jpg');">
                        <div class="collection-content">
                            <h3>SMOKY & SAVORY</h3>
                            <p>Deep, smoky flavors for grilled and roasted food.</p>
                            <a href="#" class="link-btn">Explore &rarr;</a>
                        </div>
                    </div>
                    <div class="collection-card" style="background-image: url('assets/images/product_condiments_1791360816664.jpg');">
                        <div class="collection-content">
                            <h3>SWEET HEAT</h3>
                            <p>A balanced combination of sweetness and controlled heat.</p>
                            <a href="#" class="link-btn">Explore &rarr;</a>
                        </div>
                    </div>
                    <div class="collection-card" style="background-image: url('assets/images/hero_bg_1791360790229.jpg');">
                        <div class="collection-content">
                            <h3>BOLD & HOT</h3>
                            <p>For people who want stronger intensity without sacrificing flavor.</p>
                            <a href="#" class="link-btn">Explore &rarr;</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION 05: FEATURED SAUCES -->
        <section class="section-featured bg-dark text-white">
            <div class="container">
                <p class="eyebrow text-center">THE FIRECRAFT COLLECTION</p>
                <h2 class="bold-heading text-center">Made To Change The Way You Eat.</h2>
                <div class="featured-grid">
                    <div class="featured-card">
                        <div class="featured-img">
                            <img src="assets/images/sauce_smoked_red_1791369304097.jpg" alt="Smoked Red">
                        </div>
                        <div class="featured-info">
                            <h3>SMOKED RED</h3>
                            <p class="flavor-desc">"Smoky heat with a deep savory finish."</p>
                            <div class="featured-meta">
                                <span><strong>Heat:</strong> ●●●○○</span>
                                <span><strong>Best with:</strong> Grilled meats / burgers</span>
                            </div>
                            <a href="#" class="btn btn-secondary">Discover Sauce</a>
                        </div>
                    </div>
                    <div class="featured-card">
                        <div class="featured-img">
                            <img src="assets/images/sauce_fire_roast_1791369316199.jpg" alt="Fire Roast">
                        </div>
                        <div class="featured-info">
                            <h3>FIRE ROAST</h3>
                            <p class="flavor-desc">"Bold, roasted peppers with a kick."</p>
                            <div class="featured-meta">
                                <span><strong>Heat:</strong> ●●●●○</span>
                                <span><strong>Best with:</strong> Tacos / wings</span>
                            </div>
                            <a href="#" class="btn btn-secondary">Discover Sauce</a>
                        </div>
                    </div>
                    <div class="featured-card">
                        <div class="featured-img">
                            <img src="assets/images/sauce_citrus_heat_1791369327864.jpg" alt="Citrus Heat">
                        </div>
                        <div class="featured-info">
                            <h3>CITRUS HEAT</h3>
                            <p class="flavor-desc">"Bright, tangy, and unapologetically hot."</p>
                            <div class="featured-meta">
                                <span><strong>Heat:</strong> ●●○○○</span>
                                <span><strong>Best with:</strong> Seafood / salads</span>
                            </div>
                            <a href="#" class="btn btn-secondary">Discover Sauce</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION 06: FLAVOR PHILOSOPHY -->
        <section class="section-philosophy bg-black text-white">
            <div class="container philosophy-layout">
                <div class="philosophy-content">
                    <p class="eyebrow">FLAVOR FIRST</p>
                    <h2 class="bold-heading">Heat Is Only The Beginning.</h2>
                    <p class="section-subtitle">At FireCraft, heat is part of the experience—not the entire experience. Every sauce is about creating balance between heat, flavor, texture, and the food it touches.</p>
                    <div class="philosophy-principles">
                        <div class="principle">
                            <span class="principle-num">01</span>
                            <div>
                                <h4>FLAVOR</h4>
                                <p>A sauce should bring something meaningful to the dish.</p>
                            </div>
                        </div>
                        <div class="principle">
                            <span class="principle-num">02</span>
                            <div>
                                <h4>BALANCE</h4>
                                <p>Heat should complement the ingredients around it.</p>
                            </div>
                        </div>
                        <div class="principle">
                            <span class="principle-num">03</span>
                            <div>
                                <h4>CHARACTER</h4>
                                <p>Every sauce should have its own personality.</p>
                            </div>
                        </div>
                        <div class="principle">
                            <span class="principle-num">04</span>
                            <div>
                                <h4>VERSATILITY</h4>
                                <p>Great sauce should work across more than one meal.</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="philosophy-image" style="background-image: url('assets/images/story_image_1791360872524.jpg');"></div>
            </div>
        </section>

        <!-- SECTION 07: SAUCE IN ACTION -->
        <section class="section-action bg-dark text-white">
            <div class="container">
                <h2 class="bold-heading text-center">Pour It. Pair It. Make It Yours.</h2>
                <div class="action-gallery">
                    <div class="action-item" style="background-image: url('assets/images/recipe_wings_1791360856984.jpg');">
                        <div class="action-overlay">
                            <h3>BURGERS</h3>
                            <p>"Add smoky depth and a controlled kick."</p>
                        </div>
                    </div>
                    <div class="action-item" style="background-image: url('assets/images/product_spices_1791360831178.jpg');">
                        <div class="action-overlay">
                            <h3>WINGS</h3>
                            <p>"Bring heat without losing the crunch."</p>
                        </div>
                    </div>
                    <div class="action-item" style="background-image: url('assets/images/hero_bg_1791360790229.jpg');">
                        <div class="action-overlay">
                            <h3>TACOS</h3>
                            <p>"Brighten every bite with bold flavor."</p>
                        </div>
                    </div>
                    <div class="action-item" style="background-image: url('assets/images/story_image_1791360872524.jpg');">
                        <div class="action-overlay">
                            <h3>GRILLED FOOD</h3>
                            <p>"Enhance char with deep, fiery notes."</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION 08: RECIPE DISCOVERY -->
        <section class="section-recipes bg-black text-white">
            <div class="container">
                <p class="eyebrow text-center">FROM BOTTLE TO PLATE</p>
                <h2 class="bold-heading text-center">More Ways To Use The Fire.</h2>
                <p class="section-subtitle text-center" style="margin-bottom: 60px;">FireCraft is not limited to simply pouring sauce over food.</p>
                <div class="recipe-grid">
                    <div class="recipe-card">
                        <img src="assets/images/recipe_wings_1791360856984.jpg" alt="Spicy Crispy Chicken">
                        <div class="recipe-info">
                            <h3>SPICY CRISPY CHICKEN</h3>
                            <p>Crunchy, juicy, and coated in fiery flavor.</p>
                            <span><strong>Pairing:</strong> Smoked Red</span>
                            <br><br>
                            <a href="recipes.html" class="link-btn">View Recipe &rarr;</a>
                        </div>
                    </div>
                    <div class="recipe-card">
                        <img src="assets/images/product_spices_1791360831178.jpg" alt="Smoky Burger">
                        <div class="recipe-info">
                            <h3>SMOKY BURGER</h3>
                            <p>A classic upgraded with intense, smoky notes.</p>
                            <span><strong>Pairing:</strong> Fire Roast</span>
                            <br><br>
                            <a href="recipes.html" class="link-btn">View Recipe &rarr;</a>
                        </div>
                    </div>
                    <div class="recipe-card">
                        <img src="assets/images/product_condiments_1791360816664.jpg" alt="Fire-Roasted Tacos">
                        <div class="recipe-info">
                            <h3>FIRE-ROASTED TACOS</h3>
                            <p>Vibrant, fresh, and perfectly spiced.</p>
                            <span><strong>Pairing:</strong> Citrus Heat</span>
                            <br><br>
                            <a href="recipes.html" class="link-btn">View Recipe &rarr;</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION 09: BUSINESS VALUE -->
        <section class="section-business-value bg-dark text-white">
            <div class="container">
                <p class="eyebrow text-center">BUILT BEYOND THE BOTTLE</p>
                <h2 class="bold-heading text-center">Made For People Who Serve More Than One Plate.</h2>
                <p class="section-subtitle text-center">FireCraft helps food businesses discover, manage, and work with products that fit their menu, kitchen, and customers.</p>
                <div class="business-pathways">
                    <div class="pathway-card">
                        <h3>RESTAURANTS</h3>
                        <p>Find sauces suited to your menu and kitchen.</p>
                    </div>
                    <div class="pathway-card">
                        <h3>RETAILERS</h3>
                        <p>Discover products and collections suitable for your customers.</p>
                    </div>
                    <div class="pathway-card">
                        <h3>FOOD BUSINESSES</h3>
                        <p>Build better food experiences with bold flavor.</p>
                    </div>
                </div>
                <div class="text-center" style="margin-top: 40px;">
                    <a href="#" class="btn btn-primary">Explore For Business</a>
                </div>
            </div>
        </section>

        <!-- SECTION 10: BUSINESS CTA -->
        <section class="section-business-cta bg-black text-white">
            <div class="container business-cta-layout">
                <div class="business-cta-content">
                    <h2 class="bold-heading">Bring FireCraft To Your Menu.</h2>
                    <p>Looking for sauces for your restaurant, café, retail shelf, or food business? Explore options designed for larger-scale food experiences.</p>
                    <div class="business-cta-buttons">
                        <a href="contact.html" class="btn btn-primary">Talk To FireCraft</a>
                        <a href="#" class="btn btn-secondary">Explore Business Options</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION 11: THE FIRECRAFT STORY -->
        <section class="section-story bg-dark text-white">
            <div class="container story-layout">
                <div class="story-image" style="background-image: url('assets/images/hero_bg_1791360790229.jpg');"></div>
                <div class="story-content">
                    <p class="eyebrow">OUR STORY</p>
                    <h2 class="bold-heading">Built Around Flavor.<br>Driven By Fire.</h2>
                    <p>FireCraft exists to make bold flavor more accessible, more intentional, and more enjoyable. We focus on flavor, experimentation, food, heat, craftsmanship, and discovery to bring you the best possible sauces.</p>
                    <a href="about.html" class="btn btn-primary">Discover Our Story</a>
                </div>
            </div>
        </section>

        <!-- SECTION 12: DISCOVER YOUR SAUCE -->
        <section class="section-recommendation bg-black text-white" id="recommendation">
            <div class="container text-center">
                <h2 class="bold-heading">Which Fire Is Yours?</h2>
                <div class="recommendation-ui">
                    <div class="recommendation-step">
                        <h3>WHAT DO YOU LOVE?</h3>
                        <div class="recommendation-options" id="rec-flavor">
                            <button class="rec-btn">smoky</button>
                            <button class="rec-btn">sweet</button>
                            <button class="rec-btn">savory</button>
                            <button class="rec-btn">tangy</button>
                            <button class="rec-btn">fiery</button>
                        </div>
                    </div>
                    <div class="recommendation-step">
                        <h3>WHAT ARE YOU EATING?</h3>
                        <div class="recommendation-options" id="rec-food">
                            <button class="rec-btn">burgers</button>
                            <button class="rec-btn">wings</button>
                            <button class="rec-btn">tacos</button>
                            <button class="rec-btn">fries</button>
                            <button class="rec-btn">grilled food</button>
                        </div>
                    </div>
                    <div class="recommendation-step">
                        <h3>WHAT LEVEL OF HEAT?</h3>
                        <div class="recommendation-options" id="rec-heat">
                            <button class="rec-btn">mild</button>
                            <button class="rec-btn">medium</button>
                            <button class="rec-btn">hot</button>
                            <button class="rec-btn">extra hot</button>
                        </div>
                    </div>
                    <div class="recommendation-result" id="rec-result" style="display: none; margin-top: 40px;">
                        <h3>Your FireCraft Match:</h3>
                        <h2 class="red-text" id="rec-match-name">SMOKED RED</h2>
                        <p>Perfect for your taste!</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION 13: REAL FOOD / REAL MOMENTS -->
        <section class="section-moments bg-dark text-white">
            <div class="container">
                <p class="eyebrow text-center">REAL FOOD. REAL FIRE.</p>
                <h2 class="bold-heading text-center">Show Us What You Made.</h2>
                <div class="moments-gallery">
                    <img src="assets/images/story_image_1791360872524.jpg" alt="Moment 1">
                    <img src="assets/images/product_spices_1791360831178.jpg" alt="Moment 2">
                    <img src="assets/images/recipe_wings_1791360856984.jpg" alt="Moment 3">
                    <img src="assets/images/product_condiments_1791360816664.jpg" alt="Moment 4">
                </div>
                <div class="text-center" style="margin-top: 40px;">
                    <a href="real-moments.html" class="btn btn-primary">Share Your Creation</a>
                </div>
            </div>
        </section>

        <!-- SECTION 14: WHY FIRECRAFT -->
        <section class="section-why bg-black text-white">
            <div class="container">
                <h2 class="bold-heading text-center">Why FireCraft?</h2>
                <div class="why-grid">
                    <div class="why-card">
                        <h3>FLAVOR-LED</h3>
                        <p>Heat never comes before flavor.</p>
                    </div>
                    <div class="why-card">
                        <h3>PAIRING-FIRST</h3>
                        <p>Every sauce has a purpose beyond simply being hot.</p>
                    </div>
                    <div class="why-card">
                        <h3>DISCOVERY</h3>
                        <p>Find new combinations and new ways to use sauce.</p>
                    </div>
                    <div class="why-card">
                        <h3>BUILT FOR FOOD</h3>
                        <p>Designed around real meals, kitchens, and people who love food.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION 15: NEWSLETTER -->
        <section class="section-newsletter" style="background-image: url('assets/images/newsletter_bg_1791360887045.jpg');">
            <div class="newsletter-overlay">
                <div class="container text-center">
                    <p class="eyebrow">STAY IN THE LOOP</p>
                    <h2 class="bold-heading">More Flavor. Straight To Your Inbox.</h2>
                    <p class="section-subtitle" style="margin-bottom: 40px;">Get new sauce releases, recipes, pairing ideas, and FireCraft updates.</p>
                    <form class="newsletter-form" id="newsletter-form">
                        <input type="email" placeholder="Email address" required>
                        <button type="submit" class="btn btn-primary">Join The Fire</button>
                    </form>
                </div>
            </div>
        </section>

        <!-- SECTION 16: FINAL CTA -->
        <section class="section-final-cta" style="background-image: url('assets/images/hero_bg_1791360790229.jpg');">
            <div class="final-cta-overlay">
                <div class="container text-center">
                    <h2 class="massive-heading">Ready To Turn Up The Flavor?</h2>
                    <p class="section-subtitle text-center" style="margin-bottom: 40px;">Discover your heat, find your sauce, and make every meal a little more interesting.</p>
                    <div class="final-cta-buttons">
                        <a href="products.html" class="btn btn-primary">Explore Sauces</a>
                        <button class="btn btn-secondary" onclick="document.getElementById('recommendation').scrollIntoView({behavior: 'smooth'})">Find Your Fire</button>
                    </div>
                </div>
            </div>
        </section>
    </main>
'''

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('</main>', html_content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
