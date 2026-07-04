import re
with open('original_index.html', 'r', encoding='utf-8') as f:
    html = f.read()
head_start = html.find('<header')
head_end = html.find('</header>')
header = html[head_start:head_end+9]
print('Has nav-bottom-row:', 'nav-bottom-row' in header)
top = header[header.find('<!-- Top Row Navigation Links -->'):header.find('<!-- Bottom Row: Mega Menu -->')]
bottom = header[header.find('<!-- Bottom Row: Mega Menu -->'):header.find('<!-- Mobile Nav Sidebar')]
print('Top spans:', re.findall(r'<span class="py-4 font-semibold">(.*?)<', top))
print('Top links:', re.findall(r'<a href=[^>]*>([^<]+)</a>', top))
print('Bottom spans:', re.findall(r'<span class="py-4 font-semibold">(.*?)<', bottom))
print('Bottom links:', re.findall(r'<a href=[^>]*>([^<]+)</a>', bottom))
