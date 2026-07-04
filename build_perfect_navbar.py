with open('original_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

head_start = html.find('<header')
head_end = html.find('</header>')
header = html[head_start:head_end+9]

# Rename the first Funding to Funding Top so apply scripts don't get confused
header = header.replace('<!-- Funding -->', '<!-- Funding Top -->', 1)

with open('_new_navbar.html', 'w', encoding='utf-8') as f:
    f.write(header)

print("Saved perfect base navbar to _new_navbar.html")
