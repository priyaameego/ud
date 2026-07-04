import os
import re

items_col1 = [
    "Fire Licence",
    "PF Registration",
    "PT Registration",
    "GeM Registration",
    "GST Registration",
    "ISO Registration",
    "ZED Certification",
    "BIS Registration"
]

items_col2 = [
    "DSC Registration",
    "ESI Registration",
    "RERA Registration",
    "Udyam Registration",
    "FCRA Registration",
    "Food Registration",
    "Darpan Registration",
    "Barcode Registration"
]

items_col3 = [
    "Gumasta Registration",
    "ICEGATE Registration",
    "Only 80G Registration",
    "Only 12A Registration",
    "12A and 80G Registration",
    "ImportExport Registration",
    "Tax Exemption Certificate",
    "Startup India Registration"
]

def slugify(text):
    text = text.lower()
    text = text.replace('(', '').replace(')', '').replace('&', 'and')
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def gen_desktop_col(items):
    html = '                <div class="flex flex-col gap-2">\n'
    for item in items:
        filename = slugify(item) + ".html"
        html += f'                  <a href="{filename}" class="text-[13px] font-medium text-gray-700 hover:text-amber-700 hover:bg-amber-50 px-2 py-1.5 rounded transition-colors whitespace-nowrap overflow-hidden text-ellipsis">{item}</a>\n'
    html += '                </div>'
    return html

def gen_mobile_col(items):
    html = ''
    for item in items:
        filename = slugify(item) + ".html"
        html += f'            <a href="{filename}" class="hover:text-blue-600 block pl-2 text-[13px] py-1">{item}</a>\n'
    return html

desktop_html = f"""            <div class="mega-menu absolute top-full left-0 hidden group-hover:block bg-white/95 backdrop-blur-xl border border-white/20 shadow-2xl rounded-2xl p-6 min-w-[750px] ring-1 ring-black/5 transform opacity-0 group-hover:opacity-100 group-hover:translate-y-0 translate-y-2 transition-all duration-200 origin-top-left">
              <div class="grid grid-cols-3 gap-6">
{gen_desktop_col(items_col1)}
{gen_desktop_col(items_col2)}
{gen_desktop_col(items_col3)}
              </div>
            </div>"""

mobile_html = f"""          <div class="text-sm font-medium text-gray-600 mb-4 flex flex-col pl-4 border-l-2 border-blue-100/50 animate-fade-in-down h-64 overflow-y-auto">
{gen_mobile_col(items_col1)}
{gen_mobile_col(items_col2)}
{gen_mobile_col(items_col3)}
          </div>
        </details>"""

with open('_new_navbar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Desktop Certificate mega-menu
start_desktop = content.find('<!-- Certificate -->')
if start_desktop != -1:
    end_desktop = content.find('<!-- Compliance -->', start_desktop)
    if end_desktop != -1:
        desktop_section = content[start_desktop:end_desktop]
        mega_menu_start = desktop_section.find('<div class="mega-menu')
        mega_menu_end = desktop_section.rfind('</div>\n          </div>')
        if mega_menu_start != -1 and mega_menu_end != -1:
            new_desktop_section = desktop_section[:mega_menu_start] + desktop_html + '\n          </div>\n\n          '
            content = content.replace(desktop_section, new_desktop_section)

# Replace Mobile Certificate dropdown
# The mobile menu is generally labeled "Certificate" or "Certificates"
mobile_start = content.find('<span>Certificate</span>', end_desktop)
if mobile_start != -1:
    details_start = content.rfind('<details', end_desktop, mobile_start)
    if details_start != -1:
        details_end = content.find('</details>', mobile_start) + len('</details>')
        if details_end != -1:
            mobile_section = content[details_start:details_end]
            div_start = mobile_section.find('<div class="text-sm')
            div_end = mobile_section.find('</details>') + len('</details>')
            if div_start != -1 and div_end != -1:
                new_mobile_section = mobile_section[:div_start] + mobile_html
                content = content.replace(mobile_section, new_mobile_section)

with open('_new_navbar.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully injected Certificate mega menu into _new_navbar.html")
