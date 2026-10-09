
document.addEventListener("DOMContentLoaded", () => {
    const grid = document.getElementById("recipe-grid");

    if (!grid) return;

    const cards = Array.from(grid.querySelectorAll(".recipe-card"));
    const searchInput = document.getElementById("recipe-search-input");
    const sortSelect = document.getElementById("recipe-sort");
    const resultCount = document.getElementById("recipe-result-count");
    const emptyState = document.getElementById("recipe-empty-state");
    const resetButton = document.getElementById("recipe-reset");

    const categoryButtons = Array.from(
        document.querySelectorAll(".recipe-filter")
    );

    const heatButtons = Array.from(
        document.querySelectorAll(".heat-chip")
    );

    let activeCategory = "all";
    let activeHeat = "all";

    function updateActiveButton(buttons, selectedButton) {
        buttons.forEach((button) => {
            const isActive = button === selectedButton;

            button.classList.toggle("active", isActive);
            button.setAttribute("aria-pressed", String(isActive));
        });
    }

    function getMatchingCards() {
        const query = searchInput.value.trim().toLowerCase();

        return cards.filter((card) => {
            const categories = (card.dataset.category || "").split(/\s+/);
            const heat = card.dataset.heat || "";
            const name = card.dataset.name || "";
            const searchText = card.dataset.search || "";

            const matchesCategory =
                activeCategory === "all" ||
                categories.includes(activeCategory);

            const matchesHeat =
                activeHeat === "all" || heat === activeHeat;

            const matchesSearch =
                !query ||
                name.includes(query) ||
                searchText.toLowerCase().includes(query);

            return matchesCategory && matchesHeat && matchesSearch;
        });
    }

    function renderRecipes() {
        const matches = getMatchingCards();
        const sortMode = sortSelect.value;

        matches.sort((a, b) => {
            if (sortMode === "quickest") {
                return Number(a.dataset.time) - Number(b.dataset.time);
            }

            if (sortMode === "name") {
                return (a.dataset.name || "").localeCompare(
                    b.dataset.name || ""
                );
            }

            return cards.indexOf(a) - cards.indexOf(b);
        });

        // Append matching cards in sorted order.
        // Unmatched cards are hidden but remain available for future filters.
        matches.forEach((card) => grid.appendChild(card));

        cards.forEach((card) => {
            card.hidden = !matches.includes(card);
        });

        resultCount.textContent = String(matches.length).padStart(2, "0");
        emptyState.hidden = matches.length !== 0;
        grid.hidden = matches.length === 0;
    }

    categoryButtons.forEach((button) => {
        button.addEventListener("click", () => {
            activeCategory = button.dataset.category;
            updateActiveButton(categoryButtons, button);
            renderRecipes();
        });
    });

    heatButtons.forEach((button) => {
        button.addEventListener("click", () => {
            activeHeat = button.dataset.heat;
            updateActiveButton(heatButtons, button);
            renderRecipes();
        });
    });

    searchInput.addEventListener("input", renderRecipes);
    sortSelect.addEventListener("change", renderRecipes);

    function resetFilters() {
        activeCategory = "all";
        activeHeat = "all";
        searchInput.value = "";
        sortSelect.value = "featured";

        updateActiveButton(
            categoryButtons,
            categoryButtons.find((button) => button.dataset.category === "all")
        );

        updateActiveButton(
            heatButtons,
            heatButtons.find((button) => button.dataset.heat === "all")
        );

        renderRecipes();
    }

    resetButton.addEventListener("click", resetFilters);

    document.querySelectorAll("[data-mood-category]").forEach((link) => {
        link.addEventListener("click", () => {
            const category = link.dataset.moodCategory;

            activeCategory = category;

            const button = categoryButtons.find(
                (item) => item.dataset.category === category
            );

            if (button) {
                updateActiveButton(categoryButtons, button);
            }

            renderRecipes();
        });
    });

    renderRecipes();
});