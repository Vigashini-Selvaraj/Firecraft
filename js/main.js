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
    window.initNavbar = function() {
        // Mobile Menu
        const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
        const navMenu = document.querySelector('.nav-menu');
        
        if (mobileMenuBtn && navMenu) {
            // Remove old listeners to prevent duplicates if called multiple times
            const newBtn = mobileMenuBtn.cloneNode(true);
            mobileMenuBtn.parentNode.replaceChild(newBtn, mobileMenuBtn);
            newBtn.addEventListener('click', () => {
                navMenu.classList.toggle('show');
            });
        }

        // Theme Toggle
        const themeToggleBtn = document.querySelector('.theme-toggle-btn');
        if (themeToggleBtn) {
            const newThemeBtn = themeToggleBtn.cloneNode(true);
            themeToggleBtn.parentNode.replaceChild(newThemeBtn, themeToggleBtn);
            
            // Check localStorage on load
            if (localStorage.getItem('theme') === 'light') {
                document.documentElement.classList.add('light-theme');
                document.body.classList.add('light-theme');
                const icon = newThemeBtn.querySelector('i');
                if (icon) {
                    icon.classList.remove('fa-moon');
                    icon.classList.add('fa-sun');
                }
            }
            
            newThemeBtn.addEventListener('click', () => {
                document.body.classList.toggle('light-theme');
                document.documentElement.classList.toggle('light-theme', document.body.classList.contains('light-theme'));
                const isLight = document.body.classList.contains('light-theme');
                
                // Save to localStorage
                localStorage.setItem('theme', isLight ? 'light' : 'dark');
                
                const icon = newThemeBtn.querySelector('i');
                if (icon) {
                    if (isLight) {
                        icon.classList.remove('fa-moon');
                        icon.classList.add('fa-sun');
                    } else {
                        icon.classList.remove('fa-sun');
                        icon.classList.add('fa-moon');
                    }
                }
            });
        }

        // RTL/LTR Toggle
        const dirToggleBtn = document.querySelector('.dir-toggle-btn');
        if (dirToggleBtn) {
            const newDirBtn = dirToggleBtn.cloneNode(true);
            dirToggleBtn.parentNode.replaceChild(newDirBtn, dirToggleBtn);
            newDirBtn.addEventListener('click', () => {
                const currentDir = document.documentElement.getAttribute('dir');
                if (currentDir === 'rtl') {
                    document.documentElement.setAttribute('dir', 'ltr');
                    newDirBtn.textContent = 'LTR';
                } else {
                    document.documentElement.setAttribute('dir', 'rtl');
                    newDirBtn.textContent = 'RTL';
                }
            });
        }

        // Profile Dropdown
        const profileBtn = document.querySelector('.profile-btn');
        const profileDropdown = document.querySelector('.profile-dropdown');
        
        if (profileBtn && profileDropdown) {
            const newProfileBtn = profileBtn.cloneNode(true);
            profileBtn.parentNode.replaceChild(newProfileBtn, profileBtn);
            
            newProfileBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                profileDropdown.classList.toggle('show');
            });
            
            document.addEventListener('click', (e) => {
                if (!profileDropdown.contains(e.target) && !newProfileBtn.contains(e.target)) {
                    profileDropdown.classList.remove('show');
                }
            });
        }
    };
    
    // Call it immediately for pages that might have hardcoded navbar
    window.initNavbar();

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
