import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace the topbar logo
    pattern = r'<a href="index\.html" class="flex items-center gap-3">.*?</a>'
    new_logo = '<a href="index.html" class="flex items-center">\n      <img src="logo.png" alt="Udyog Suvidha Kendra" class="h-10">\n    </a>'
    
    # regex sub with DOTALL
    new_content = re.sub(pattern, new_logo, content, flags=re.DOTALL)
    
    # Also replace mobile nav logo
    pattern2 = r'<a href="index\.html" class="font-black text-.*?UDYOG<sup.*?</a>'
    new_logo2 = '<a href="index.html" class="flex items-center">\n        <img src="logo.png" alt="Udyog" class="h-8">\n      </a>'
    new_content = re.sub(pattern2, new_logo2, new_content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)
