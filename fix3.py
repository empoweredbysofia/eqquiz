f = open('eq-audit-v9.html', 'r')
c = f.read()
f.close()

# FIX 1: Add line space between "— Sofia" and the Discover button on screen02
c = c.replace(
    '<p class="sofia-attribution">— Sofia</p>\n\n    <div style="text-align:center;margin-bottom:28px;"><button class="btn-gold" onclick="show(\'screen03\')" style="font-size:15px;padding:14px 36px;">Discover your EQ Stage — Free</button></div>',
    '<p class="sofia-attribution">— Sofia</p>\n\n    <div style="height:20px;"></div>\n\n    <div style="text-align:center;margin-bottom:28px;"><button class="btn-gold" onclick="show(\'screen03\')" style="font-size:15px;padding:14px 36px;">Discover your EQ Stage \u2014 Free</button></div>'
)

# FIX 2: Remove duplicate emoji icons at the bottom of screen02 (the eq-reminder-cards section has Career/Parenting icons already shown at bottom — keep only the new ones we added near EQ definition)
# The old icons were in .eq-reminder-cards div — remove that whole block
c = c.replace(
    '\n    <div class="eq-reminder-cards">\n      <div class="eq-card"><div class="eq-card-icon">\U0001f9e0</div><div class="eq-card-text"><strong style="color:var(--gold);">Career:</strong> EQ is the most consistent predictor of professional success \u2014 more than IQ or technical skill.</div></div>\n      <div class="eq-card"><div class="eq-card-icon">\u2764\ufe0f</div><div class="eq-card-text"><strong style="color:var(--gold);">Relationships:</strong> Couples who understand their emotional triggers report dramatically deeper connection and repair.</div></div>\n      <div class="eq-card"><div class="eq-card-icon">\U0001f64c</div><div class="eq-card-text"><strong style="color:var(--gold);">Parenting:</strong> Regulated parents raise regulated children. Your healing is generational.</div></div>\n    </div>',
    ''
)

# FIX 3: Add Home life to life area cards on screen02
c = c.replace(
    "      <div class=\"life-area-card\" onclick=\"toggleLifeArea(this,'Parenting')\" data-area=\"Parenting\">",
    "      <div class=\"life-area-card\" onclick=\"toggleLifeArea(this,'Home Life')\" data-area=\"Home Life\">\n        <div class=\"la-emoji\">\U0001f3e0</div>\n        <div class=\"la-title\">Home Life</div>\n      </div>\n      <div class=\"life-area-card\" onclick=\"toggleLifeArea(this,'Parenting')\" data-area=\"Parenting\">"
)

# FIX 4: Screen05 (halfway) — add line gap after "— Sofia" and second "Keep going" button before existing one
c = c.replace(
    '    <p class="sofia-attribution">— Sofia</p>\n\n    <div class="eq-reminder-cards">',
    '    <p class="sofia-attribution">— Sofia</p>\n\n    <div style="height:20px;"></div>\n    <div style="text-align:center;margin-bottom:28px;"><button class="btn-gold" onclick="show(\'screen06\'); renderQuizBlock(\'b\')" style="font-size:15px;padding:14px 36px;">Keep going</button></div>\n\n    <div class="eq-reminder-cards">'
)

# FIX 5: Screen07 — move "Almost there" button to after the "200+ women" line and before testimonials
old_btn = '    <button class="btn-gold" onclick="show(\'screen08\'); renderQuizBlock(\'c\')">Almost there \u2014 finish your audit</button>'
# Remove from current position
c = c.replace(old_btn, '')
# Insert after "200+ women" line and before first testimonial-card
c = c.replace(
    '    <p class="subheadline" style="font-size:16px;">200+ women have already taken the EQ Audit. Here is what changed for them.</p>\n    <div class="testimonial-card">',
    '    <p class="subheadline" style="font-size:16px;">200+ women have already taken the EQ Audit. Here is what changed for them.</p>\n\n    <div style="text-align:center;margin:24px 0;"><button class="btn-gold" onclick="show(\'screen08\'); renderQuizBlock(\'c\')" style="font-size:15px;padding:14px 36px;">Almost there \u2014 finish your audit</button></div>\n\n    <div class="testimonial-card">'
)

# FIX 6: Screen09 — move "Reveal my EQ Stage" button to directly under "Your EQ stage is ready" heading
# Remove existing button placement at bottom
c = c.replace(
    '    <p class="tier-tease-label">Where do you fall?</p>\n\n    <div style="text-align:center;margin-bottom:24px;"><button class="btn-gold" onclick="show(\'screen10\')" style="font-size:15px;padding:14px 36px;">Reveal my EQ Stage \u2014 Free</button></div>',
    '    <p class="tier-tease-label">Where do you fall?</p>'
)
# Add button right after the "Your EQ stage is ready" heading
c = c.replace(
    '    <h2 class="headline" style="font-size:clamp(28px,6vw,44px);margin-bottom:24px;">Your EQ stage is ready.</h2>',
    '    <h2 class="headline" style="font-size:clamp(28px,6vw,44px);margin-bottom:24px;">Your EQ stage is ready.</h2>\n\n    <div style="text-align:center;margin-bottom:28px;"><button class="btn-gold" onclick="show(\'screen10\')" style="font-size:15px;padding:14px 36px;">Reveal my EQ Stage \u2014 Free</button></div>'
)
# Remove the old bottom button on screen09
c = c.replace(
    '\n    <button class="btn-gold" onclick="show(\'screen10\')">Reveal my EQ stage</button>',
    ''
)

f = open('eq-audit-v9.html', 'w')
f.write(c)
f.close()
print('All done')
