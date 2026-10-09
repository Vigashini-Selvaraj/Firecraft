(function applySavedTheme() {
    try {
        if (localStorage.getItem('theme') === 'light') {
            document.documentElement.classList.add('light-theme');
            if (document.body) document.body.classList.add('light-theme');
        }
    } catch (err) {
        /* ignore storage errors */
    }
})();

document.addEventListener('DOMContentLoaded', () => {
    // Dynamic Navbar & Footer Fetch Loader
    const navbarContainer = document.getElementById('navbar-container');
    if (navbarContainer) {
        // Highlight active link based on window.location
        const updateActiveNav = () => {
            const currentUrl = window.location.pathname.split('/').pop() || 'index.html';
            const navLinks = navbarContainer.querySelectorAll('.nav-menu a');
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === currentUrl) {
                    link.classList.add('active');
                }
            });
        };

        fetch('components/navbar.html')
            .then(res => {
                if (!res.ok) throw new Error('HTTP error ' + res.status);
                return res.text();
            })
            .then(data => {
                navbarContainer.innerHTML = data;
                updateActiveNav();
                if (typeof window.initNavbar === 'function') {
                    window.initNavbar();
                }
            })
            .catch(err => {
                console.warn('Navbar fetch note (using pre-rendered fallback if available):', err);
                updateActiveNav();
                if (typeof window.initNavbar === 'function') {
                    window.initNavbar();
                }
            });
    } else {
        if (typeof window.initNavbar === 'function') {
            window.initNavbar();
        }
    }


    const footerContainer = document.getElementById('footer-container');
    if (footerContainer) {
        fetch('components/footer.html')
            .then(res => {
                if (!res.ok) throw new Error('HTTP error ' + res.status);
                return res.text();
            })
            .then(data => {
                footerContainer.innerHTML = data;
            })
            .catch(err => {
                console.warn('Footer fetch note (using pre-rendered fallback if available):', err);
            });
    }


    // Heat Modal Logic
    const heatCards = document.querySelectorAll('.heat-card');
    const heatModal = document.getElementById('heatModal');
    const closeHeatModal = document.getElementById('closeHeatModal');
    const heatModalImg = document.getElementById('heatModalImg');
    const heatModalTitle = document.getElementById('heatModalTitle');
    const heatModalDots = document.getElementById('heatModalDots');
    const heatModalDesc = document.getElementById('heatModalDesc');

    const heatData = {
        'mild': {
            img: 'assets/images/heat_mild.jpg',
            title: 'Mild Heat',
            dots: '● ○ ○ ○ ○',
            desc: 'A gentle introduction to our flavors. Fresh jalapeño notes with a slight char, providing big flavor with only a whisper of heat.'
        },
        'medium': {
            img: 'assets/images/heat_medium.jpg',
            title: 'Medium Heat',
            dots: '● ● ○ ○ ○',
            desc: 'A perfectly balanced warmth. Bright, vibrant habanero peppers offer a fruity kick that builds beautifully without overwhelming the palate.'
        },
        'hot': {
            img: 'assets/images/heat_hot.jpg',
            title: 'Hot',
            dots: '● ● ● ○ ○',
            desc: 'For the experienced heat lover. Blended with bright cayenne and intense flames, this sauce leaves a fiery, lingering sting.'
        },
        'very-hot': {
            img: 'assets/images/heat_very_hot.jpg',
            title: 'Very Hot',
            dots: '● ● ● ● ○',
            desc: 'Proceed with caution. Featuring heavily blistered ghost peppers, this delivers dramatic, violent heat that takes over your senses.'
        },
        'extreme': {
            img: 'assets/images/heat_extreme.jpg',
            title: 'Extreme Heat',
            dots: '● ● ● ● ●',
            desc: 'Not for the faint of heart. Molten lava heat crafted from terrifying Carolina Reaper peppers. This is our most fierce and punishing concoction.'
        }
    };

    if (heatCards.length > 0 && heatModal) {
        heatCards.forEach(card => {
            card.addEventListener('click', (e) => {
                e.preventDefault();
                const heatLevel = card.getAttribute('data-heat');
                if (heatData[heatLevel]) {
                    heatModalImg.src = heatData[heatLevel].img;
                    heatModalTitle.textContent = heatData[heatLevel].title;
                    heatModalDots.textContent = heatData[heatLevel].dots;
                    heatModalDesc.textContent = heatData[heatLevel].desc;
                    heatModal.classList.add('show');
                }
            });
        });

        closeHeatModal.addEventListener('click', () => {
            heatModal.classList.remove('show');
        });

        heatModal.addEventListener('click', (e) => {
            if (e.target === heatModal) {
                heatModal.classList.remove('show');
            }
        });
    }
});
