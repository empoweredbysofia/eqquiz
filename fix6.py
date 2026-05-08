f = open('eq-audit-v9.html', 'r')
lines = f.readlines()
f.close()

out = []
i = 0
while i < len(lines):
    line = lines[i]

    # Remove the wrongly added Keep going button on screen02 (line ~724, before screen05)
    if 'text-align:center;margin:20px 0' in line and 'Keep going' in line and i < 830:
        i += 1
        # skip blank line after it too
        if i < len(lines) and lines[i].strip() == '':
            i += 1
        continue

    # Remove the OLD plain Keep going button on screen05 (the one without styling)
    if line.strip() == '<button class="btn-gold" onclick="show(\'screen06\'); renderQuizBlock(\'b\')">Keep going</button>':
        i += 1
        continue

    out.append(line)
    i += 1

f = open('eq-audit-v9.html', 'w')
f.writelines(out)
f.close()
print('Done')
