f = open('eq-audit-v9.html', 'r')
lines = f.readlines()
f.close()

out = []
i = 0
while i < len(lines):
    line = lines[i]
    # Remove the eq-reminder-cards block
    if '<div class="eq-reminder-cards">' in line:
        # skip until closing div
        while i < len(lines) and '</div>' not in lines[i]:
            i += 1
        i += 1  # skip the closing div line
        continue
    out.append(line)
    i += 1

f = open('eq-audit-v9.html', 'w')
f.writelines(out)
f.close()
print('Done')
