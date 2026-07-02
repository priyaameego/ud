import os
import re

with open('_new_navbar.html', 'r', encoding='utf-8') as f:
    mega_navbar = f.read()

html_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('_')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_header = mega_navbar

    # Try matching the comment block first
    start_match = re.search(r'<!-- =+\s*(PREMIUM TWO-TIER NAVBAR|INNER PAGE NAVBAR)', content)
    if start_match:
        start_idx = start_match.start()
        end_match = re.search(r'</header>', content[start_idx:])
        if end_match:
            end_idx = start_idx + end_match.end()
            new_content = content[:start_idx] + new_header + content[end_idx:]
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Clean updated {file} (using comment block)")
            continue
            
    # If no comment block, try to find <header> tag
    header_match = re.search(r'<header.*?</header>', content, flags=re.DOTALL)
    if header_match:
        new_content = content[:header_match.start()] + new_header + content[header_match.end():]
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Clean updated {file} (using header tag)")
    else:
        print(f"Could not find exact block in {file}, skipping for now")
