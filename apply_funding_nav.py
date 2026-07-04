import os
import re

desktop_html = """            <div class="mega-menu absolute top-full left-0 hidden group-hover:block bg-white/95 backdrop-blur-xl border border-white/20 shadow-2xl rounded-2xl p-6 min-w-[500px] ring-1 ring-black/5 transform opacity-0 group-hover:opacity-100 group-hover:translate-y-0 translate-y-2 transition-all duration-200 origin-top-left">
              <div class="grid grid-cols-2 gap-6">
                <div>
                  <h4 class="text-xs font-bold text-navy-800 uppercase tracking-wider border-b-2 border-blue-100 pb-2 mb-3">Startup Funding</h4>
                  <div class="flex flex-col gap-2">
                    <a href="seed-funding.html" class="text-sm font-medium text-gray-700 hover:text-green-700 hover:bg-green-50 px-2 py-1.5 rounded transition-colors whitespace-nowrap overflow-hidden text-ellipsis">Seed Funding</a>
                    <a href="angel-investment.html" class="text-sm font-medium text-gray-700 hover:text-green-700 hover:bg-green-50 px-2 py-1.5 rounded transition-colors whitespace-nowrap overflow-hidden text-ellipsis">Angel Investment</a>
                    <a href="venture-capital.html" class="text-sm font-medium text-gray-700 hover:text-green-700 hover:bg-green-50 px-2 py-1.5 rounded transition-colors whitespace-nowrap overflow-hidden text-ellipsis">Venture Capital</a>
                  </div>
                </div>
                <div>
                  <h4 class="text-xs font-bold text-navy-800 uppercase tracking-wider border-b-2 border-blue-100 pb-2 mb-3">Govt Schemes</h4>
                  <div class="flex flex-col gap-2">
                    <a href="mudra-loan.html" class="text-sm font-medium text-gray-700 hover:text-green-700 hover:bg-green-50 px-2 py-1.5 rounded transition-colors whitespace-nowrap overflow-hidden text-ellipsis">Mudra Loan</a>
                    <a href="cgtmse-scheme.html" class="text-sm font-medium text-gray-700 hover:text-green-700 hover:bg-green-50 px-2 py-1.5 rounded transition-colors whitespace-nowrap overflow-hidden text-ellipsis">CGTMSE Scheme</a>
                    <a href="startup-india-seed-fund.html" class="text-sm font-medium text-gray-700 hover:text-green-700 hover:bg-green-50 px-2 py-1.5 rounded transition-colors whitespace-nowrap overflow-hidden text-ellipsis">Startup India Seed Fund</a>
                  </div>
                </div>
              </div>
            </div>"""

mobile_html = """          <div class="text-sm font-medium text-gray-600 mb-4 flex flex-col gap-2 pl-4 border-l-2 border-blue-100/50 animate-fade-in-down">
            <div class="font-bold text-xs text-gray-500 uppercase mt-2 mb-1">Startup Funding</div>
            <a href="seed-funding.html" class="hover:text-blue-600 block pl-2 py-0.5">Seed Funding</a>
            <a href="angel-investment.html" class="hover:text-blue-600 block pl-2 py-0.5">Angel Investment</a>
            <a href="venture-capital.html" class="hover:text-blue-600 block pl-2 py-0.5">Venture Capital</a>
            
            <div class="font-bold text-xs text-gray-500 uppercase mt-3 mb-1">Govt Schemes</div>
            <a href="mudra-loan.html" class="hover:text-blue-600 block pl-2 py-0.5">Mudra Loan</a>
            <a href="cgtmse-scheme.html" class="hover:text-blue-600 block pl-2 py-0.5">CGTMSE Scheme</a>
            <a href="startup-india-seed-fund.html" class="hover:text-blue-600 block pl-2 py-0.5">Startup India Seed Fund</a>
          </div>
        </details>"""

with open('_new_navbar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Desktop Funding mega-menu
start_desktop = content.find('<!-- Funding -->')
if start_desktop != -1:
    end_desktop = content.find('<!-- Trademark & IP -->', start_desktop)
    if end_desktop != -1:
        desktop_section = content[start_desktop:end_desktop]
        mega_menu_start = desktop_section.find('<div class="mega-menu')
        mega_menu_end = desktop_section.rfind('</div>\n          </div>')
        if mega_menu_start != -1 and mega_menu_end != -1:
            new_desktop_section = desktop_section[:mega_menu_start] + desktop_html + '\n          </div>\n\n          '
            content = content.replace(desktop_section, new_desktop_section)

# Replace Mobile Funding dropdown
mobile_start = content.find('<span>Funding</span>', end_desktop)
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

print("Successfully reverted Funding dropdown into _new_navbar.html")
