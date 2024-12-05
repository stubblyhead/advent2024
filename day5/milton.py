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
        if r[0] in m and r[1] in m:  # if m contains both elements of r...
            if (m.index(r[0]) < m.index(r[1])):  # ...and the first element of r comes first
                next  # go to next rule, this one is in compliance
            else:
                valid = False  # otherwise manual is not valid so we can skip the rest of the rules
                break
        # don't need to do anything if manual doesn't contain all in r

    if valid:
        count += m[int(len(m)/2)]

print(count)