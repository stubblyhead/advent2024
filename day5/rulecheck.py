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

pages = []
for r in rules:
    if r[0] not in pages:
        pages.append(r[0])


print(pages)
