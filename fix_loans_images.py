import re

filepath = r'c:\Users\Priya\Documents\udyog\loans.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix the loans_img.png visibility
content = re.sub(
    r'<div class="absolute lg:-right-20 lg:-top-20 opacity-30 pointer-events-none mix-blend-screen hidden lg:block" style="z-index: 0;">\s*<img src="loans_img\.png"[^>]*>\s*</div>',
    r'<div class="absolute top-10 right-0 pointer-events-none z-0 md:block opacity-50">\n          <img src="loans_img.png" alt="Premium Finance" class="w-[300px] md:w-[600px] h-auto drop-shadow-2xl" />\n      </div>',
    content
)

# 2. Add an explicit image in the left side of the Hero section so it's super visible
if "loans-hero-img" not in content:
    content = content.replace(
        '<div class="text-white gsap-reveal">',
        '<div class="text-white gsap-reveal">\n        <img src="loans_img.png" alt="Loans Finance" class="w-full max-w-sm rounded-[2rem] shadow-2xl mb-8 border border-white/10 loans-hero-img lg:hidden" />'
    )

# 3. Ensure the Unsplash image is visible (remove gsap-reveal just in case it was stuck)
content = re.sub(
    r'<img src="https://images.unsplash.com/photo-[^"]+" alt="Corporate Finance" class="([^"]*)gsap-reveal([^"]*)">',
    r'<img src="https://images.unsplash.com/photo-1542744173-8e7e53415bb0?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="Corporate Finance" class="\1\2">',
    content
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
    
print("loans.html images fixed!")
