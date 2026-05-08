f = open('eq-audit-v9.html', 'r')
c = f.read()
f.close()

# FIX 1: Screen05 — add line gap after "— Sofia" and a second Keep going button before the italic quote
c = c.replace(
    '    <p class="sofia-attribution">— Sofia</p>\n    <p style="font-style:italic;font-size:16px;color:rgba(245,237,216,0.65);text-align:center;margin-bottom:24px;">"Every answer is showing us something true about you."</p>\n    <button class="btn-gold" onclick="show(\'screen06\'); renderQuizBlock(\'b\')">Keep going</button>',
    '    <p class="sofia-attribution">— Sofia</p>\n\n    <div style="text-align:center;margin:20px 0;"><button class="btn-gold" onclick="show(\'screen06\'); renderQuizBlock(\'b\')" style="font-size:15px;padding:14px 36px;">Keep going</button></div>\n\n    <p style="font-style:italic;font-size:16px;color:rgba(245,237,216,0.65);text-align:center;margin-bottom:24px;">"Every answer is showing us something true about you."</p>\n    <button class="btn-gold" onclick="show(\'screen06\'); renderQuizBlock(\'b\')">Keep going</button>'
)

# FIX 2: Screen07 — move Almost there button to after "200+ women" line
c = c.replace(
    '    <button class="btn-gold" onclick="show(\'screen08\'); renderQuizBlock(\'c\')">Almost there \u2014 finish your audit</button>',
    ''
)
c = c.replace(
    '    <p class="subheadline" style="font-size:16px;">200+ women have already taken the EQ Audit. Here is what changed for them.</p>\n    <div class="testimonial-card">',
    '    <p class="subheadline" style="font-size:16px;">200+ women have already taken the EQ Audit. Here is what changed for them.</p>\n\n    <div style="text-align:center;margin:24px 0;"><button class="btn-gold" onclick="show(\'screen08\'); renderQuizBlock(\'c\')" style="font-size:15px;padding:14px 36px;">Almost there \u2014 finish your audit</button></div>\n\n    <div class="testimonial-card">'
)

f = open('eq-audit-v9.html', 'w')
f.write(c)
f.close()
print('Done')
