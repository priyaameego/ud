import os
import sys

directory = r"c:\Users\Priya\Documents\udyog"

def remove_funding_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    start_marker = "<!-- Funding Top -->"
    end_marker = '<a href="benefits.html"'
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        return False
        
    end_idx = content.find(end_marker, start_idx)
    if end_idx == -1:
        return False
        
    # Find the whitespace before start_marker to keep indentation clean
    while start_idx > 0 and content[start_idx-1] in ' \t':
        start_idx -= 1
        
    # Replace the whole block with nothing
    new_content = content[:start_idx] + content[end_idx:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    return True

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html") or filename == "_new_navbar.html" or filename == "_navbar.html":
        filepath = os.path.join(directory, filename)
        if remove_funding_from_file(filepath):
            count += 1
            print(f"Removed from {filename}")

print(f"Total files updated: {count}")
