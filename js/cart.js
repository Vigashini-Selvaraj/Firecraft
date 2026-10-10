
/* =====================================================
   FIRECRAFT CART LOGIC
   Demo checkout — no real payment processing
===================================================== */

document.addEventListener("DOMContentLoaded", () => {
    const CART_KEY = "firecraftCart";
    const ORDERS_KEY = "firecraftOrders";
    const PROMO_KEY = "firecraftPromo";

    const TAX_RATE = 0.08;
    const SHIPPING = {
        standard: 99,
        express: 199,
        pickup: 0
    };

    const DEMO_PRODUCTS = [
        {
            id: "classic-hot-sauce",
            name: "Classic Hot Sauce",
            description: "Tangy · Bold · Savory",
            price: 8.99,
            heat: 3,
            image: "assets/images/products/Classic-Hot-Sauce.png",
            quantity: 1
        },
        {
            id: "mango-habanero",
            name: "Mango Habanero",
            description: "Fruity · Sweet · Fiery",
            price: 11.99,
            heat: 4,
            image: "assets/images/products/Mango-Habanero-Hot-Sauce.png",
            quantity: 1
        },
        {
            id: "chipotle-bbq",
            name: "Chipotle BBQ",
            description: "Smoky · Rich · Sweet",
            price: 10.99,
            heat: 3,
            image: "assets/images/products/Chipotle-BBQ-Sauce.png",
            quantity: 1
        }
    ];

    const $ = (selector) => document.querySelector(selector);

    const cartItemsEl = $("#cart-items");
    const emptyCartEl = $("#empty-cart");
    const cartCountEl = $("#cart-count");
    const promoInput = $("#promo-code");
    const promoMessage = $("#promo-message");
    const promoArea = $("#promo-area");
    const discountRow = $("#discount-row");
    const paymentNote = $("#online-payment-note");
    const placeOrderBtn = $("#place-order");
    const successSection = $("#order-success");

    let cart = loadCart();
    let promoApplied = false;
    let promoDiscount = 0;

    /* -----------------------------------------
       STORAGE
    ----------------------------------------- */

    function readJSON(key, fallback) {
        try {
            const value = localStorage.getItem(key);
            return value ? JSON.parse(value) : fallback;
        } catch {
            return fallback;
        }
    }

    function saveJSON(key, value) {
        try {
            localStorage.setItem(key, JSON.stringify(value));
            return true;
        } catch {
            showMessage(
                "Your browser could not save this information. Check your storage settings.",
                "error"
            );
            return false;
        }
    }

    function loadCart() {
        const stored = readJSON(CART_KEY, null);

        // Show sample products only when the cart has never been saved.
        if (stored === null) {
            return DEMO_PRODUCTS.map(item => ({ ...item }));
        }

        if (!Array.isArray(stored)) {
            return [];
        }

        return stored
            .filter(item =>
                item &&
                item.id != null &&
                typeof item.name === "string" &&
                Number.isFinite(Number(item.price)) &&
                Number(item.price) >= 0
            )
            .map(item => ({
                ...item,
                id: String(item.id),
                price: Number(item.price),
                quantity: Math.min(
                    99,
                    Math.max(1, Math.floor(Number(item.quantity) || 1))
                ),
                heat: Math.min(
                    5,
                    Math.max(0, Math.floor(Number(item.heat) || 0))
                ),
                image: typeof item.image === "string"
                    ? item.image
                    : ""
            }));
    }

    function persistCart() {
        return saveJSON(CART_KEY, cart);
    }

    function money(amount) {
        return new Intl.NumberFormat("en-IN", {
            style: "currency",
            currency: "INR",
            minimumFractionDigits: 2
        }).format(amount);
    }

    /* -----------------------------------------
       CART TOTALS
    ----------------------------------------- */

    function subtotal() {
        return cart.reduce(
            (sum, item) => sum + item.price * item.quantity,
            0
        );
    }

    function getShipping() {
        const selected = document.querySelector(
            'input[name="shipping"]:checked'
        );

        return SHIPPING[selected?.value] ?? SHIPPING.standard;
    }

    function getDiscount() {
        return promoApplied
            ? Math.round(subtotal() * 0.10 * 100) / 100
            : 0;
    }

    function getTax() {
        return Math.round(
            Math.max(0, subtotal() - getDiscount()) * TAX_RATE * 100
        ) / 100;
    }

    function getTotal() {
        return Math.max(
            0,
            subtotal() - getDiscount() + getShipping() + getTax()
        );
    }

    /* -----------------------------------------
       RENDER PRODUCTS
    ----------------------------------------- */

    function renderCart() {
        cartItemsEl.replaceChildren();

        const totalItems = cart.reduce(
            (sum, item) => sum + item.quantity,
            0
        );

        cartCountEl.textContent = `(${totalItems})`;

        emptyCartEl.hidden = cart.length > 0;
        cartItemsEl.hidden = cart.length === 0;
        promoArea.hidden = cart.length === 0;
        placeOrderBtn.disabled = cart.length === 0;

        cart.forEach(item => {
            const row = document.createElement("article");
            row.className = "cart-item";

            const imageBox = document.createElement("div");
            imageBox.className = "cart-item-image";

            const image = document.createElement("img");
            image.src = item.image || "assets/images/firecraft_logo.png";
            image.alt = item.name;
            image.loading = "lazy";
            image.onerror = () => {
                image.onerror = null;
                image.src = "assets/images/firecraft_logo.png";
            };
            imageBox.appendChild(image);

            const info = document.createElement("div");
            info.className = "cart-item-info";

            const title = document.createElement("h3");
            title.textContent = item.name;

            const description = document.createElement("p");
            description.textContent = item.description || "Firecraft signature flavor";

            const heat = document.createElement("div");
            heat.className = "cart-item-heat";

            const dots = document.createElement("span");
            dots.className = "dots";
            dots.textContent =
                "● ".repeat(item.heat) + "○ ".repeat(5 - item.heat);

            const heatText = document.createElement("span");
            heatText.textContent = `${item.heat}/5 heat`;

            heat.append(dots, heatText);

            const price = document.createElement("strong");
            price.className = "cart-item-price";
            price.textContent = money(item.price * item.quantity);

            info.append(title, description, heat, price);

            const controls = document.createElement("div");
            controls.className = "cart-item-controls";

            const quantity = document.createElement("div");
            quantity.className = "quantity-control";
            quantity.setAttribute("aria-label", `Quantity for ${item.name}`);

            const decrease = document.createElement("button");
            decrease.type = "button";
            decrease.textContent = "−";
            decrease.setAttribute("aria-label", "Decrease quantity");
            decrease.disabled = item.quantity <= 1;

            decrease.addEventListener("click", () => {
                if (item.quantity > 1) {
                    item.quantity--;
                    updateCart();
                }
            });

            const quantityText = document.createElement("span");
            quantityText.textContent = item.quantity;
            quantityText.setAttribute("aria-live", "polite");

            const increase = document.createElement("button");
            increase.type = "button";
            increase.textContent = "+";
            increase.setAttribute("aria-label", "Increase quantity");
            increase.disabled = item.quantity >= 99;

            increase.addEventListener("click", () => {
                if (item.quantity < 99) {
                    item.quantity++;
                    updateCart();
                }
            });

            quantity.append(decrease, quantityText, increase);

            const remove = document.createElement("button");
            remove.type = "button";
            remove.className = "remove-item";
            remove.innerHTML = '<i class="fa-regular fa-trash-can"></i><span>Remove</span>';
            remove.setAttribute("aria-label", `Remove ${item.name}`);

            remove.addEventListener("click", () => {
                cart = cart.filter(product => product.id !== item.id);
                updateCart();
            });

            controls.append(quantity, remove);
            row.append(imageBox, info, controls);
            cartItemsEl.appendChild(row);
        });

        updateSummary();
    }

    function updateCart() {
        if (!persistCart()) return;
        renderCart();
    }

    /* -----------------------------------------
       ORDER SUMMARY
    ----------------------------------------- */

    function updateSummary() {
        const sub = subtotal();
        const discount = getDiscount();
        const shipping = getShipping();
        const tax = getTax();
        const total = getTotal();

        $("#summary-subtotal").textContent = money(sub);
        $("#summary-discount").textContent = `−${money(discount)}`;
        $("#summary-shipping").textContent = money(shipping);
        $("#summary-tax").textContent = money(tax);
        $("#summary-total").textContent = money(total);

        discountRow.hidden = discount <= 0;

        document.querySelectorAll("[data-shipping-price]").forEach(el => {
            const key = el.dataset.shippingPrice;
            el.textContent = money(SHIPPING[key]);
        });

        if (promoApplied && sub === 0) {
            promoApplied = false;
            promoDiscount = 0;
            discountRow.hidden = true;
        }

        placeOrderBtn.disabled = cart.length === 0;
    }

    /* -----------------------------------------
       PROMO CODE
       Demo code: FIRE10
    ----------------------------------------- */

    $("#apply-promo").addEventListener("click", () => {
        const code = promoInput.value.trim().toUpperCase();

        if (!cart.length) {
            showPromoMessage("Add products before applying a coupon.", "error");
            return;
        }

        if (code === "FIRE10") {
            promoApplied = true;
            promoDiscount = 10;
            updateSummary();

            showPromoMessage(
                `Success! 10% off — you saved ${money(getDiscount())}.`,
                "success"
            );
        } else {
            promoApplied = false;
            promoDiscount = 0;
            updateSummary();
            showPromoMessage("That coupon code isn't valid.", "error");
        }
    });

    promoInput.addEventListener("keydown", event => {
        if (event.key === "Enter") {
            event.preventDefault();
            $("#apply-promo").click();
        }
    });

    function showPromoMessage(message, type) {
        promoMessage.textContent = message;
        promoMessage.className = `form-message ${type}`;
    }

    /* -----------------------------------------
       DELIVERY & PAYMENT SELECTION
    ----------------------------------------- */

    document.querySelectorAll('input[name="shipping"]').forEach(input => {
        input.addEventListener("change", () => {
            document.querySelectorAll('input[name="shipping"]').forEach(radio => {
                radio.closest(".choice-card").classList.toggle(
                    "selected",
                    radio.checked
                );
            });

            updateSummary();
        });
    });

    document.querySelectorAll('input[name="payment"]').forEach(input => {
        input.addEventListener("change", () => {
            document.querySelectorAll('input[name="payment"]').forEach(radio => {
                radio.closest(".choice-card").classList.toggle(
                    "selected",
                    radio.checked
                );
            });

            const payment = document.querySelector(
                'input[name="payment"]:checked'
            )?.value;

            paymentNote.hidden = payment === "cod";
        });
    });

    /* -----------------------------------------
       CHECKOUT
    ----------------------------------------- */

    placeOrderBtn.addEventListener("click", () => {
        if (!cart.length) {
            alert("Your cart is empty. Add a sauce before checking out.");
            return;
        }

        const form = $("#delivery-form");

        if (!form.reportValidity()) {
            form.querySelector(":invalid")?.focus();
            $("#delivery-details").scrollIntoView({
                behavior: "smooth",
                block: "center"
            });
            return;
        }

        const payment = document.querySelector(
            'input[name="payment"]:checked'
        )?.value || "cod";

        if (payment !== "cod") {
            paymentNote.hidden = false;
            paymentNote.scrollIntoView({
                behavior: "smooth",
                block: "center"
            });

            alert(
                "Online payments are not connected yet. Choose Cash on Delivery for the demo checkout, or integrate a payment gateway before enabling online orders."
            );
            return;
        }

        const formData = new FormData(form);
        const delivery = Object.fromEntries(formData.entries());

        const orderId = "FC" + Date.now().toString().slice(-8);

        const order = {
            id: orderId,
            createdAt: new Date().toISOString(),
            status: "Order Placed",
            paymentMethod: "Cash on Delivery",
            paymentStatus: "Pay on delivery",
            deliveryOption: document.querySelector(
                'input[name="shipping"]:checked'
            )?.value || "standard",
            customer: delivery,
            items: cart.map(item => ({ ...item })),
            subtotal: subtotal(),
            discount: getDiscount(),
            shipping: getShipping(),
            tax: getTax(),
            total: getTotal(),
            currency: "INR"
        };

        const orders = readJSON(ORDERS_KEY, []);

        if (!Array.isArray(orders)) {
            alert("Unable to access saved orders. Please refresh and try again.");
            return;
        }

        orders.push(order);

        if (!saveJSON(ORDERS_KEY, orders)) return;

        $("#success-order-id").textContent = orderId;
        $("#success-message").textContent =
            `Your order total is ${money(order.total)}. ` +
            "Payment is due upon delivery. This is a local demo confirmation, not a dispatched order.";

        successSection.hidden = false;
        successSection.scrollIntoView({
            behavior: "smooth",
            block: "center"
        });

        // Clear the saved cart only after the demo order is saved.
        cart = [];

        if (!persistCart()) {
            alert("The order was saved, but the cart could not be cleared.");
        }

        renderCart();

        // Prevent duplicate submissions on the current confirmation view.
        placeOrderBtn.disabled = true;
    });

    $("#continue-after-order").addEventListener("click", () => {
        window.location.href = "products.html";
    });

    /* -----------------------------------------
       LOCAL DEMO ORDER TRACKING
    ----------------------------------------- */

    $("#track-form").addEventListener("submit", event => {
        event.preventDefault();

        const id = $("#tracking-id").value.trim().toUpperCase();
        const result = $("#tracking-result");

        result.replaceChildren();
        result.className = "tracking-result";

        const orders = readJSON(ORDERS_KEY, []);
        const order = Array.isArray(orders)
            ? orders.find(item => item.id.toUpperCase() === id)
            : null;

        if (!order) {
            result.classList.add("error");
            result.textContent =
                "No locally saved demo order was found with that reference. Live tracking requires your backend order records.";
            return;
        }

        result.classList.add("success");

        const title = document.createElement("strong");
        title.textContent = order.status;

        const details = document.createElement("p");
        details.textContent =
            `Order ${order.id} · ${money(order.total)} · ` +
            `${order.deliveryOption} delivery`;

        const payment = document.createElement("p");
        payment.textContent = `Payment: ${order.paymentStatus}`;

        const date = document.createElement("p");
        date.textContent =
            `Created: ${new Date(order.createdAt).toLocaleString()}`;

        result.append(title, details, payment, date);
    });

    /* -----------------------------------------
       WISHLIST LOGIC
    ----------------------------------------- */
    const WISHLIST_KEY = "firecraftWishlist";
    let wishlist = readJSON(WISHLIST_KEY, []);
    const wishlistSection = $("#wishlist-section");
    const wishlistItemsEl = $("#wishlist-items");

    function renderWishlist() {
        if (!wishlistSection || !wishlistItemsEl) return;
        
        if (!wishlist || wishlist.length === 0) {
            wishlistSection.style.display = "none";
            return;
        }
        
        wishlistSection.style.display = "block";
        wishlistItemsEl.replaceChildren();

        wishlist.forEach(item => {
            const row = document.createElement("article");
            row.className = "cart-item";

            const imageBox = document.createElement("div");
            imageBox.className = "cart-item-image";

            const image = document.createElement("img");
            image.src = item.image || "assets/images/firecraft_logo.png";
            image.alt = item.name;
            image.loading = "lazy";
            imageBox.appendChild(image);

            const info = document.createElement("div");
            info.className = "cart-item-info";

            const title = document.createElement("h3");
            title.textContent = item.name;

            const heat = document.createElement("div");
            heat.className = "cart-item-heat";
            const dots = document.createElement("span");
            dots.className = "dots";
            dots.textContent = "● ".repeat(item.heat || 0) + "○ ".repeat(5 - (item.heat || 0));
            heat.append(dots);

            const price = document.createElement("strong");
            price.className = "cart-item-price";
            price.textContent = money(item.price);

            info.append(title, heat, price);

            const controls = document.createElement("div");
            controls.className = "cart-item-controls";

            const addBtn = document.createElement("button");
            addBtn.className = "cart-btn cart-btn-primary";
            addBtn.innerHTML = 'Add to Cart <i class="fa-solid fa-cart-shopping"></i>';
            addBtn.style.padding = "10px 15px";
            addBtn.style.fontSize = "13px";
            addBtn.onclick = () => {
                // Add to cart
                const existing = cart.find(c => String(c.id) === String(item.id));
                if (existing) {
                    existing.quantity += 1;
                } else {
                    cart.push({ ...item, quantity: 1 });
                }
                persistCart();
                
                // Remove from wishlist
                wishlist = wishlist.filter(w => String(w.id) !== String(item.id));
                saveJSON(WISHLIST_KEY, wishlist);
                
                renderCart();
                renderWishlist();
            };

            const removeBtn = document.createElement("button");
            removeBtn.className = "remove-btn";
            removeBtn.innerHTML = '<i class="fa-regular fa-trash-can"></i> Remove';
            removeBtn.onclick = () => {
                wishlist = wishlist.filter(w => String(w.id) !== String(item.id));
                saveJSON(WISHLIST_KEY, wishlist);
                renderWishlist();
            };

            const actionsDiv = document.createElement("div");
            actionsDiv.style.display = "flex";
            actionsDiv.style.flexDirection = "column";
            actionsDiv.style.gap = "10px";
            actionsDiv.style.alignItems = "flex-end";
            actionsDiv.append(addBtn, removeBtn);

            controls.appendChild(actionsDiv);
            
            row.append(imageBox, info, controls);
            wishlistItemsEl.appendChild(row);
        });
    }

    /* -----------------------------------------
       INITIAL RENDER
    ----------------------------------------- */

    renderWishlist();
    renderCart();
});
