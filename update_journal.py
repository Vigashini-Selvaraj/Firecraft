import urllib.parse

html_path = r'c:\Users\vigas\Desktop\firecraft\home2.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Image 1
content = content.replace('assets/images/journal/chili-guide.jpg', 'assets/images/products/extra-hot.png')
# Replace Link 1
old_link = '<a href="#">\n                        Read Article\n                        <i class="fa-solid fa-arrow-right"></i>\n                    </a>'
title1 = urllib.parse.quote('Understanding Heat: A Guide to Chili Peppers')
img1 = urllib.parse.quote('assets/images/products/extra-hot.png')
new_link1 = f'<a href="blog-detail.html?title={title1}&image={img1}">\n                        Read Article\n                        <i class="fa-solid fa-arrow-right"></i>\n                    </a>'
content = content.replace(old_link, new_link1, 1)

# Replace Image 2
content = content.replace('assets/images/journal/sweet-vs-smoky.jpg', 'assets/images/products/deep-and-smoky.png')
# Replace Link 2
title2 = urllib.parse.quote('Sweet vs. Smoky: Choosing Your Sauce')
img2 = urllib.parse.quote('assets/images/products/deep-and-smoky.png')
new_link2 = f'<a href="blog-detail.html?title={title2}&image={img2}">\n                        Read Article\n                        <i class="fa-solid fa-arrow-right"></i>\n                    </a>'
content = content.replace(old_link, new_link2, 1)

# Replace Image 3
content = content.replace('assets/images/journal/choosing-hot-sauce.jpg', 'assets/images/products/everyday-sauce.png')
# Replace Link 3
title3 = urllib.parse.quote('The Art of Pairing Hot Sauce')
img3 = urllib.parse.quote('assets/images/products/everyday-sauce.png')
new_link3 = f'<a href="blog-detail.html?title={title3}&image={img3}">\n                        Read Article\n                        <i class="fa-solid fa-arrow-right"></i>\n                    </a>'
content = content.replace(old_link, new_link3, 1)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('JOURNAL UPDATED')
