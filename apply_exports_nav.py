import os
import re

items_col1 = [
    "Council for Leather Exports", "Handloom Export Promotion Council", "Ayush Export Promotion Council", 
    "Plastics Export Promotion Council", "Services Export Promotion Council", "Cotton Textiles Export Promotion Council", 
    "Wool Industry Export Promotion Council", "Electronics & Computer Software EPC", "Gem & Jewellery Export Promotion Council", 
    "Cashew Export Promotion Council", "Wool & Woollens Export Promotion Council"
]
items_col2 = [
    "Sports Goods & Toys Export Promotion Council", "Export Promotion Council for Handicrafts", 
    "Export Promotion Council for EOUs & SEZs", "Management & Technical Textiles", "RCMC Registration", 
    "APEDA Registration", "Federation of Indian Export Organisations", "The Indian Silk Export Promotion Council", 
    "Indian Oil Seeds & Produce Export Promotion Council", "Shellac & Forest Products Export Promotion Council", 
    "Powerloom Development & Export Promotion Council"
]
items_col3 = [
    "Project Exports Promotion Council", "Pharmaceuticals Export Promotion Council", 
    "Export Promotion Council for Special Economic Zones", "Marine Products Export Development Authority", 
    "Directorate of Handicrafts, J&K", "EEPC INDIA", "Telecom Equipment and Services EPC", 
    "Basic Chemicals Cosmetics & Dyes EPC", "Jute Products Development and EPC", 
    "Mobile and Electronic Devices EPC", "Tea Board"
]
items_col4 = [
    "Coir Board", "Coffee Board", "Rubber Board", "Spices Board", "Tobacco Board", 
    "CAPEXIL", "TESTEPC", "Coconut Development Board", "Carpet Export Promotion Council", 
    "Apparel Export Promotion Council"
]

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def gen_desktop_col(items):
    html = '                <div class="flex flex-col gap-1.5">\n'
    for item in items:
        filename = slugify(item) + ".html"
        display = item if len(item) <= 30 else item[:28] + ".."
        html += f'                  <a href="{filename}" class="text-[12px] font-medium text-gray-700 hover:text-blue-700 hover:bg-blue-50 px-2 py-1 rounded transition-colors whitespace-nowrap overflow-hidden text-ellipsis" title="{item}">{display}</a>\n'
    html += '                </div>'
    return html

def gen_mobile_col(items):
    html = ''
    for item in items:
        filename = slugify(item) + ".html"
        html += f'            <a href="{filename}" class="hover:text-blue-600 block pl-2 text-[12px] py-1">{item}</a>\n'
    return html

desktop_html = f"""            <div class="mega-menu absolute top-full left-1/2 -translate-x-1/2 hidden group-hover:block bg-white/95 backdrop-blur-xl border border-white/20 shadow-2xl rounded-2xl p-6 min-w-[1000px] ring-1 ring-black/5 transform opacity-0 group-hover:opacity-100 group-hover:translate-y-0 translate-y-2 transition-all duration-200 origin-top">
              <div class="grid grid-cols-4 gap-6">
{gen_desktop_col(items_col1)}
{gen_desktop_col(items_col2)}
{gen_desktop_col(items_col3)}
{gen_desktop_col(items_col4)}
              </div>
            </div>"""

mobile_html = f"""          <div class="text-sm font-medium text-gray-600 mb-4 flex flex-col pl-4 border-l-2 border-blue-100/50 animate-fade-in-down h-64 overflow-y-auto">
{gen_mobile_col(items_col1)}
{gen_mobile_col(items_col2)}
{gen_mobile_col(items_col3)}
{gen_mobile_col(items_col4)}
          </div>
        </details>"""

with open('_new_navbar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Desktop Exports mega-menu
# Find start of desktop exports mega menu
start_desktop = content.find('<!-- Exports -->')
if start_desktop != -1:
    end_desktop = content.find('<!-- Funding -->', start_desktop)
    # The block we want to replace is the `<div class="mega-menu...` inside this section.
    if end_desktop != -1:
        desktop_section = content[start_desktop:end_desktop]
        mega_menu_start = desktop_section.find('<div class="mega-menu')
        mega_menu_end = desktop_section.rfind('</div>\n          </div>')
        if mega_menu_start != -1 and mega_menu_end != -1:
            new_desktop_section = desktop_section[:mega_menu_start] + desktop_html + '\n          </div>\n\n          '
            content = content.replace(desktop_section, new_desktop_section)

# Replace Mobile Exports dropdown
start_mobile = content.find('<!-- Exports -->', end_desktop if start_desktop != -1 else 0)
if start_mobile != -1:
    end_mobile = content.find('<!-- Funding -->', start_mobile)
    if end_mobile != -1:
        mobile_section = content[start_mobile:end_mobile]
        div_start = mobile_section.find('<div class="text-sm')
        div_end = mobile_section.find('</details>') + len('</details>')
        if div_start != -1 and div_end != -1:
            new_mobile_section = mobile_section[:div_start] + mobile_html + '\n\n        '
            content = content.replace(mobile_section, new_mobile_section)

with open('_new_navbar.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully injected Exports mega menu into _new_navbar.html")
