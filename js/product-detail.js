const productsData = {
    'classic-hot-sauce': {
        id: 'classic-hot-sauce',
        name: 'Classic Hot Sauce',
        image: 'assets/images/products/Classic-Hot-Sauce.png',
        price: '$120',
        size: '12 Bottles / Case',
        heat: 'Mild',
        heatScore: 2,
        pepper: 'Red Jalapeño & Cayenne',
        scoville: '2,500 SHU',
        shortDesc: 'The perfect balance of heat and tang for any meal. Wholesale bulk ordering only.',
        flavorTags: ['Tangy', 'Zesty', 'Pepper-forward'],
        rating: 4.8,
        reviewCount: 342,
        flavorProfile: {
            notes: ['Tangy', 'Pepper-forward', 'Bold heat', 'Balanced acidity'],
            desc: 'A bright, zesty vinegar base that cuts through rich, heavy cheese perfectly without overwhelming the palate.'
        },
        ingredients: 'Aged Red Jalapeño Peppers, Cayenne Peppers, Distilled Vinegar, Sea Salt, Garlic, Onion Powder, Spices.',
        texture: 'Smooth, thin, perfect for dashing.',
        shelfLife: '2 Years Unopened, 6 Months Refrigerated After Opening.',
        allergens: 'None',
        pairings: [
            { name: 'Pizza & Flatbreads', desc: 'Cuts through rich cheese perfectly.', img: 'assets/images/products/Hot-Honey-Pizza.png' },
            { name: 'Breakfast Eggs', desc: 'Wake up your morning scramble.', img: 'assets/images/products/Chilli-Garlic-Noodles.png' },
            { name: 'Avocado Toast', desc: 'A dash of zesty heat to start the day.', img: 'assets/images/products/everyday-sauce.png' }
        ],
        related: ['smoked-jalapeno', 'garlic-chili', 'daily-blaze']
    },
    'mango-habanero': {
        id: 'mango-habanero',
        name: 'Mango Habanero',
        image: 'assets/images/products/Mango-Habanero-Hot-Sauce.png',
        price: '$140',
        size: '12 Bottles / Case',
        heat: 'Hot',
        heatScore: 4,
        pepper: 'Orange Habanero',
        scoville: '45,000 SHU',
        shortDesc: 'A fierce, sweet and fruity burn that pairs beautifully with grilled chicken and tacos.',
        flavorTags: ['Sweet', 'Fruity', 'Fiery'],
        rating: 4.9,
        reviewCount: 512,
        flavorProfile: {
            notes: ['Tropical', 'Sweet upfront', 'Fiery finish', 'Citrusy'],
            desc: 'A sugary front note that quickly gives way to intense, lingering heat from fresh orange habaneros.'
        },
        ingredients: 'Fresh Mangoes, Orange Habanero Peppers, Apple Cider Vinegar, Lime Juice, Sea Salt, Agave Nectar.',
        texture: 'Slightly pulpy, medium thickness.',
        shelfLife: '1 Year Unopened, 6 Months Refrigerated After Opening.',
        allergens: 'None',
        pairings: [
            { name: 'Grilled Chicken', desc: 'The ultimate sweet heat glaze.', img: 'assets/images/products/Fire-Wings.png' },
            { name: 'Tacos', desc: 'Elevates fish and pork tacos instantly.', img: 'assets/images/products/Spicy-Chicken-Tacos.png' },
            { name: 'Shrimp Skewers', desc: 'Perfect tropical glaze for seafood.', img: 'assets/images/sauce_smoked_red_1791369304097.jpg' }
        ],
        related: ['pineapple-habanero', 'ghost-pepper', 'classic-hot-sauce']
    },
    'chipotle-bbq': {
        id: 'chipotle-bbq',
        name: 'Chipotle BBQ',
        image: 'assets/images/products/Chipotle-BBQ-Sauce.png',
        price: '$130',
        size: '12 Bottles / Case',
        heat: 'Medium',
        heatScore: 3,
        pepper: 'Smoked Chipotle & Ancho',
        scoville: '10,000 SHU',
        shortDesc: 'Deep, earthy molasses and oak-smoked chili for ribs and burgers.',
        flavorTags: ['Smoky', 'Earthy', 'Rich'],
        rating: 4.7,
        reviewCount: 289,
        flavorProfile: {
            notes: ['Oak-smoked', 'Molasses', 'Earthy', 'Savory'],
            desc: 'Deep, oak-smoked chili notes that instantly elevate grilled meats and rich dishes.'
        },
        ingredients: 'Tomato Puree, Smoked Chipotle Peppers, Molasses, Brown Sugar, Apple Cider Vinegar, Garlic, Onion, Spices.',
        texture: 'Thick, sticky, perfect for glazing.',
        shelfLife: '18 Months Unopened, 6 Months Refrigerated.',
        allergens: 'None',
        pairings: [
            { name: 'Ribs & Brisket', desc: 'The ultimate BBQ companion.', img: 'assets/images/sauce_smoked_red_1791369304097.jpg' },
            { name: 'Burgers', desc: 'Mix into mayo or spread directly.', img: 'assets/images/products/Fire-Wings.png' },
            { name: 'Pulled Pork', desc: 'Smoky, earthy depth for slow-cooked meats.', img: 'assets/images/products/Chipotle-BBQ-Sauce.png' }
        ],
        related: ['smoked-jalapeno', 'ghost-pepper', 'classic-hot-sauce']
    },
    'garlic-chili': {
        id: 'garlic-chili',
        name: 'Garlic Chili Sauce',
        image: 'assets/images/products/Garlic-Chili-Sauce.png',
        price: '$135',
        size: '12 Bottles / Case',
        heat: 'Medium',
        heatScore: 3,
        pepper: 'Red Jalapeño & Fresno',
        scoville: '5,000 SHU',
        shortDesc: 'Deeply savory and garlicky, perfect for noodles, stir-fry, or any savory dish.',
        flavorTags: ['Garlicky', 'Umami', 'Zesty'],
        rating: 4.8,
        reviewCount: 420,
        flavorProfile: {
            notes: ['Roasted Garlic', 'Umami', 'Zesty', 'Savory'],
            desc: 'Savory roasted garlic blended with sharp chilies for ultimate umami depth.'
        },
        ingredients: 'Red Jalapeño Peppers, Garlic (Roasted and Raw), Rice Vinegar, Sea Salt, Sesame Oil.',
        texture: 'Chunky, garlic-heavy.',
        shelfLife: '1 Year Unopened.',
        allergens: 'Contains Sesame.',
        pairings: [
            { name: 'Noodles & Stir-Fries', desc: 'Toss directly into wok for instant flavor.', img: 'assets/images/products/Chilli-Garlic-Noodles.png' },
            { name: 'Dumplings', desc: 'The perfect dipping companion.', img: 'assets/images/products/Spicy-Chicken-Tacos.png' },
            { name: 'Fried Rice', desc: 'An umami explosion for wok-tossed dishes.', img: 'assets/images/products/Garlic-Chili-Sauce.png' }
        ],
        related: ['classic-hot-sauce', 'daily-blaze', 'chipotle-bbq']
    },
    'ghost-pepper': {
        id: 'ghost-pepper',
        name: 'Ghost Pepper Reserve',
        image: 'assets/images/products/extra-hot.png',
        price: '$160',
        size: '12 Bottles / Case',
        heat: 'Extra Hot',
        heatScore: 5,
        pepper: 'Bhut Jolokia (Ghost Pepper)',
        scoville: '650,000 SHU',
        shortDesc: 'Pure fire and earthy smoke. Use with extreme caution on your BBQ.',
        flavorTags: ['Fiery', 'Smoky', 'Intense'],
        rating: 4.9,
        reviewCount: 890,
        flavorProfile: {
            notes: ['Extreme Heat', 'Earthy', 'Smoky undertones', 'Lingering burn'],
            desc: 'Unapologetic, aggressive flavor profiles that refuse to take a back seat. Pure, unfiltered heat.'
        },
        ingredients: 'Ghost Peppers, White Vinegar, Sea Salt, Garlic, Black Pepper.',
        texture: 'Smooth, thin.',
        shelfLife: '3 Years Unopened.',
        allergens: 'None',
        pairings: [
            { name: 'Wings', desc: 'For those who want their endorphins racing.', img: 'assets/images/products/Fire-Wings.png' },
            { name: 'Chili & Stews', desc: 'Add one drop to a pot for huge heat.', img: 'assets/images/sauce_smoked_red_1791369304097.jpg' },
            { name: 'Bravest Burgers', desc: 'Mix into a fiery aioli if you dare.', img: 'assets/images/products/extra-hot.png' }
        ],
        related: ['mango-habanero', 'pineapple-habanero', 'chipotle-bbq']
    },
    'smoked-jalapeno': {
        id: 'smoked-jalapeno',
        name: 'Smoked Jalapeño',
        image: 'assets/images/products/deep-and-smoky.png',
        price: '$125',
        size: '12 Bottles / Case',
        heat: 'Mild',
        heatScore: 2,
        pepper: 'Smoked Green Jalapeño',
        scoville: '3,000 SHU',
        shortDesc: 'Mild smoky zest that elevates tacos and nachos without burning your tongue.',
        flavorTags: ['Smoky', 'Zesty', 'Mild'],
        rating: 4.6,
        reviewCount: 210,
        flavorProfile: {
            notes: ['Oak-smoked', 'Green zest', 'Mild heat', 'Savory'],
            desc: 'A gentle, warming tingle. Perfect for enhancing flavor without breaking a sweat.'
        },
        ingredients: 'Smoked Green Jalapeño Peppers, Apple Cider Vinegar, Sea Salt, Garlic.',
        texture: 'Medium thickness.',
        shelfLife: '2 Years Unopened.',
        allergens: 'None',
        pairings: [
            { name: 'Tacos & Nachos', desc: 'Earthy flavors perfect for Mexican cuisine.', img: 'assets/images/products/Spicy-Chicken-Tacos.png' },
            { name: 'Eggs', desc: 'A smoky start to your morning.', img: 'assets/images/products/Hot-Honey-Pizza.png' },
            { name: 'Grilled Veggies', desc: 'Adds a campfire depth to zucchini and peppers.', img: 'assets/images/products/deep-and-smoky.png' }
        ],
        related: ['classic-hot-sauce', 'chipotle-bbq', 'daily-blaze']
    },
    'pineapple-habanero': {
        id: 'pineapple-habanero',
        name: 'Pineapple Habanero',
        image: 'assets/images/products/Fruit-Forward.png',
        price: '$140',
        size: '12 Bottles / Case',
        heat: 'Hot',
        heatScore: 4,
        pepper: 'Orange Habanero',
        scoville: '40,000 SHU',
        shortDesc: 'A sharp tropical bite that works surprisingly incredibly well on a hot slice of pizza.',
        flavorTags: ['Fruity', 'Tropical', 'Fiery'],
        rating: 4.8,
        reviewCount: 305,
        flavorProfile: {
            notes: ['Tropical fruit', 'Sharp heat', 'Citrus', 'Sweet'],
            desc: 'Tropical fruit notes that pair wonderfully with light, acidic, or fresh dishes.'
        },
        ingredients: 'Fresh Pineapple, Habanero Peppers, White Vinegar, Lime Juice, Sea Salt.',
        texture: 'Slightly pulpy.',
        shelfLife: '1 Year Unopened.',
        allergens: 'None',
        pairings: [
            { name: 'Pizza', desc: 'Hawaiian pizza elevated to the next level.', img: 'assets/images/products/Hot-Honey-Pizza.png' },
            { name: 'Seafood', desc: 'Perfect on grilled fish or shrimp tacos.', img: 'assets/images/products/Spicy-Chicken-Tacos.png' },
            { name: 'Pork Chops', desc: 'Sweet, tropical acidity cuts through the richness.', img: 'assets/images/products/Fruit-Forward.png' }
        ],
        related: ['mango-habanero', 'ghost-pepper', 'classic-hot-sauce']
    },
    'daily-blaze': {
        id: 'daily-blaze',
        name: 'The Daily Blaze',
        image: 'assets/images/products/everyday-sauce.png',
        price: '$120',
        size: '12 Bottles / Case',
        heat: 'Medium',
        heatScore: 3,
        pepper: 'Cayenne & Habanero Blend',
        scoville: '15,000 SHU',
        shortDesc: 'Your new daily driver. Balanced heat and tang that is good on literally everything.',
        flavorTags: ['Balanced', 'Versatile', 'Zesty'],
        rating: 4.9,
        reviewCount: 1024,
        flavorProfile: {
            notes: ['Perfectly balanced', 'Tangy', 'Medium kick', 'Versatile'],
            desc: 'The sweet spot for everyday heat seekers. A satisfying, noticeable kick that doesn\'t linger too long.'
        },
        ingredients: 'Cayenne Peppers, Habanero Peppers, Distilled Vinegar, Sea Salt, Garlic Powder.',
        texture: 'Smooth, medium thickness.',
        shelfLife: '2 Years Unopened.',
        allergens: 'None',
        pairings: [
            { name: 'Everything', desc: 'Literally everything.', img: 'assets/images/products/Chilli-Garlic-Noodles.png' },
            { name: 'Sandwiches', desc: 'Mix into mayo for a spicy spread.', img: 'assets/images/products/Hot-Honey-Pizza.png' },
            { name: 'Roasted Potatoes', desc: 'A bright, zesty drizzle for crispy sides.', img: 'assets/images/products/everyday-sauce.png' }
        ],
        related: ['classic-hot-sauce', 'garlic-chili', 'chipotle-bbq']
    }
};

