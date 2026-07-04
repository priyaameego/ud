import os

directory = r"c:\Users\Priya\Documents\udyog"

nav2_html = '''  <!-- Navbar 2 Top Row (Support & Login) -->
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
      <div class="hidden md:flex items-center gap-6">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 bg-blue-50 rounded-lg flex items-center justify-center"><i class="fas fa-envelope text-[#1a237e] text-sm"></i></div>
          <div class="text-xs">
            <div class="font-semibold text-gray-800">support@udyogsuvidhakendra.in</div>
            <div class="text-gray-500">Time: 10:30 AM to 06:00 PM</div>
          </div>
        </div>
        <a href="contact.html" class="bg-[#1a237e] text-white font-bold py-2 px-6 rounded-lg shadow-md hover:bg-[#283593] transition-colors text-sm">Login</a>
      </div>
    </div>
  </div>

  <!-- Bottom Row: Mega Menu -->'''

old_js = '''  // Hide bottom row on scroll (Desktop)
  const bottomRow = document.querySelector('.nav-bottom-row');
  if(bottomRow) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        bottomRow.style.height = '0';
        bottomRow.style.opacity = '0';
        bottomRow.style.overflow = 'hidden';
      } else {
        bottomRow.style.height = '56px'; // h-14 is 3.5rem = 56px
        bottomRow.style.opacity = '1';
        bottomRow.style.overflow = 'visible';
      }
    });
  }'''

new_js = '''  // Dual Navbar Scroll Logic
  const topRow = document.querySelector('.top-row');
  const bottomRow = document.querySelector('.nav-bottom-row');
  const nav2Top = document.querySelector('.nav2-top-row');
  const premiumNavbar = document.getElementById('premium-navbar');
  
  // Set initial state
  if (bottomRow) {
    bottomRow.style.height = '0';
    bottomRow.style.opacity = '0';
    bottomRow.style.overflow = 'hidden';
  }
  if (nav2Top) {
    nav2Top.style.height = '0';
    nav2Top.style.opacity = '0';
    nav2Top.style.overflow = 'hidden';
    nav2Top.style.padding = '0';
  }

  let lastScrollY = window.scrollY;
  window.addEventListener('scroll', () => {
    const currentScrollY = window.scrollY;
    
    if (currentScrollY > 50 && currentScrollY > lastScrollY) {
      // Scrolling DOWN
      if(topRow) { 
        topRow.style.height = '0'; 
        topRow.style.opacity = '0'; 
        topRow.style.overflow = 'hidden'; 
        topRow.style.padding = '0'; 
      }
      if(nav2Top) { 
        nav2Top.style.height = 'auto'; 
        nav2Top.style.opacity = '1'; 
        nav2Top.style.overflow = 'visible'; 
        nav2Top.style.padding = '0.5rem 0'; 
      }
      if(bottomRow) { 
        bottomRow.style.height = '56px'; 
        bottomRow.style.opacity = '1'; 
        bottomRow.style.overflow = 'visible'; 
      }
      if(premiumNavbar) {
        premiumNavbar.classList.add('shadow-md');
        premiumNavbar.classList.remove('shadow-sm');
      }
    } else if (currentScrollY < lastScrollY || currentScrollY <= 50) {
      // Scrolling UP or at top
      if(topRow) { 
        topRow.style.height = 'auto'; 
        topRow.style.opacity = '1'; 
        topRow.style.overflow = 'visible'; 
        topRow.style.padding = '0.75rem 0'; 
      }
      if(nav2Top) { 
        nav2Top.style.height = '0'; 
        nav2Top.style.opacity = '0'; 
        nav2Top.style.overflow = 'hidden'; 
        nav2Top.style.padding = '0'; 
      }
      if(bottomRow) { 
        bottomRow.style.height = '0'; 
        bottomRow.style.opacity = '0'; 
        bottomRow.style.overflow = 'hidden'; 
      }
      if(currentScrollY <= 50 && premiumNavbar) {
        premiumNavbar.classList.remove('shadow-md');
        premiumNavbar.classList.add('shadow-sm');
      }
    }
    lastScrollY = currentScrollY;
  });'''


def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    changed = False

    # 1. Replace JS
    if old_js in content:
        content = content.replace(old_js, new_js)
        changed = True
    elif 'Dual Navbar Scroll Logic' not in content:
         # Try a more flexible replacement for JS if whitespace differs
         import re
         js_pattern = re.compile(r'// Hide bottom row on scroll \(Desktop\).*?bottomRow\.style\.overflow = \'visible\';\s*}\s*}\);\s*}', re.DOTALL)
         if js_pattern.search(content):
             content = js_pattern.sub(new_js, content)
             changed = True
             
    # 2. Inject nav2_html if not present
    if 'nav2-top-row' not in content:
        if '<!-- Bottom Row: Mega Menu -->' in content:
            content = content.replace('<!-- Bottom Row: Mega Menu -->', nav2_html)
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
