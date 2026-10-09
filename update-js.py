import re

# Update JS for 3 pairings
with open('js/product-detail.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Add a 3rd pairing to Classic Hot Sauce
js_content = js_content.replace(
    "{ name: 'Breakfast Eggs', desc: 'Wake up your morning scramble.', img: 'assets/images/products/Chilli-Garlic-Noodles.png' }",
    "{ name: 'Breakfast Eggs', desc: 'Wake up your morning scramble.', img: 'assets/images/products/Chilli-Garlic-Noodles.png' },\n            { name: 'Avocado Toast', desc: 'A dash of zesty heat to start the day.', img: 'assets/images/products/everyday-sauce.png' }"
)

# Mango Habanero
js_content = js_content.replace(
    "{ name: 'Tacos', desc: 'Elevates fish and pork tacos instantly.', img: 'assets/images/products/Spicy-Chicken-Tacos.png' }",
    "{ name: 'Tacos', desc: 'Elevates fish and pork tacos instantly.', img: 'assets/images/products/Spicy-Chicken-Tacos.png' },\n            { name: 'Shrimp Skewers', desc: 'Perfect tropical glaze for seafood.', img: 'assets/images/sauce_smoked_red_1791369304097.jpg' }"
)

# Chipotle BBQ
js_content = js_content.replace(
    "{ name: 'Burgers', desc: 'Mix into mayo or spread directly.', img: 'assets/images/products/Fire-Wings.png' }",
    "{ name: 'Burgers', desc: 'Mix into mayo or spread directly.', img: 'assets/images/products/Fire-Wings.png' },\n            { name: 'Pulled Pork', desc: 'Smoky, earthy depth for slow-cooked meats.', img: 'assets/images/products/Chipotle-BBQ-Sauce.png' }"
)

# Garlic Chili
js_content = js_content.replace(
    "{ name: 'Dumplings', desc: 'The perfect dipping companion.', img: 'assets/images/products/Spicy-Chicken-Tacos.png' }",
    "{ name: 'Dumplings', desc: 'The perfect dipping companion.', img: 'assets/images/products/Spicy-Chicken-Tacos.png' },\n            { name: 'Fried Rice', desc: 'An umami explosion for wok-tossed dishes.', img: 'assets/images/products/Garlic-Chili-Sauce.png' }"
)

# Ghost Pepper
js_content = js_content.replace(
    "{ name: 'Chili & Stews', desc: 'Add one drop to a pot for huge heat.', img: 'assets/images/sauce_smoked_red_1791369304097.jpg' }",
    "{ name: 'Chili & Stews', desc: 'Add one drop to a pot for huge heat.', img: 'assets/images/sauce_smoked_red_1791369304097.jpg' },\n            { name: 'Bravest Burgers', desc: 'Mix into a fiery aioli if you dare.', img: 'assets/images/products/extra-hot.png' }"
)

# Smoked Jalapeno
js_content = js_content.replace(
    "{ name: 'Eggs', desc: 'A smoky start to your morning.', img: 'assets/images/products/Hot-Honey-Pizza.png' }",
    "{ name: 'Eggs', desc: 'A smoky start to your morning.', img: 'assets/images/products/Hot-Honey-Pizza.png' },\n            { name: 'Grilled Veggies', desc: 'Adds a campfire depth to zucchini and peppers.', img: 'assets/images/products/deep-and-smoky.png' }"
)

# Pineapple Habanero
js_content = js_content.replace(
    "{ name: 'Seafood', desc: 'Perfect on grilled fish or shrimp tacos.', img: 'assets/images/products/Spicy-Chicken-Tacos.png' }",
    "{ name: 'Seafood', desc: 'Perfect on grilled fish or shrimp tacos.', img: 'assets/images/products/Spicy-Chicken-Tacos.png' },\n            { name: 'Pork Chops', desc: 'Sweet, tropical acidity cuts through the richness.', img: 'assets/images/products/Fruit-Forward.png' }"
)

# The Daily Blaze
js_content = js_content.replace(
    "{ name: 'Sandwiches', desc: 'Mix into mayo for a spicy spread.', img: 'assets/images/products/Hot-Honey-Pizza.png' }",
    "{ name: 'Sandwiches', desc: 'Mix into mayo for a spicy spread.', img: 'assets/images/products/Hot-Honey-Pizza.png' },\n            { name: 'Roasted Potatoes', desc: 'A bright, zesty drizzle for crispy sides.', img: 'assets/images/products/everyday-sauce.png' }"
)

with open('js/product-detail.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
