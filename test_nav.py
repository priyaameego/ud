import re

filepath = 'ayush-export-promotion-council.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove nav2-top-row
pattern = re.compile(r'<!-- Navbar 2 Top Row.*?<!-- Bottom Row: Mega Menu -->', re.DOTALL)
content = pattern.sub('<!-- Bottom Row: Mega Menu -->', content)

# 2. Inject Logo
logo_html = '''        <!-- Desktop Mega Nav Links -->
        <div class="hidden lg:flex items-center gap-2 w-full justify-between pr-4 desktop-nav text-sm font-semibold text-gray-700">
          
          <!-- Navbar 2 Logo -->
          <a href="index.html" class="flex flex-col mr-2">
            <div class="text-[18px] font-black text-[#1a237e] tracking-tight leading-none">UDYOG</div>
            <div class="flex items-center gap-1 mt-0.5">
              <span class="text-[7px] font-bold text-[#1a237e] tracking-wider leading-none">SUVIDHA KENDRA</span>
              <div class="grid grid-cols-2 gap-[1px]">
                <div class="w-1 h-1 bg-[#84cc16]"></div><div class="w-1 h-1 bg-[#84cc16]"></div>
                <div class="w-1 h-1 bg-[#84cc16]"></div><div class="w-1 h-1 bg-[#84cc16]"></div>
              </div>
            </div>
          </a>'''

content = content.replace(
    '<div class="hidden lg:flex items-center gap-4 w-full justify-between pr-4 desktop-nav text-sm font-semibold text-gray-700">',
    logo_html
)

# 3. Inject Support & Login at the end of the flex container
# We need to find where the flex container ends.
# The flex container ends just before the Mobile Hamburger toggle which is outside it, or let's find the hamburger.
# Actually, the hamburger toggle is usually outside `hidden lg:flex`.
support_login_html = '''          <!-- Support & Login -->
          <div class="flex items-center gap-3 ml-2">
            <div class="flex items-center gap-1.5">
              <div class="w-6 h-6 bg-blue-50 rounded-md flex items-center justify-center"><i class="fas fa-envelope text-[#1a237e] text-[10px]"></i></div>
              <div class="text-[9px] leading-tight hidden xl:block">
                <div class="font-semibold text-gray-800">support@udyogsuvidhakendra.in</div>
                <div class="text-gray-500">10:30 AM - 06:00 PM</div>
              </div>
            </div>
            <a href="contact.html" class="bg-[#1a237e] text-white font-bold py-1.5 px-3 rounded text-[11px] shadow-sm hover:bg-[#283593] transition-colors">Login</a>
          </div>'''

# Let's place it right before the mobile hamburger menu toggle.
# Wait, the mobile hamburger is not inside the `lg:flex` container!
# It's at the end of `flex items-center justify-between h-14`.
# Let's look at the structure again.
