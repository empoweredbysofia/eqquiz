f = open('eq-audit-v9.html', 'r')
content = f.read()
f.close()

button = '    <button class="btn-gold" onclick="show(\'screen14\')" style="font-size:20px;padding:18px 36px;">Show me how →</button>'
content = content.replace(button, '')

target = '    <div class="divider"></div>\n\n    <!-- Block 3: Transformation'
new_button = '    <button class="btn-gold" onclick="show(\'screen14\')" style="font-size:20px;padding:18px 36px;margin-bottom:32px;">Show me how →</button>\n\n    <div class="divider"></div>\n\n    <!-- Block 3: Transformation'
content = content.replace(target, new_button)

f = open('eq-audit-v9.html', 'w')
f.write(content)
f.close()
print('Done')
