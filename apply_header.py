import os
import re

with open('_new_navbar.html', 'r', encoding='utf-8') as f:
    new_header = f.read()

html_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('_')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace either a <nav>...</nav> block or a <header>...</header> block at the top of the body
    # Using regex to find the first <nav> or <header> and replace it
    # We will match the first occurrence
    
    nav_pattern = r'<nav.*?</nav>'
    header_pattern = r'<header.*?</header>'
    
    # Find the earliest occurrence of either
    nav_match = re.search(nav_pattern, content, flags=re.DOTALL)
    header_match = re.search(header_pattern, content, flags=re.DOTALL)
    
    match_to_replace = None
    if nav_match and header_match:
        if nav_match.start() < header_match.start():
            match_to_replace = nav_pattern
        else:
            match_to_replace = header_pattern
    elif nav_match:
        match_to_replace = nav_pattern
    elif header_match:
        match_to_replace = header_pattern
        
    if match_to_replace:
        new_content = re.sub(match_to_replace, new_header, content, count=1, flags=re.DOTALL)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        # If no nav/header, inject right after <body>
        body_pattern = r'<body.*?>'
        new_content = re.sub(body_pattern, lambda m: m.group(0) + '\n' + new_header, content, count=1, flags=re.DOTALL)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected into {file}")
