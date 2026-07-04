import re

with open('_new_navbar.html', 'r', encoding='utf-8') as f:
    html = f.read()

def get_block(html, start_marker, end_marker):
    start = html.find(start_marker)
    if start == -1: return ""
    end = html.find(end_marker, start)
    if end == -1: return ""
    return html[start:end]

# Extract blocks from current navbar
# From Top Row
funding = get_block(html, '<!-- Funding -->', '<!-- Trademark & IP -->')
trademark = get_block(html, '<!-- Trademark & IP -->', '<!-- International -->')
international = get_block(html, '<!-- International -->', '<!-- Skill India')
skill_india = get_block(html, '<div class="nav-item relative group h-full flex items-center cursor-pointer text-[#374151] hover:text-[#1a237e] transition-colors">\n            <span class="py-4 font-semibold">Skill India', '<!-- Desktop Hamburger')
if not skill_india:
    skill_india = get_block(html, '<!-- Skill India', '<!-- Desktop Hamburger')
hamburger = get_block(html, '<!-- Desktop Hamburger (More Options) -->', '</div>\n\n        <!-- Mobile Hamburger Icon -->')

# Clean up any trailing tags in hamburger block
hamburger = hamburger.strip()
if hamburger.endswith('</div>'):
    hamburger = hamburger[:-6].strip()

# From Bottom Row
bottom_nav_start = html.find('<!-- Business -->')
bottom_nav_end = html.find('</div>\n\n        <!-- Mobile Hamburger Icon -->', bottom_nav_start)
if bottom_nav_end == -1:
    bottom_nav_end = html.find('</div>\n      </div>\n    </div>', bottom_nav_start)
bottom_row = html[bottom_nav_start:bottom_nav_end].strip()

# Now we construct the new top row
top_row = """      <!-- Top Row Navigation Links -->
      <nav class="hidden lg:flex items-center gap-8">
        <a href="index.html" class="text-sm font-semibold text-gray-700 hover:text-[#1a237e] transition-colors">Home</a>
        <a href="overview.html" class="text-sm font-semibold text-gray-700 hover:text-[#1a237e] transition-colors">Overview</a>
        <!-- Funding -->
""" + funding.replace('<!-- Funding -->\n', '') + """        <a href="benefits.html" class="text-sm font-semibold text-gray-700 hover:text-[#1a237e] transition-colors">Benefits</a>
        <a href="process.html" class="text-sm font-semibold text-gray-700 hover:text-[#1a237e] transition-colors">Process</a>
        <a href="documents.html" class="text-sm font-semibold text-gray-700 hover:text-[#1a237e] transition-colors">Documents</a>
        <a href="faq.html" class="text-sm font-semibold text-gray-700 hover:text-[#1a237e] transition-colors">FAQs</a>
      </nav>
      
      <!-- Apply Now Button -->
      <div class="hidden lg:block">
        <a href="contact.html" class="bg-[#1a237e] text-white font-bold py-2.5 px-6 rounded-lg shadow-md hover:shadow-lg hover:bg-[#283593] transition-all duration-300">
          Apply Now
        </a>
      </div>
"""

# Construct the new bottom row
# Combine bottom_row with trademark, international, skill_india, hamburger
new_bottom_row = bottom_row + '\n          ' + funding + '\n          ' + trademark + '\n          ' + international + '\n          ' + skill_india + '\n          ' + hamburger

# Create the full replacement for the desktop part
mobile_start = html.find('<!-- Mobile Nav Sidebar/Dropdown')
head_start = html.find('<header')
header_opening = html[head_start:html.find('<!-- Top Row Navigation Links -->')]

full_desktop = header_opening + top_row + """    </div>
  </div>

  <!-- Bottom Row: Mega Menu -->
  <div class="nav-bottom-row w-full transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4">
      <div class="flex items-center justify-between h-14">
        
        <!-- Desktop Mega Nav Links -->
        <div class="hidden lg:flex items-center gap-4 w-full justify-between pr-4 desktop-nav text-sm font-semibold text-gray-700">
          """ + new_bottom_row + """
        </div>

        <!-- Mobile Hamburger Icon (if you want one here, or leave empty if it's in top row) -->
      </div>
    </div>
  </div>

  """

# Note: The original mobile toggle is actually inside the Top Row container!
# Wait, let's fix the mobile toggle position.
# It should be right after "Apply Now Button" div inside the top row flex container.
top_row_end_idx = html.find('<!-- Mobile Hamburger Icon -->')
if top_row_end_idx != -1:
    mobile_hamburger = html[top_row_end_idx:html.find('</div>', top_row_end_idx)+6]
else:
    mobile_hamburger = ""

# Let's rebuild properly
top_section = header_opening + top_row + "\n      " + mobile_hamburger + "\n    </div>\n  </div>\n\n"
bottom_section = """  <!-- Bottom Row: Mega Menu -->
  <div class="nav-bottom-row w-full transition-all duration-300 border-t border-gray-100">
    <div class="max-w-7xl mx-auto px-4">
      <div class="flex items-center justify-between h-14">
        
        <!-- Desktop Mega Nav Links -->
        <div class="hidden lg:flex items-center gap-4 w-full justify-between pr-4 desktop-nav text-[13px] font-semibold text-gray-700">
          """ + bottom_row + '\n          <!-- Funding Bottom -->\n' + funding.replace('<!-- Funding -->\n', '') + '\n          ' + trademark + '\n          ' + international + '\n          ' + skill_india + '\n          ' + hamburger + """
        </div>
      </div>
    </div>
  </div>

  """

final_html = html[:head_start] + top_section + bottom_section + html[mobile_start:]

with open('_new_navbar.html', 'w', encoding='utf-8') as f:
    f.write(final_html)
print("Updated _new_navbar.html")
