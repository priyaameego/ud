import os
import re

def update_file(filepath, img_name):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add the CSS animation styles just before </head> or <style>
    style_block = """
<style>
@keyframes floatForm {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-12px); }
  100% { transform: translateY(0px); }
}
@keyframes glowForm {
  0% { box-shadow: 0 0 15px rgba(79, 70, 229, 0.2), 0 20px 40px rgba(0,0,0,0.4); }
  50% { box-shadow: 0 0 40px rgba(79, 70, 229, 0.6), 0 30px 60px rgba(0,0,0,0.6); }
  100% { box-shadow: 0 0 15px rgba(79, 70, 229, 0.2), 0 20px 40px rgba(0,0,0,0.4); }
}
.premium-form-anim {
  animation: floatForm 6s ease-in-out infinite, glowForm 4s ease-in-out infinite;
  border: 1px solid rgba(255,255,255,0.1) !important;
}
</style>
"""
    if "premium-form-anim" not in content:
        if "</head>" in content:
            content = content.replace("</head>", style_block + "\n</head>")
        else:
            content = style_block + "\n" + content

    # 2. Find the form container and add the premium-form-anim class
    # The form container has classes like: "bg-white rounded-[2rem] p-8 md:p-10 shadow-2xl relative max-w-md w-full mx-auto lg:ml-auto gsap-reveal reveal-scale"
    # or "bg-white/10 backdrop-blur-xl border border-white/20 rounded-[2rem] p-8 md:p-10 shadow-2xl relative max-w-md w-full mx-auto lg:ml-auto gsap-reveal reveal-scale"
    
    form_pattern = r'(<div[^>]*class="[^"]*max-w-md[^"]*mx-auto lg:ml-auto[^"]*)"'
    content = re.sub(form_pattern, r'\1 premium-form-anim"', content)
    
    # 3. Add the image to the hero section.
    # We can add it as a background image overlay, or position it absolutely behind the form.
    # Let's add it behind the form.
    # Find the form div again, and insert the image div right before it.
    
    img_element = f"""
      <!-- Premium Illustration -->
      <div class="absolute lg:-right-20 lg:-top-20 opacity-30 pointer-events-none mix-blend-screen hidden lg:block" style="z-index: 0;">
          <img src="{img_name}" alt="Premium Finance" class="w-[600px] h-auto blur-[2px] opacity-80" />
      </div>
      <div class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-full opacity-40 pointer-events-none mix-blend-screen hidden md:block z-0 blur-[1px]">
          <img src="{img_name}" alt="Premium Background" class="w-full h-full object-cover object-center rounded-full scale-150 opacity-20" />
      </div>
    """
    
    # We'll put it just inside the Right Content section, before the form container.
    # Since we can't be sure of the exact regex to find the parent, let's inject it into the hero left column
    # Right before the right content div.
    content = re.sub(r'(<!-- Right Content[^>]*>)', r'\1\n' + img_element, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_file(r"c:\Users\Priya\Documents\udyog\grants.html", "grants_img.png")
update_file(r"c:\Users\Priya\Documents\udyog\loans.html", "loans_img.png")
print("Added animations and images successfully!")
