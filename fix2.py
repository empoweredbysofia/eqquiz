f = open('eq-audit-v9.html', 'r')
content = f.read()
f.close()

# FIX 1: Add gold button after "— Sofia" line on screen02 (before EQ definition)
old1 = '    <p class="sofia-attribution">— Sofia</p>\n\n    <p style="font-size:16px;color:var(--ivory);text-align:center;line-height:1.6;max-width:500px;margin-bottom:28px;"><strong style="color:var(--gold);">Emotional Intelligence (EQ)</strong>'
new1 = '    <p class="sofia-attribution">— Sofia</p>\n\n    <div style="text-align:center;margin-bottom:28px;">\n      <button class="btn-gold" onclick="show(\'screen03\')" style="font-size:15px;padding:14px 36px;">Discover your EQ Stage — Free</button>\n    </div>\n\n    <p style="font-size:16px;color:var(--ivory);text-align:center;line-height:1.6;max-width:500px;margin-bottom:28px;"><strong style="color:var(--gold);">Emotional Intelligence (EQ)</strong>'
content = content.replace(old1, new1)

# FIX 2: Add emojis block after EQ definition paragraph, before the life area cards
old2 = 'so they work for you rather than against you.</p>\n\n'
new2 = 'so they work for you rather than against you.</p>\n\n    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:12px;margin-bottom:28px;max-width:480px;">\n      <div style="text-align:center;padding:10px 16px;background:rgba(201,148,58,0.08);border:1px solid rgba(201,148,58,0.2);border-radius:8px;min-width:90px;">\n
cat > fix2.py << 'EOF'
f = open('eq-audit-v9.html', 'r')
content = f.read()
f.close()

# FIX 1: Add gold button after "— Sofia" line on screen02 (before EQ definition)
old1 = '    <p class="sofia-attribution">— Sofia</p>\n\n    <p style="font-size:16px;color:var(--ivory);text-align:center;line-height:1.6;max-width:500px;margin-bottom:28px;"><strong style="color:var(--gold);">Emotional Intelligence (EQ)</strong>'
new1 = '    <p class="sofia-attribution">— Sofia</p>\n\n    <div style="text-align:center;margin-bottom:28px;">\n      <button class="btn-gold" onclick="show(\'screen03\')" style="font-size:15px;padding:14px 36px;">Discover your EQ Stage — Free</button>\n    </div>\n\n    <p style="font-size:16px;color:var(--ivory);text-align:center;line-height:1.6;max-width:500px;margin-bottom:28px;"><strong style="color:var(--gold);">Emotional Intelligence (EQ)</strong>'
content = content.replace(old1, new1)

# FIX 2: Add emojis block after EQ definition paragraph, before the life area cards
old2 = 'so they work for you rather than against you.</p>\n\n'
new2 = 'so they work for you rather than against you.</p>\n\n    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:12px;margin-bottom:28px;max-width:480px;">\n      <div style="text-align:center;padding:10px 16px;background:rgba(201,148,58,0.08);border:1px solid rgba(201,148,58,0.2);border-radius:8px;min-width:90px;">\n        <div style="font-size:20px;margin-bottom:4px;">💼</div>\n        <div style="font-size:11px;color:var(--gold);font-weight:700;letter-spacing:0.05em;">Career</div>\n        <div style="font-size:11px;color:rgba(245,237,216,0.6);">Perform under pressure</div>\n      </div>\n      <div style="text-align:center;padding:10px 16px;background:rgba(201,148,58,0.08);border:1px solid rgba(201,148,58,0.2);border-radius:8px;min-width:90px;">\n        <div style="font-size:20px;margin-bottom:4px;">🚀</div>\n        <div style="font-size:11px;color:var(--gold);font-weight:700;letter-spacing:0.05em;">Business</div>\n        <div style="font-size:11px;color:rgba(245,237,216,0.6);">Lead with clarity</div>\n      </div>\n      <div style="text-align:center;padding:10px 16px;background:rgba(201,148,58,0.08);border:1px solid rgba(201,148,58,0.2);border-radius:8px;min-width:90px;">\n        <div style="font-size:20px;margin-bottom:4px;">📖</div>\n        <div style="font-size:11px;color:var(--gold);font-weight:700;letter-spacing:0.05em;">Study</div>\n        <div style="font-size:11px;color:rgba(245,237,216,0.6);">Focus and believe</div>\n      </div>\n      <div style="text-align:center;padding:10px 16px;background:rgba(201,148,58,0.08);border:1px solid rgba(201,148,58,0.2);border-radius:8px;min-width:90px;">\n        <div style="font-size:20px;margin-bottom:4px;">💍</div>\n        <div style="font-size:11px;color:var(--gold);font-weight:700;letter-spacing:0.05em;">Marriage</div>\n        <div style="font-size:11px;color:rgba(245,237,216,0.6);">Communicate and repair</div>\n      </div>\n      <div style="text-align:center;padding:10px 16px;background:rgba(201,148,58,0.08);border:1px solid rgba(201,148,58,0.2);border-radius:8px;min-width:90px;">\n        <div style="font-size:20px;margin-bottom:4px;">🌱</div>\n        <div style="font-size:11px;color:var(--gold);font-weight:700;letter-spacing:0.05em;">Parenting</div>\n        <div style="font-size:11px;color:rgba(245,237,216,0.6);">Respond, not react</div>\n      </div>\n    </div>\n\n'
content = content.replace(old2, new2)

# FIX 3: Add second button after "Where do you fall?" label
old3 = '    <p class="tier-tease-label">Where do you fall?</p>'
new3 = '    <p class="tier-tease-label">Where do you fall?</p>\n\n    <div style="text-align:center;margin-bottom:24px;">\n      <button class="btn-gold" onclick="show(\'screen10\')" style="font-size:15px;padding:14px 36px;">Reveal my EQ Stage — Free</button>\n    </div>'
content = content.replace(old3, new3)

# FIX 4: Restructure screen14 cards — 2 side by side, 1 below, add membership
old4 = '    <div class="step-cards">'
new4 = '    <div class="step-cards" style="display:grid;grid-template-columns:1fr 1fr;gap:16px;max-width:600px;">'
content = content.replace(old4, new4)

# Add membership card before closing step-cards div
old5 = '      <!-- OPTION 3: 1:1 WITH SOFIA'
new5 = '      <!-- OPTION 3: MEMBERSHIP -->\n      <div class="step-card" id="card-membership" style="grid-column:1 / -1;">\n        <div class="step-card-header">\n          <div class="step-card-icon">🌙</div>\n          <div>\n            <div class="step-card-title">The Reset Room — Membership</div>\n            <div class="step-card-subtitle">Monthly community · Waitlist open</div>\n          </div>\n        </div>\n        <div class="step-card-body">\n          <p>A monthly space for women doing the inner work — live sessions with Sofia, community support, and tools to keep rising.</p>\n          <a href="membership.html" style="text-decoration:none;display:block;">\n            <button class="btn-outline-gold" style="max-width:100%;">Join the waitlist →</button>\n          </a>\n        </div>\n      </div>\n\n      <!-- OPTION 4: 1:1 WITH SOFIA'
content = content.replace(old5, new5)

f = open('eq-audit-v9.html', 'w')
f.write(content)
f.close()
print('Done')
