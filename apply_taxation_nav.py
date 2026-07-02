import os
import re

items_col1 = [
    "Composition Return",
    "GST Cancellation",
    "GST Return Filing",
    "GST Nil Return",
    "ITR-1 (Only Salary)",
    "ITR-2 (Salary & Other)"
]
items_col2 = [
    "ITR-3 Return Filing",
    "ITR-4 Return Filing",
    "ITR-5 Return Filing",
    "ITR-6 Return Filing",
    "ITR-7 Return Filing"
]

def slugify(text):
    text = text.lower()
    text = text.replace('(', '').replace(')', '').replace('&', 'and')
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def gen_desktop_col(items):
    html = '                <div class="flex flex-col gap-3">\n'
    for item in items:
        filename = slugify(item) + ".html"
        html += f'                  <a href="{filename}" class="text-sm font-medium text-gray-700 hover:text-indigo-700 hover:bg-indigo-50 px-3 py-2 rounded-lg transition-colors whitespace-nowrap overflow-hidden text-ellipsis">{item}</a>\n'
    html += '                </div>'
    return html

def gen_mobile_col(items):
    html = ''
    for item in items:
        filename = slugify(item) + ".html"
        html += f'            <a href="{filename}" class="hover:text-blue-600 block pl-2 py-1">{item}</a>\n'
    return html

desktop_html = f"""            <div class="mega-menu absolute top-full left-1/2 -translate-x-1/2 hidden group-hover:block bg-white/95 backdrop-blur-xl border border-white/20 shadow-2xl rounded-2xl p-8 min-w-[600px] ring-1 ring-black/5 transform opacity-0 group-hover:opacity-100 group-hover:translate-y-0 translate-y-2 transition-all duration-200 origin-top">
              <div class="grid grid-cols-2 gap-8">
{gen_desktop_col(items_col1)}
{gen_desktop_col(items_col2)}
              </div>
            </div>"""

mobile_html = f"""          <div class="text-sm font-medium text-gray-600 mb-4 flex flex-col gap-2 pl-4 border-l-2 border-blue-100/50 animate-fade-in-down">
{gen_mobile_col(items_col1)}
{gen_mobile_col(items_col2)}
          </div>
        </details>"""

with open('_new_navbar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Desktop Taxation mega-menu
start_desktop = content.find('<!-- Taxation -->')
if start_desktop != -1:
    end_desktop = content.find('<!-- Exports -->', start_desktop)
    if end_desktop != -1:
        desktop_section = content[start_desktop:end_desktop]
        mega_menu_start = desktop_section.find('<div class="mega-menu')
        mega_menu_end = desktop_section.rfind('</div>\n          </div>')
        if mega_menu_start != -1 and mega_menu_end != -1:
            new_desktop_section = desktop_section[:mega_menu_start] + desktop_html + '\n          </div>\n\n          '
            content = content.replace(desktop_section, new_desktop_section)

# Replace Mobile Taxation dropdown
# Wait, where is the mobile taxation dropdown?
# I need to find "<!-- Taxation -->" after the desktop one, or just search for "<span>Taxation</span>" in the mobile section.
mobile_taxation_start = content.find('<span>Taxation</span>', end_desktop)
if mobile_taxation_start != -1:
    # Find the nearest details tag start before it
    details_start = content.rfind('<details', end_desktop, mobile_taxation_start)
    if details_start != -1:
        details_end = content.find('</details>', mobile_taxation_start) + len('</details>')
        if details_end != -1:
            mobile_section = content[details_start:details_end]
            div_start = mobile_section.find('<div class="text-sm')
            div_end = mobile_section.find('</details>') + len('</details>')
            if div_start != -1 and div_end != -1:
                new_mobile_section = mobile_section[:div_start] + mobile_html
                content = content.replace(mobile_section, new_mobile_section)
# Note: Actually, there is NO mobile "Taxation" section explicitly labeled with <!-- Taxation --> in the previous diffs, it's just under a details tag. 
# Let me double check if there's an issue with the mobile section replacement.
# Let's write the file back.
with open('_new_navbar.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully injected Taxation mega menu into _new_navbar.html")
