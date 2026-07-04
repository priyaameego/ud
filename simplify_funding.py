import os
import sys

directory = r"c:\Users\Priya\Documents\udyog"

desktop_old_start = '<!-- Funding -->'
desktop_old_end = '<!-- Trademark & IP -->'
desktop_fallback_end = '<!-- Trademark -->'

desktop_new = '''<!-- Funding -->
          <div class="nav-item relative group h-full flex items-center cursor-pointer text-[#374151] hover:text-[#1a237e] transition-colors">
            <a href="funding.html" class="py-4 font-semibold group-hover:text-blue-600 group-hover:bg-blue-50 px-3 rounded-lg transition-colors">Funding <i class="fas fa-chevron-down text-[10px] ml-1.5 opacity-60 transition-transform group-hover:rotate-180"></i></a>
            <div class="absolute top-full left-0 hidden group-hover:block bg-white border border-gray-100 shadow-xl rounded-2xl p-2 min-w-[200px] transform opacity-0 group-hover:opacity-100 group-hover:translate-y-0 translate-y-2 transition-all duration-200 origin-top-left z-50">
              <div class="flex flex-col gap-1">
                <a href="grants.html" class="text-[15px] font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-50 px-4 py-2.5 rounded-xl transition-colors whitespace-nowrap">Grants</a>
                <a href="loans.html" class="text-[15px] font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-50 px-4 py-2.5 rounded-xl transition-colors whitespace-nowrap">Loans</a>
                <a href="nbfc.html" class="text-[15px] font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-50 px-4 py-2.5 rounded-xl transition-colors whitespace-nowrap">NBFC</a>
                <a href="equity.html" class="text-[15px] font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-50 px-4 py-2.5 rounded-xl transition-colors whitespace-nowrap">Equity</a>
              </div>
            </div>
          </div>

          '''

mobile_old_start = '<!-- Funding -->\n        <details'
mobile_old_end = '        <!-- Contact -->'

mobile_new = '''<!-- Funding -->
        <details class="group border-b border-gray-100">
          <summary class="flex justify-between items-center font-bold text-gray-800 text-base cursor-pointer list-none py-4 hover:text-[#1a237e] transition-colors">
            <span>Funding</span>
            <span class="transition-transform duration-300 group-open:rotate-180 text-gray-400">
              <i class="fas fa-chevron-down text-xs"></i>
            </span>
          </summary>
          <div class="text-sm font-medium text-gray-600 mb-4 flex flex-col gap-1 pl-4 border-l-2 border-blue-100/50 animate-fade-in-down">
            <a href="grants.html" class="hover:text-blue-600 hover:bg-blue-50/50 rounded-lg block px-3 py-2 text-[15px]">Grants</a>
            <a href="loans.html" class="hover:text-blue-600 hover:bg-blue-50/50 rounded-lg block px-3 py-2 text-[15px]">Loans</a>
            <a href="nbfc.html" class="hover:text-blue-600 hover:bg-blue-50/50 rounded-lg block px-3 py-2 text-[15px]">NBFC</a>
            <a href="equity.html" class="hover:text-blue-600 hover:bg-blue-50/50 rounded-lg block px-3 py-2 text-[15px]">Equity</a>
          </div>
        </details>

'''

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    changed = False

    # Replace Desktop Menu
    # We find the first "<!-- Funding -->" in the file which corresponds to the desktop mega menu.
    idx1 = content.find(desktop_old_start)
    if idx1 != -1:
        # Find Trademark
        idx2 = content.find(desktop_old_end, idx1)
        if idx2 == -1:
            idx2 = content.find(desktop_fallback_end, idx1)
            
        if idx2 != -1:
            # We must be careful not to replace the mobile menu yet.
            # The desktop menu is before the mobile menu.
            content = content[:idx1] + desktop_new + content[idx2:]
            changed = True

    # Replace Mobile Menu
    # After first replacement, find again the next "<!-- Funding -->" which is for mobile
    # OR we can just search for the details tag
    mob_idx1 = content.find('<!-- Funding -->\\n        <details')
    if mob_idx1 == -1:
         mob_idx1 = content.find('<!-- Funding -->\\n\\t\\t<details')
    if mob_idx1 == -1:
         mob_idx1 = content.find('<!-- Funding -->\\n      <details')
    if mob_idx1 == -1:
         # let's do a more robust search for mobile menu
         mob_idx1 = content.find('<!-- Funding -->', content.find('<!-- Mobile Menu -->'))
         
    if mob_idx1 != -1:
        mob_idx2 = content.find(mobile_old_end, mob_idx1)
        if mob_idx2 != -1:
            content = content[:mob_idx1] + mobile_new + content[mob_idx2:]
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
        if replace_in_file(filepath):
            count += 1
            print(f"Updated {filename}")

print(f"Total files updated: {count}")
