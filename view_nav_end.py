import re

with open('ayush-export-promotion-council.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'<div class="nav-bottom-row(.*?)</header>', content, re.DOTALL)
if match:
    print(match.group(0)[-1000:])
