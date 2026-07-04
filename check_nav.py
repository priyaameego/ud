import re

with open('_new_navbar.html', 'r', encoding='utf-8') as f:
    html = f.read()

top_block = html[html.find('<!-- Top Row Navigation Links -->'):html.find('<!-- Bottom Row: Mega Menu -->')]
bottom_block = html[html.find('<!-- Bottom Row: Mega Menu -->'):html.find('<!-- Mobile Nav Sidebar')]

print('Top row contains:')
print('spans:', re.findall(r'<span class="py-4 font-semibold">(.*?)<', top_block))
print('links:', re.findall(r'<a href=[^>]*>([^<]+)</a>', top_block))

print('\nBottom row contains:')
print('spans:', re.findall(r'<span class="py-4 font-semibold">(.*?)<', bottom_block))
print('links:', re.findall(r'<a href=[^>]*>([^<]+)</a>', bottom_block))
