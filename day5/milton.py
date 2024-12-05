lines = open('testcase').readlines()

rules = []
manuals = []

for l in lines:
    if l.count('|'):  # I don't think we really need to cast as int at this point, but maybe in part 2
        rules.append(list(map(int, l.split('|'))))
    elif l.count(','):
        manuals.append(list(map(int, l.split(','))))
    else:
        next

count = 0

for m in manuals:
    valid = True  # assume valid
    for r in rules:
        if r[0] in m and r[1] in m and (m.index(r[0]) < m.index(r[1])):
            next
        else:
            valid = False

        if valid:
            count += m[int(len(m)/2)]

print(count)