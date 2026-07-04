import os
import re

directory = r"c:\Users\Priya\Documents\udyog"

logo_html = '''        <!-- Desktop Mega Nav Links -->
        <div class="hidden lg:flex items-center gap-2 w-full justify-between pr-4 desktop-nav text-sm font-semibold text-gray-700">
          
          <!-- Navbar 2 Logo -->
          <a href="index.html" class="flex flex-col mr-2 shrink-0">
            <div class="text-[18px] font-black text-[#1a237e] tracking-tight leading-none">UDYOG</div>
            <div class="flex items-center gap-1 mt-0.5">
              <span class="text-[7px] font-bold text-[#1a237e] tracking-wider leading-none">SUVIDHA KENDRA</span>
              <div class="grid grid-cols-2 gap-[1px]">
                <div class="w-1 h-1 bg-[#84cc16]"></div><div class="w-1 h-1 bg-[#84cc16]"></div>
                <div class="w-1 h-1 bg-[#84cc16]"></div><div class="w-1 h-1 bg-[#84cc16]"></div>
              </div>
            </div>
          </a>'''

login_html = '''        </div>
          
          <!-- Support & Login -->
          <div class="flex items-center gap-3 ml-2 shrink-0">
            <div class="flex items-center gap-1.5">
              <div class="w-6 h-6 bg-blue-50 rounded-md flex items-center justify-center"><i class="fas fa-envelope text-[#1a237e] text-[10px]"></i></div>
              <div class="text-[9px] leading-tight hidden xl:block">
                <div class="font-semibold text-gray-800">support@udyogsuvidhakendra.in</div>
                <div class="text-gray-500">10:30 AM - 06:00 PM</div>
              </div>
            </div>
            <a href="contact.html" class="bg-[#1a237e] text-white font-bold py-1.5 px-3 rounded text-[11px] shadow-sm hover:bg-[#283593] transition-colors">Login</a>
          </div>
      </div>'''

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    changed = False

    # 1. Remove nav2-top-row if present
    if 'nav2-top-row' in content:
        content = re.sub(r'<!-- Navbar 2 Top Row.*?<!-- Bottom Row: Mega Menu -->', '<!-- Bottom Row: Mega Menu -->', content, flags=re.DOTALL)
        changed = True

    # 2. Inject Logo
    if '<!-- Navbar 2 Logo -->' not in content:
        start_pattern = r'<div class="hidden lg:flex items-center gap-4 w-full justify-between pr-4 desktop-nav text-sm font-semibold text-gray-700">'
        if start_pattern in content:
            content = content.replace(start_pattern, logo_html)
            changed = True
        
        # 3. Inject Login block at the end of the desktop-nav
        # Find the end of desktop-nav by looking for `experts.html... </div> </div>`
        # Because whitespace can vary, we use regex.
        end_pattern = re.compile(r'</a>\s*</div>\s*</div>\s*(?=<!-- Apply Mobile Button -->)', re.DOTALL)
        if end_pattern.search(content):
            content = end_pattern.sub(r'</a>\n' + login_html, content)
            changed = True
        else:
             # Fallback if "Apply Mobile Button" isn't exactly there, try a slightly looser regex
             end_pattern2 = re.compile(r'</a>\s*</div>\s*</div>\s*(?=<(?:a|button|div)[^>]*class="[^"]*mobile[^"]*")', re.DOTALL | re.IGNORECASE)
             if end_pattern2.search(content):
                 content = end_pattern2.sub(r'</a>\n' + login_html, content)
                 changed = True

    if changed:
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
            print(f"Updated {filename}")

print(f"Total files updated: {count}")