document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    let productId = urlParams.get('id');
    
    // Default to classic if none provided
    if (!productId || !productsData[productId]) {
        productId = 'classic-hot-sauce';
    }

    const product = productsData[productId];
    
    // Update Document Title
    document.title = product.name + ' - Firecraft';
    const bName = document.getElementById('pd-breadcrumb-name'); if(bName) bName.textContent = product.name;
    
    // Populate Hero
    document.getElementById('pd-image').src = product.image;
    document.getElementById('pd-name').textContent = product.name;
    document.getElementById('pd-desc').textContent = product.shortDesc;
    document.getElementById('pd-price').innerHTML = product.price + ' <span style="font-size:14px; font-weight:normal; color:var(--color-muted);">( ' + product.size + ' )</span>';
    document.getElementById('pd-rating').textContent = product.rating;
    document.getElementById('pd-reviews').textContent = '(' + product.reviewCount + ' Reviews)';
    document.getElementById('pd-heat').textContent = product.heat;
    
    const tagsContainer = document.getElementById('pd-tags');
    tagsContainer.innerHTML = '';
    product.flavorTags.forEach(tag => {
        const span = document.createElement('span');
        span.className = 'flavor-badge';
        span.textContent = tag;
        tagsContainer.appendChild(span);
    });

    // Populate Flavor Profile
    document.getElementById('pd-flavor-desc').textContent = product.flavorProfile.desc;
    const notesContainer = document.getElementById('pd-flavor-notes');
    notesContainer.innerHTML = '';
    product.flavorProfile.notes.forEach(note => {
        const li = document.createElement('li');
        li.textContent = note;
        notesContainer.appendChild(li);
    });

    // Populate Heat Breakdown
    document.getElementById('pd-pepper').textContent = product.pepper;
    document.getElementById('pd-scoville').textContent = product.scoville;
    
    const heatMeters = document.querySelectorAll('.heat-meter .bar');
    heatMeters.forEach((bar, index) => {
        if (index < product.heatScore) {
            bar.classList.add('active');
        } else {
            bar.classList.remove('active');
        }
    });

    // Populate Accords
    document.getElementById('pd-ingredients').textContent = product.ingredients;
    document.getElementById('pd-texture').textContent = product.texture;
    document.getElementById('pd-shelf').textContent = product.shelfLife;
    document.getElementById('pd-allergens').textContent = product.allergens;

    // Populate Pairings
    const pairingsContainer = document.getElementById('pd-pairings');
    pairingsContainer.innerHTML = '';
    product.pairings.forEach(pairing => {
        const div = document.createElement('div');
        div.className = 'pairing-card';
        div.innerHTML = `
            <img src="${pairing.img}" alt="${pairing.name}">
            <div class="pairing-info">
                <h4>${pairing.name}</h4>
                <p>${pairing.desc}</p>
            </div>
        `;
        pairingsContainer.appendChild(div);
    });

    // Populate Related
    const relatedContainer = document.getElementById('pd-related');
    relatedContainer.innerHTML = '';
    product.related.forEach(relId => {
        const relProd = productsData[relId];
        if (relProd) {
            const div = document.createElement('div');
            div.className = 'related-card';
            div.style.cursor = 'pointer';
            div.onclick = () => window.location.href = 'product-detail.html?id=' + relId;
            div.innerHTML = `
                <img src="${relProd.image}" alt="${relProd.name}">
                <div class="related-info">
                    <h4>${relProd.name}</h4>
                    <span class="price">${relProd.price}</span>
                    <a href="product-detail.html?id=${relId}" class="btn btn-outline" style="padding: 8px 15px; font-size: 12px; margin-top: 15px;">View Sauce</a>
                </div>
            `;
            relatedContainer.appendChild(div);
        }
    });

    // Quantity Logic
    const qtyInput = document.getElementById('qty-input');
    document.getElementById('qty-minus').addEventListener('click', () => {
        if (qtyInput.value > 1) qtyInput.value--;
    });
    document.getElementById('qty-plus').addEventListener('click', () => {
        qtyInput.value++;
    });

    // Accordions Logic
    const accordions = document.querySelectorAll('.accordion-header');
    accordions.forEach(acc => {
        acc.addEventListener('click', () => {
            const content = acc.nextElementSibling;
            const icon = acc.querySelector('i');
            if (content.style.maxHeight) {
                content.style.maxHeight = null;
                icon.className = 'fa-solid fa-plus';
            } else {
                content.style.maxHeight = content.scrollHeight + 'px';
                icon.className = 'fa-solid fa-minus';
            }
        });
    });
});
