window.initNavbar = () => {
    // Mobile menu toggle
    const hamburger = document.querySelector(".hamburger-btn") || document.querySelector(".mobile-menu-btn");
    const navCenter = document.querySelector(".nav-center") || document.querySelector(".nav-menu");

    if (hamburger && navCenter) {
        const newHamburger = hamburger.cloneNode(true);
        hamburger.parentNode.replaceChild(newHamburger, hamburger);

        newHamburger.addEventListener("click", () => {
            navCenter.classList.toggle("show");
            if (navCenter.style.display === "flex") {
                navCenter.style.display = "";
            } else if (window.innerWidth <= 900) {
                navCenter.style.display = "flex";
                navCenter.style.flexDirection = "column";
                navCenter.style.position = "absolute";
                navCenter.style.top = "80px";
                navCenter.style.left = "0";
                navCenter.style.width = "100%";
                navCenter.style.backgroundColor = "#080808";
                navCenter.style.padding = "20px";
                navCenter.style.borderBottom = "1px solid rgba(255,255,255,0.14)";
            }
        });
    }

    // Profile dropdown
    const profileBtn = document.querySelector(".profile-btn");
    const dropdownContent = document.querySelector(".dropdown-content") || document.querySelector(".profile-dropdown");

    if (profileBtn && dropdownContent) {
        const newProfileBtn = profileBtn.cloneNode(true);
        profileBtn.parentNode.replaceChild(newProfileBtn, profileBtn);

        newProfileBtn.addEventListener("click", (e) => {
            e.stopPropagation();
            dropdownContent.classList.toggle("show");
        });

        document.addEventListener("click", (e) => {
            if (
                !newProfileBtn.contains(e.target) &&
                !dropdownContent.contains(e.target)
            ) {
                dropdownContent.classList.remove("show");
            }
        });
    }

    // THEME TOGGLE
    const themeBtn = document.querySelector(".theme-toggle-btn") || document.querySelector(".theme-btn");

    if (themeBtn) {
        const newThemeBtn = themeBtn.cloneNode(true);
        themeBtn.parentNode.replaceChild(newThemeBtn, themeBtn);

        const updateThemeIcon = () => {
            const isLight = document.body.classList.contains("light-theme");
            const icon = newThemeBtn.querySelector("i");
            if (icon) {
                icon.className = isLight ? "fa-solid fa-sun" : "fa-solid fa-moon";
            }
        };

        if (localStorage.getItem("theme") === "light") {
            document.documentElement.classList.add("light-theme");
            document.body.classList.add("light-theme");
        }
        updateThemeIcon();

        newThemeBtn.addEventListener("click", () => {
            document.body.classList.toggle("light-theme");
            document.documentElement.classList.toggle("light-theme", document.body.classList.contains("light-theme"));
            const isLight = document.body.classList.contains("light-theme");
            localStorage.setItem("theme", isLight ? "light" : "dark");
            updateThemeIcon();
        });
    }

    // LTR / RTL toggle
    const ltrRtlBtn = document.querySelector(".ltr-rtl-btn") || document.querySelector(".dir-toggle-btn");

    if (ltrRtlBtn) {
        const newLtrRtlBtn = ltrRtlBtn.cloneNode(true);
        ltrRtlBtn.parentNode.replaceChild(newLtrRtlBtn, ltrRtlBtn);

        newLtrRtlBtn.addEventListener("click", () => {
            const currentDir = document.documentElement.getAttribute("dir");
            const ltrText = newLtrRtlBtn.querySelector(".ltr-text") || newLtrRtlBtn;

            if (currentDir === "rtl") {
                document.documentElement.setAttribute("dir", "ltr");
                if (ltrText.querySelector) {
                    const span = ltrText.querySelector(".ltr-text");
                    if (span) span.textContent = "LTR";
                    else ltrText.textContent = "LTR";
                } else {
                    ltrText.textContent = "LTR";
                }
            } else {
                document.documentElement.setAttribute("dir", "rtl");
                if (ltrText.querySelector) {
                    const span = ltrText.querySelector(".ltr-text");
                    if (span) span.textContent = "RTL";
                    else ltrText.textContent = "RTL";
                } else {
                    ltrText.textContent = "RTL";
                }
            }
        });
    }
};

// Initialize navbar
if (
    document.readyState === "complete" ||
    document.readyState === "interactive"
) {
    if (document.querySelector(".nav-container") || document.querySelector(".navbar")) {
        window.initNavbar();
    }
} else {
    document.addEventListener("DOMContentLoaded", () => {
        if (document.querySelector(".nav-container") || document.querySelector(".navbar")) {
            window.initNavbar();
        }
    });
}