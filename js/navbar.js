// FIRECRAFT NAVBAR INTERACTIVITY LOGIC

function updateThemeIcons() {
    const isLight = document.body.classList.contains("light-theme") || document.documentElement.classList.contains("light-theme");
    const themeBtns = document.querySelectorAll(".theme-toggle-btn, .theme-btn");
    themeBtns.forEach(btn => {
        const icon = btn.querySelector("i");
        if (icon) {
            icon.className = isLight ? "fa-solid fa-sun" : "fa-solid fa-moon";
        }
    });
}

function updateDirButtons() {
    const currentDir = document.documentElement.getAttribute("dir") || "ltr";
    const dirBtns = document.querySelectorAll(".dir-toggle-btn, .ltr-rtl-btn");
    dirBtns.forEach(btn => {
        btn.textContent = currentDir.toUpperCase() === "RTL" ? "RTL" : "LTR";
    });
}

window.initNavbar = () => {
    // Sync initial states
    if (localStorage.getItem("theme") === "light") {
        document.documentElement.classList.add("light-theme");
        document.body.classList.add("light-theme");
    } else if (localStorage.getItem("theme") === "dark") {
        document.documentElement.classList.remove("light-theme");
        document.body.classList.remove("light-theme");
    }
    updateThemeIcons();
    updateDirButtons();
};

// Global Delegation for all Navbar Interactions
document.addEventListener("click", (e) => {
    // 1. THEME TOGGLE BUTTON
    const themeBtn = e.target.closest(".theme-toggle-btn, .theme-btn");
    if (themeBtn) {
        e.preventDefault();
        e.stopPropagation();

        const isLight = document.body.classList.contains("light-theme") || document.documentElement.classList.contains("light-theme");
        if (isLight) {
            document.body.classList.remove("light-theme");
            document.documentElement.classList.remove("light-theme");
            localStorage.setItem("theme", "dark");
        } else {
            document.body.classList.add("light-theme");
            document.documentElement.classList.add("light-theme");
            localStorage.setItem("theme", "light");
        }
        updateThemeIcons();
        return;
    }

    // 2. LTR / RTL DIRECTION TOGGLE BUTTON
    const dirBtn = e.target.closest(".dir-toggle-btn, .ltr-rtl-btn");
    if (dirBtn) {
        e.preventDefault();
        e.stopPropagation();

        const currentDir = document.documentElement.getAttribute("dir") || "ltr";
        const newDir = currentDir.toLowerCase() === "rtl" ? "ltr" : "rtl";
        document.documentElement.setAttribute("dir", newDir);
        updateDirButtons();
        return;
    }

    // 3. PROFILE DROPDOWN BUTTON
    const profileBtn = e.target.closest(".profile-btn");
    if (profileBtn) {
        e.preventDefault();
        e.stopPropagation();
        const container = profileBtn.closest(".profile-dropdown-container, .dropdown");
        if (container) {
            const dropdown = container.querySelector(".profile-dropdown, .dropdown-content");
            if (dropdown) {
                dropdown.classList.toggle("show");
            }
        }
        return;
    }

    // Close profile dropdown if clicked outside
    const dropdowns = document.querySelectorAll(".profile-dropdown.show, .dropdown-content.show");
    dropdowns.forEach(dd => {
        if (!dd.contains(e.target)) {
            dd.classList.remove("show");
        }
    });

    // 4. MOBILE HAMBURGER MENU BUTTON
    const mobileBtn = e.target.closest(".mobile-menu-btn, .hamburger-btn");
    if (mobileBtn) {
        e.preventDefault();
        e.stopPropagation();
        const navMenu = document.querySelector(".nav-menu, .nav-center");
        if (navMenu) {
            navMenu.classList.toggle("show");
        }
        return;
    }

    // Close mobile nav menu when clicking outside or clicking a menu link
    const navMenu = document.querySelector(".nav-menu.show, .nav-center.show");
    if (navMenu) {
        if (e.target.closest("a") || !navMenu.contains(e.target)) {
            navMenu.classList.remove("show");
        }
    }
});

// Run init on ready
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", window.initNavbar);
} else {
    window.initNavbar();
}