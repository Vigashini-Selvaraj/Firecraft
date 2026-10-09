import re

html_path = r'c:\Users\vigas\Desktop\firecraft\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

def replace_spaces(match):
    path = match.group(0)
    return path.replace(' ', '-')

new_content = re.sub(r'assets/images/products/[^\'\"]+', replace_spaces, content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print('INDEX UPDATED')
