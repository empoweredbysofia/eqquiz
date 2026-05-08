f = open('eq-audit-v9.html', 'r')
c = f.read()
f.close()

# FIX 1: Add emoji to Home Life card
c = c.replace(
    '      <div class="life-area-card" onclick="toggleLifeArea(this,\'Home Life\')" data-area="Home Life">\n        <div class="la-title">Home Life</div>',
    '      <div class="life-area-card" onclick="toggleLifeArea(this,\'Home Life\')" data-area="Home Life">\n        <div class="la-emoji">\U0001f3e0</div>\n        <div class="la-title">Home Life</div>\n        <div class="la-sub">Navigate and connect</div>'
)

# FIX 2: Make emoji cards scroll horizontally on one line
c = c.replace(
    '<div style="display:flex;flex-wrap:wrap;justify-content:center;gap:12px;margin-bottom:28px;max-width:480px;margin-left:auto;margin-right:auto;">',
    '<div style="display:flex;flex-wrap:nowrap;overflow-x:auto;justify-content:flex-start;gap:8px;margin-bottom:28px;width:100%;padding-bottom:6px;-webkit-overflow-scrolling:touch;">'
)

f = open('eq-audit-v9.html', 'w')
f.write(c)
f.close()
print('Done')
