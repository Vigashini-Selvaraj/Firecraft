import os

css_content = '''

/* --- NEW SECTIONS STYLES --- */

/* Section 03: Heat Guide 3 */
.section-heat-guide-3 {
    padding: 140px 0;
}
.heat-spectrum {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 60px;
    gap: 20px;
}
.spectrum-item {
    text-align: center;
    flex: 1;
    padding: 30px;
    border-top: 2px solid var(--muted);
    transition: all 0.3s ease;
}
.spectrum-item:hover {
    border-top-color: var(--red);
    background: rgba(255,255,255,0.02);
}
.spectrum-item h4 {
    font-size: 24px;
    margin-bottom: 8px;
    color: var(--white);
}
.spectrum-item p {
    font-size: 14px;
    color: var(--muted-white);
}

/* Section 04: Sauce Collections */
.section-collections {
    padding: 140px 0;
}
.collection-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 30px;
    margin-top: 60px;
}
.collection-card {
    height: 400px;
    background-size: cover;
    background-position: center;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
}
.collection-content {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    padding: 40px;
    background: linear-gradient(to top, rgba(0,0,0,0.9), transparent);
}
.collection-content h3 {
    font-size: 32px;
    margin-bottom: 12px;
}
.collection-content p {
    font-size: 16px;
    margin-bottom: 20px;
    opacity: 0.8;
}

/* Section 05: Featured Sauces */
.section-featured {
    padding: 140px 0;
}
.featured-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 40px;
    margin-top: 60px;
}
.featured-card {
    background: var(--black);
    border-radius: 4px;
    overflow: hidden;
    transition: transform 0.3s ease;
}
.featured-card:hover {
    transform: translateY(-10px);
}
.featured-img {
    height: 300px;
    overflow: hidden;
}
.featured-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.featured-info {
    padding: 30px;
}
.featured-info h3 {
    font-size: 28px;
    margin-bottom: 12px;
}
.flavor-desc {
    font-style: italic;
    color: var(--muted-white);
    margin-bottom: 20px;
}
.featured-meta {
    display: flex;
    flex-direction: column;
    gap: 8px;
    margin-bottom: 24px;
    font-size: 14px;
}
.featured-meta strong {
    color: var(--red);
}

/* Section 06: Flavor Philosophy */
.section-philosophy {
    padding: 140px 0;
}
.philosophy-layout {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 80px;
    align-items: center;
}
.philosophy-principles {
    margin-top: 40px;
    display: flex;
    flex-direction: column;
    gap: 30px;
}
.principle {
    display: flex;
    gap: 20px;
}
.principle-num {
    font-size: 24px;
    font-weight: 800;
    color: var(--red);
}
.principle h4 {
    font-size: 20px;
    margin-bottom: 8px;
}
.philosophy-image {
    height: 600px;
    background-size: cover;
    background-position: center;
    border-radius: 4px;
}

/* Section 07: Sauce in Action */
.section-action {
    padding: 140px 0;
}
.action-gallery {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    margin-top: 60px;
}
.action-item {
    height: 400px;
    background-size: cover;
    background-position: center;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
}
.action-overlay {
    position: absolute;
    bottom: 0; left: 0; width: 100%;
    padding: 30px;
    background: linear-gradient(to top, rgba(0,0,0,0.9), transparent);
}
.action-overlay h3 {
    font-size: 24px;
    margin-bottom: 8px;
}
.action-overlay p {
    font-size: 14px;
    font-style: italic;
    opacity: 0.8;
}

/* Section 08: Recipe Discovery */
.section-recipes {
    padding: 140px 0;
}
.recipe-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 40px;
    margin-top: 60px;
}
.recipe-card img {
    width: 100%;
    height: 250px;
    object-fit: cover;
    border-radius: 4px;
    margin-bottom: 20px;
}
.recipe-info h3 {
    font-size: 24px;
    margin-bottom: 12px;
}
.recipe-info p {
    margin-bottom: 12px;
    color: var(--muted-white);
}
.recipe-info span strong {
    color: var(--red);
}

/* Section 09: Business Value */
.section-business-value {
    padding: 140px 0;
}
.business-pathways {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 40px;
    margin-top: 60px;
}
.pathway-card {
    background: var(--black);
    padding: 40px;
    border-radius: 4px;
    border-top: 4px solid var(--red);
    text-align: center;
}
.pathway-card h3 {
    font-size: 24px;
    margin-bottom: 16px;
}

/* Section 10: Business CTA */
.section-business-cta {
    padding: 140px 0;
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
}
.business-cta-layout {
    text-align: center;
    max-width: 800px;
    margin: 0 auto;
}
.business-cta-buttons {
    margin-top: 40px;
    display: flex;
    justify-content: center;
    gap: 20px;
}

/* Section 11: Story */
.section-story {
    padding: 140px 0;
}
.story-layout {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 80px;
    align-items: center;
}
.story-image {
    height: 500px;
    background-size: cover;
    background-position: center;
    border-radius: 4px;
}
.story-content p {
    font-size: 18px;
    color: var(--muted-white);
    margin-bottom: 40px;
}

/* Section 12: Recommendation */
.section-recommendation {
    padding: 140px 0;
}
.recommendation-ui {
    margin-top: 60px;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}
.recommendation-step {
    margin-bottom: 40px;
}
.recommendation-step h3 {
    font-size: 18px;
    margin-bottom: 20px;
    color: var(--muted);
    letter-spacing: 0.1em;
}
.recommendation-options {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 12px;
}
.rec-btn {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--white);
    padding: 10px 24px;
    border-radius: 30px;
    cursor: pointer;
    text-transform: uppercase;
    font-weight: 700;
    font-size: 13px;
    transition: all 0.2s ease;
}
.rec-btn.active, .rec-btn:hover {
    background: var(--red);
    border-color: var(--red);
}

/* Section 13: Moments */
.section-moments {
    padding: 140px 0;
}
.moments-gallery {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    margin-top: 60px;
}
.moments-gallery img {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 4px;
}

/* Section 14: Why FireCraft */
.section-why {
    padding: 140px 0;
}
.why-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 40px;
    margin-top: 60px;
    text-align: center;
}
.why-card h3 {
    font-size: 20px;
    margin-bottom: 12px;
    color: var(--red);
}

/* Section 15: Newsletter */
.section-newsletter {
    position: relative;
    background-size: cover;
    background-position: center;
    padding: 160px 0;
}
.newsletter-overlay {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.8);
    display: flex;
    align-items: center;
    justify-content: center;
}
.section-newsletter .container {
    position: relative;
    z-index: 2;
    max-width: 600px;
}
.newsletter-form {
    display: flex;
    margin-top: 40px;
}
.newsletter-form input {
    flex: 1;
    padding: 16px 20px;
    border: none;
    background: rgba(255,255,255,0.1);
    color: var(--white);
    font-size: 16px;
    border-radius: 4px 0 0 4px;
}
.newsletter-form input:focus {
    outline: none;
    background: rgba(255,255,255,0.2);
}
.newsletter-form button {
    border-radius: 0 4px 4px 0;
}

/* Section 16: Final CTA */
.section-final-cta {
    position: relative;
    background-size: cover;
    background-position: center;
    padding: 200px 0;
}
.final-cta-overlay {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.9));
}
.section-final-cta .container {
    position: relative;
    z-index: 2;
}
.final-cta-buttons {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 40px;
}

/* Responsive updates for new sections */
@media (max-width: 1024px) {
    .collection-grid { grid-template-columns: 1fr; }
    .featured-grid, .recipe-grid, .business-pathways { grid-template-columns: repeat(2, 1fr); }
    .philosophy-layout, .story-layout { grid-template-columns: 1fr; }
    .action-gallery, .moments-gallery, .why-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 768px) {
    .featured-grid, .recipe-grid, .business-pathways, .action-gallery, .moments-gallery, .why-grid, .heat-spectrum { grid-template-columns: 1fr; flex-direction: column; }
    .newsletter-form { flex-direction: column; }
    .newsletter-form input { border-radius: 4px; margin-bottom: 16px; }
    .newsletter-form button { border-radius: 4px; }
}

'''

with open('css/home.css', 'a', encoding='utf-8') as f:
    f.write(css_content)

