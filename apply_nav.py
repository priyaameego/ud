import os
import re

with open('_new_navbar.html', 'r', encoding='utf-8') as f:
    new_nav = f.read()

files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('_')]

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Try to find the start of the topbar
    # The topbar always starts with either <div class="topbar or <!-- TOP BAR --> or similar
    # We will use regex to find the start of the topbar block
    # and the end of the </nav> block
    
    # Let's match from <!-- TOP BAR to </nav>
    # OR <div class="topbar to </nav>
    
    pattern1 = r'<!-- =*.*?TOP BAR.*?</nav>'
    pattern2 = r'<!-- TOP BAR -->.*?</nav>'
    pattern3 = r'<div class="topbar.*?</nav>'
    
    new_content = content
    if re.search(pattern1, new_content, flags=re.DOTALL | re.IGNORECASE):
        new_content = re.sub(pattern1, new_nav, new_content, flags=re.DOTALL | re.IGNORECASE)
    elif re.search(pattern2, new_content, flags=re.DOTALL | re.IGNORECASE):
        new_content = re.sub(pattern2, new_nav, new_content, flags=re.DOTALL | re.IGNORECASE)
    elif re.search(pattern3, new_content, flags=re.DOTALL | re.IGNORECASE):
        new_content = re.sub(pattern3, new_nav, new_content, flags=re.DOTALL | re.IGNORECASE)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)
