import os
import re

# Read the new footer template
with open('_footer.html', 'r', encoding='utf-8') as f:
    footer_content = f.read()

# Get all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('_')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match existing footer
    footer_pattern = r'<footer.*?>.*?</footer>'
    
    if re.search(footer_pattern, content, flags=re.DOTALL):
        # Replace existing footer
        new_content = re.sub(footer_pattern, footer_content, content, count=1, flags=re.DOTALL)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Replaced footer in {file}")
    else:
        # If no footer, inject right before the GSAP script or </body>
        # Since we added GSAP script right before </body>, we can inject right before <script>\n  if (typeof lenis
        gsap_script_pattern = r'(<script>\s*if \(typeof lenis === \'undefined\')'
        if re.search(gsap_script_pattern, content):
            new_content = re.sub(gsap_script_pattern, lambda m: footer_content + '\n' + m.group(1), content, count=1)
        else:
            body_end_pattern = r'(</body>)'
            new_content = re.sub(body_end_pattern, lambda m: footer_content + '\n' + m.group(1), content, count=1)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected footer into {file}")
