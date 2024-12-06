lines = open('input').readlines()

rules = []
manuals = []
incorrect_manuals = []

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
                incorrect_manuals.append(m)
                break
        # don't need to do anything if manual doesn't contain all in r

    if valid:
        count += m[int(len(m)/2)]

print(count)

# rules are cylical, not really a single "order," would depend on the pages in the manual
# I think I need to build a page order for each manual, filter out rules that include pages not in the manual

count = 0
for m in incorrect_manuals:
    applicable_rules = []
    for r in rules:
        if r[0] in m and r[1] in m:
            applicable_rules.append(r)
    rule_dict = {}
    left_rules = []
    right_rules = []
    for r in applicable_rules:
        if r[0] in rule_dict.keys():
            rule_dict[r[0]].append(r[1])
        else:
            rule_dict[r[0]] = [r[1]]
            right_rules.append(r[1])
    # pretty sure they're in order by the length of the value arrays in rule_dict?
    order = []
    last = 0
    for i in range(len(m)-1,0,-1):  # for as many times as there are pages in the current manual...
        found = False
        while not found:
            for k,v in rule_dict.items():  # ...check each applicable rule...
                if len(v) == 1: # (but first if there's only one rule)
                    last = v[0] # then it must be the last one in the sequence
                if len(v) == i:  #  ...and if there are as many rules as the current count...
                    order.append(k)  # ...add that page to the order
                    found = True  # can move on to the page with one fewer rules
                    break  # found the one with the most rules, so we can stop looking
    order.append(last)          
    # left_rules = list(rule_dict.keys())
    # order = []
    # while left_rules:
    #     for l in left_rules:
    #         if l not in right_rules:
    #             order.append(l)
    #             for r in rule_dict[l]:
    #                 right_rules.remove(r)
    #             left_rules.remove(l)
    #             break
    count += order[int(len(order)/2)]
    
print(count)


    
