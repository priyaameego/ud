import os
import re

with open('_new_navbar.html', 'r', encoding='utf-8') as f:
    mega_navbar = f.read()

html_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('_')]

for file in html_files:
    # Read the file
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace everything from the very first '<header'
    # to the very LAST '</header>' in the file.
    # This removes all the duplicated garbage headers.
    
    start_idx = content.find('<header')
    end_idx = content.rfind('</header>')
    
    if start_idx != -1 and end_idx != -1:
        # The end_idx is the start of '</header>', so we add len('</header>')
        end_idx += len('</header>')
        
        new_content = content[:start_idx] + mega_navbar + content[end_idx:]
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Force cleaned {file}")
    else:
        print(f"Skipping {file}, no header found.")
