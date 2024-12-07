lines = open('testcase').readlines()

eqns = {}
for l in lines:
    a,b = l.split(':')
    eqns[int(a)] = list(map(int,b.split()))

