f = open('eq-audit-v9.html', 'r')
lines = f.readlines()
f.close()

out = []
i = 0
while i < len(lines):
    line = lines[i]

    # FIX 1: Insert Keep going button after "— Sofia" line on screen05
    if '    <p class="sofia-attribution">— Sofia</p>' in line and i < 860:
        out.append(line)
        out.append('\n')
        out.append('    <div style="text-align:center;margin:20px 0;"><button class="btn-gold" onclick="show(\'screen06\'); renderQuizBlock(\'b\')" style="font-size:15px;padding:14px 36px;">Keep going</button></div>\n')
        out.append('\n')
        i += 1
        continue

    # FIX 2: Insert Almost there button after "200+ women" line on screen07
    if '200+ women have already taken the EQ Audit' in line:
        out.append(line)
        out.append('\n')
        out.append('    <div style="text-align:center;margin:24px 0;"><button class="btn-gold" onclick="show(\'screen08\'); renderQuizBlock(\'c\')" style="font-size:15px;padding:14px 36px;">Almost there \u2014 finish your audit</button></div>\n')
        out.append('\n')
        i += 1
        continue

    # FIX 3: Remove old Almost there button at bottom of screen07
    if 'Almost there' in line and 'btn-gold' in line and 'renderQuizBlock' in line:
        i += 1
        continue

    out.append(line)
    i += 1

f = open('eq-audit-v9.html', 'w')
f.writelines(out)
f.close()
print('Done')
