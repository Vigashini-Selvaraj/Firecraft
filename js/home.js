document.addEventListener('DOMContentLoaded', () => {
    // Load navbar
    fetch('components/navbar.html')
        .then(response => response.text())
        .then(data => {
            const container = document.getElementById('navbar-container');
            if (container) {
                container.innerHTML = data;
                
                // Set active class based on current URL
                const currentUrl = window.location.pathname.split('/').pop() || 'index.html';
                const navLinks = container.querySelectorAll('.nav-menu a');
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === currentUrl) {
                        link.classList.add('active');
                    }
                });

                if (typeof window.initNavbar === 'function') {
                    window.initNavbar();
                }
            }
        });

    // Load footer
    fetch('components/footer.html')
        .then(response => response.text())
        .then(data => {
            const container = document.getElementById('footer-container');
            if (container) {
                container.innerHTML = data;
            }
        });

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
            
            if(recMatchName && recResult) {
                recMatchName.textContent = sauce;
                recResult.style.display = 'block';
                recResult.style.animation = 'fadeIn 0.5s ease';
                setTimeout(() => {
                    recResult.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                }, 100);
            }
        }
    }

    function setupRecGroup(buttons, stateKey) {
        if(!buttons || !buttons.length) return;
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
});

    // Interactive Pairing Guide Logic
    const pairingTabs = document.querySelectorAll('.pairing-tab');
    const pairingPanes = document.querySelectorAll('.pairing-pane');
    
    if (pairingTabs.length > 0) {
        pairingTabs.forEach(tab => {
            tab.addEventListener('click', () => {
                // Remove active from all tabs and panes
                pairingTabs.forEach(t => t.classList.remove('active'));
                pairingPanes.forEach(p => p.classList.remove('active'));
                
                // Add active to clicked tab
                tab.classList.add('active');
                
                // Add active to corresponding pane
                const targetPane = document.getElementById('pane-' + tab.dataset.pairing);
                if (targetPane) {
                    targetPane.classList.add('active');
                }
            });
        });
    }
