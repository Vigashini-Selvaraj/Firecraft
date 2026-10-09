import os

js_content = '''

    // Recommendation UI Logic
    const recFlavors = document.querySelectorAll('#rec-flavor .rec-btn');
    const recFoods = document.querySelectorAll('#rec-food .rec-btn');
    const recHeats = document.querySelectorAll('#rec-heat .rec-btn');
    const recResult = document.getElementById('rec-result');
    const recMatchName = document.getElementById('rec-match-name');

    let state = { flavor: null, food: null, heat: null };

    function checkRecommendation() {
        if (state.flavor && state.food && state.heat) {
            let sauce = 'SMOKED RED';
            if (state.heat === 'extra hot') sauce = 'FIRE ROAST';
            if (state.flavor === 'tangy' || state.flavor === 'sweet') sauce = 'CITRUS HEAT';
            if (state.flavor === 'fiery' && state.heat === 'mild') sauce = 'EVERYDAY HEAT';
            
            recMatchName.textContent = sauce;
            recResult.style.display = 'block';
            recResult.style.animation = 'fadeIn 0.5s ease';
            
            // Re-trigger scroll if already in view or smooth scroll down slightly
            setTimeout(() => {
                recResult.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }, 100);
        }
    }

    function setupRecGroup(buttons, stateKey) {
        buttons.forEach(btn => {
            btn.addEventListener('click', () => {
                buttons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                state[stateKey] = btn.textContent.toLowerCase();
                checkRecommendation();
            });
        });
    }

    setupRecGroup(recFlavors, 'flavor');
    setupRecGroup(recFoods, 'food');
    setupRecGroup(recHeats, 'heat');

    // Newsletter Validation
    const newsletterForm = document.getElementById('newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const input = newsletterForm.querySelector('input');
            if (input.value) {
                alert('Welcome to the FireCraft community!');
                input.value = '';
            }
        });
    }

'''

with open('js/home.js', 'r', encoding='utf-8') as f:
    content = f.read()

# insert before last closing brace
content = content.replace('});\n', js_content + '\n});\n')

with open('js/home.js', 'w', encoding='utf-8') as f:
    f.write(content)
