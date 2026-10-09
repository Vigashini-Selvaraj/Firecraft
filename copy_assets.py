import os, shutil

os.makedirs('assets/images/products', exist_ok=True)
os.makedirs('assets/images/flavors', exist_ok=True)
os.makedirs('assets/images/recipes', exist_ok=True)

src = 'assets/images/'
dst = 'assets/images/'

copies = {
    'sauce_smoked_red_1791369304097.jpg': 'products/classic-hot-sauce.jpg',
    'sauce_citrus_heat_1791369327864.jpg': 'products/mango-habanero.jpg',
    'sauce_fire_roast_1791369316199.jpg': 'products/chipotle-bbq.jpg',
    'product_sauces_1791360804955.jpg': 'products/garlic-chili.jpg',
    
    'product_gifts_1791360842749.jpg': 'flavors/sweet.jpg',
    'product_spices_1791360831178.jpg': 'flavors/smoky.jpg',
    'product_condiments_1791360816664.jpg': 'flavors/garlic.jpg',
    'sauce_citrus_heat_1791369327864.jpg': ['flavors/fruity.jpg', 'flavors/citrus.jpg'],
    'sauce_smoked_red_1791369304097.jpg': 'flavors/tangy.jpg',
    
    'story_image_1791360872524.jpg': ['ingredients.jpg', 'recipes/hot-honey-pizza.jpg'],
    'hero_bg_1791360790229.jpg': 'our-story.jpg',
    
    'recipe_wings_1791360856984.jpg': ['recipes/chicken-tacos.jpg', 'recipes/fire-wings.jpg'],
    'product_spices_1791360831178.jpg': 'recipes/chili-noodles.jpg',
    'firecraft_logo.png': 'pepper.png'
}

for source, targets in copies.items():
    if isinstance(targets, str):
        targets = [targets]
    for target in targets:
        shutil.copy(src + source, dst + target)
