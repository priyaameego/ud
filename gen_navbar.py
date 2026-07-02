import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract from '<!-- Business -->' to '<!-- Skill India --> ... </div>'
start_marker = '<!-- Business -->'
end_marker = '<div class="ml-auto flex items-center gap-2 pl-4">'
start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

nav_items = content[start_idx:end_idx]

unified_navbar = f'''<!-- =========================================================
     UNIFIED NAVBAR
     ========================================================= -->
<nav class="navbar sticky top-0 z-50 bg-white border-b border-gray-200 shadow-sm transition-all">
  <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
    <!-- Logo -->
    <a href="index.html" class="flex items-center">
      <img src="logo.png" alt="Udyog Suvidha Kendra" class="h-10">
    </a>

    <!-- Desktop Nav -->
    <div class="hidden lg:flex items-center gap-2 desktop-nav">
{nav_items}
    </div>

    <!-- Right Button -->
    <div class="hidden lg:flex items-center gap-4">
      <a href="tel:+919999999999" class="font-bold text-sm text-gray-700 hover:text-navy-700"><i class="fas fa-phone mr-1"></i>+91 99XXX XXXXX</a>
      <a href="contact.html" class="btn-primary text-sm py-2.5 px-6" style="background:#1a3490; color:#fff;">Talk to Expert</a>
    </div>

    <!-- Mobile Toggle -->
    <button id="mob-nav-toggle" class="lg:hidden text-navy-900 p-2 rounded-lg border border-gray-200">
      <i class="fas fa-bars text-lg"></i>
    </button>
  </div>

  <!-- Mobile Menu -->
  <div id="mobile-nav" class="hidden lg:hidden border-t border-gray-100 bg-white w-full absolute left-0 top-full shadow-lg">
    <div class="grid grid-cols-2 gap-1 p-4">
      <a href="business-registration.html" class="text-sm text-gray-700 hover:bg-navy-50 px-3 py-2 rounded-lg font-medium">?? Business</a>
      <a href="licenses.html" class="text-sm text-gray-700 hover:bg-navy-50 px-3 py-2 rounded-lg font-medium">?? Licenses</a>
      <a href="compliance.html" class="text-sm text-gray-700 hover:bg-navy-50 px-3 py-2 rounded-lg font-medium">? Compliance</a>
      <a href="taxation.html" class="text-sm text-gray-700 hover:bg-navy-50 px-3 py-2 rounded-lg font-medium">?? Taxation</a>
      <a href="gst.html" class="text-sm text-gray-700 hover:bg-navy-50 px-3 py-2 rounded-lg font-medium">?? GST</a>
      <a href="international.html" class="text-sm text-gray-700 hover:bg-navy-50 px-3 py-2 rounded-lg font-medium">?? International</a>
      <a href="funding.html" class="text-sm text-gray-700 hover:bg-navy-50 px-3 py-2 rounded-lg font-medium">?? Funding</a>
      <a href="contact.html" class="text-sm text-gray-700 hover:bg-navy-50 px-3 py-2 rounded-lg font-medium">?? Contact</a>
    </div>
  </div>
</nav>'''

with open('_new_navbar.html', 'w', encoding='utf-8') as f:
    f.write(unified_navbar)
