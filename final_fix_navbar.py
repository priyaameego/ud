import os
import re

directory = r"c:\Users\Priya\Documents\udyog"

nav2_top_html = '''  <!-- Navbar 2 Top Row (Support & Login) -->
  <div class="w-full transition-all duration-300 nav2-top-row overflow-hidden border-b border-gray-100" style="height: 0; opacity: 0; padding: 0;">
    <div class="max-w-7xl mx-auto px-4 flex items-center justify-between">
      <a href="index.html" class="flex flex-col">
        <div class="text-[28px] font-black text-[#1a237e] tracking-tight leading-none">UDYOG</div>
        <div class="flex items-center gap-1 mt-1">
          <span class="text-[10px] font-bold text-[#1a237e] tracking-wider leading-none">SUVIDHA KENDRA</span>
          <div class="grid grid-cols-2 gap-[1px]">
            <div class="w-1 h-1 bg-[#84cc16]"></div>
            <div class="w-1 h-1 bg-[#84cc16]"></div>
            <div class="w-1 h-1 bg-[#84cc16]"></div>
            <div class="w-1 h-1 bg-[#84cc16]"></div>
          </div>
        </div>
      </a>
      <div class="hidden md:flex items-center gap-8">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 bg-gray-100 rounded-full flex items-center justify-center"><i class="fas fa-envelope text-gray-600 text-sm"></i></div>
          <div class="text-xs">
            <div class="font-semibold text-gray-700">support@udyogsuvidhakendra.in</div>
            <div class="text-gray-500 mt-0.5">Time: 10:30 AM to 06:00 PM</div>
          </div>
        </div>
        <a href="contact.html" class="bg-[#5a4fcf] text-white font-bold py-2.5 px-8 rounded-lg shadow-md hover:bg-[#4b42b4] transition-colors text-sm tracking-wide">Login</a>
      </div>
    </div>
  </div>

  <!-- Bottom Row: Mega Menu -->'''

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original = content

    # 1. Strip out ANY existing nav2-top-row so we can cleanly re-inject
    content = re.sub(r'<!-- Navbar 2 Top Row.*?<!-- Bottom Row: Mega Menu -->', '<!-- Bottom Row: Mega Menu -->', content, flags=re.DOTALL)
    
    # 2. Re-inject nav2-top-row properly
    content = content.replace('<!-- Bottom Row: Mega Menu -->', nav2_top_html)

    # 3. Clean up the messed up single row logo
    content = re.sub(
        r'<div class="hidden lg:flex items-center gap-2 w-full justify-between pr-4 desktop-nav text-sm font-semibold text-gray-700">\s*<!-- Navbar 2 Logo -->\s*<a href="index\.html" class="flex flex-col mr-2 shrink-0">.*?</a>',
        '<div class="hidden lg:flex items-center gap-4 w-full justify-between pr-4 desktop-nav text-sm font-semibold text-gray-700">',
        content, flags=re.DOTALL
    )

    # 4. Clean up the messed up Support & Login at the end
    content = re.sub(
        r'<!-- Support & Login -->\s*<div class="flex items-center gap-3 ml-2 shrink-0">.*?<a href="contact\.html"[^>]*>Login</a>\s*</div>',
        '',
        content, flags=re.DOTALL
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        if update_file(filepath):
            count += 1

print(f"Total files updated: {count}")
