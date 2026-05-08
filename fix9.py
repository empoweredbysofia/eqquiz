f = open('eq-audit-v9.html', 'r')
lines = f.readlines()
f.close()

out = []
i = 0
while i < len(lines):
    # Find the second emoji grid (the one with flex:1;min-width:80px)
    if 'flex:1;min-width:80px' in lines[i] and 'display:flex;gap:8px' in lines[max(0,i-1)]:
        # go back and remove the opening div too
        out.pop()  # remove the opening div line
        # skip until closing div
        while i < len(lines) and '</div>' not in lines[i]:
            i += 1
        i += 1  # skip closing div
        continue
    out.append(lines[i])
    i += 1

f = open('eq-audit-v9.html', 'w')
f.writelines(out)
f.close()
print('Done')
