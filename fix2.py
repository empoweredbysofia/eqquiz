f = open('eq-audit-v9.html', 'r')
c = f.read()
f.close()

# FIX 1: Button after "— Sofia" on screen02
c = c.replace(
    '<p class="sofia-attribution">— Sofia</p>',
    '<p class="sofia-attribution">— Sofia</p>\n\n    <div style="text-align:center;margin-bottom:28px;"><button class="btn-gold" onclick="show(\'screen03\')" style="font-size:15px;padding:14px 36px;">Discover your EQ Stage \u2014 Free</button></div>',
    1
)

# FIX 2: Emoji cards after EQ definition
c = c.replace(
    'so they work for you rather than against you.</p>',
    'so they work for you rather than against you.</p>\n\n    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:12px;margin-bottom:28px;max-width:480px;margin-left:auto;margin-right:auto;"><div style="text-align:center;padding:10px 16px;background:rgba(201,148,58,0.08);border:1px solid rgba(201,148,58,0.2);border-radius:8px;min-width:90px;"><div style="font-size:20px;margin-bottom:4px;">\U0001f4bc</div><div style="font-size:11px;color:var(--gold);font-weight:700;">Career</div><div style="font-size:11px;color:rgba(245,237,216,0.6);">Perform under pressure</div></div><div style="text-align:center;padding:10px 16px;background:rgba(201,148,58,0.08);border:1px solid rgba(201,148,58,0.2);border-radius:8px;min-width:90px;"><div style="font-size:20px;margin-bottom:4px;">\U0001f680</div><div style="font-size:11px;color:var(--gold);font-weight:700;">Business</div><div style="font-size:11px;color:rgba(245,237,216,0.6);">Lead with clarity</div></div><div style="text-align:center;padding:10px 16px;background:rgba(201,148,58,0.08);border:1px solid rgba(201,148,58,0.2);border-radius:8px;min-width:90px;"><div style="font-size:20px;margin-bottom:4px;">\U0001f4d6</div><div style="font-size:11px;color:var(--gold);font-weight:700;">Study</div><div style="font-size:11px;color:rgba(245,237,216,0.6);">Focus and believe</div></div><div style="text-align:center;padding:10px 16px;background:rgba(201,148,58,0.08);border:1px solid rgba(201,148,58,0.2);border-radius:8px;min-width:90px;"><div style="font-size:20px;margin-bottom:4px;">\U0001f48d</div><div style="font-size:11px;color:var(--gold);font-weight:700;">Marriage</div><div style="font-size:11px;color:rgba(245,237,216,0.6);">Communicate and repair</div></div><div style="text-align:center;padding:10px 16px;background:rgba(201,148,58,0.08);border:1px solid rgba(201,148,58,0.2);border-radius:8px;min-width:90px;"><div style="font-size:20px;margin-bottom:4px;">\U0001f331</div><div style="font-size:11px;color:var(--gold);font-weight:700;">Parenting</div><div style="font-size:11px;color:rgba(245,237,216,0.6);">Respond, not react</div></div></div>'
)

# FIX 3: Button after "Where do you fall?"
c = c.replace(
    '<p class="tier-tease-label">Where do you fall?</p>',
    '<p class="tier-tease-label">Where do you fall?</p>\n\n    <div style="text-align:center;margin-bottom:24px;"><button class="btn-gold" onclick="show(\'screen10\')" style="font-size:15px;padding:14px 36px;">Reveal my EQ Stage \u2014 Free</button></div>'
)

# FIX 4: Grid layout for step cards
c = c.replace(
    '<div class="step-cards">',
    '<div class="step-cards" style="display:grid;grid-template-columns:1fr 1fr;gap:16px;max-width:600px;margin:0 auto;">'
)

# FIX 5: Add membership card + make 1:1 full width
c = c.replace(
    '<!-- OPTION 3: 1:1 WITH SOFIA',
    '<!-- OPTION 3: MEMBERSHIP -->\n      <div class="step-card" id="card-membership" style="grid-column:1/-1;">\n        <div class="step-card-header"><div class="step-card-icon">\U0001f319</div><div><div class="step-card-title">The Reset Room \u2014 Membership</div><div class="step-card-subtitle">Monthly community \u00b7 Waitlist open</div></div></div>\n        <div class="step-card-body"><p>A monthly space for women doing the inner work \u2014 live sessions with Sofia, community support, and tools to keep rising.</p><a href="membership.html" style="text-decoration:none;display:block;"><button class="btn-outline-gold" style="max-width:100%;">Join the waitlist \u2192</button></a></div>\n      </div>\n\n      <!-- OPTION 4: 1:1 WITH SOFIA'
)

f = open('eq-audit-v9.html', 'w')
f.write(c)
f.close()
print('All done')
