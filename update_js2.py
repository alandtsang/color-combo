with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# We need to replace the onclick string in the template literal.
content = re.sub(
    r'onclick="applySchemeToAvatar\(\'\$\{mainHex\}\', \'\$\{secondaryHex\}\', \'\$\{accentHex\}\'\)"',
    r'onclick="applySchemeToAvatar(\'${mainHex}\', \'${secondaryHex}\', \'${accentHex}\', event)"',
    content
)

content = content.replace("function applySchemeToAvatar(mainHex, secondaryHex, accentHex) {", "function applySchemeToAvatar(mainHex, secondaryHex, accentHex, e) {")
content = content.replace("const activeEvent = event;", "const activeEvent = e;")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
