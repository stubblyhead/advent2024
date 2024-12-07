from operator import add, mul
ops = {'0':add,'1':mul}  # this makes me feel kind of dirty but it beats 10 billion calls to int()
lines = open('input').readlines()

def bin(s):
    return str(s) if s<=1 else bin(s>>1) + str(s&1)

eqns = {}
for l in lines:
    a,b = l.split(':')
    eqns[int(a)] = list(map(int,b.split()))

"""
TODO need to potentially check all combinations of + and *.
strategy--2^n possible combinations where n = len(rhs)-1,
so iterate through that many times, shifting off bits as we 
go.  probably won't scale well for large n, but should be 
some ways to mitigate that.  maybe leverage operator module?
might be too inefficient to make so many function calls.
"""

total = 0

for target in eqns.keys():
    perm = len(eqns[target]) - 1
    found = False
    for i in range(pow(2,perm)):
        operands = eqns[target] # will let me manipulate list without affecting future iterations
        this_total = 0
        binstr = '{:>0{length}}'.format(bin(i),length=perm)
        for i in binstr:
            this_total = ops[i](operands[0],operands[1])
            operands = [this_total]+operands[2:]
        if operands[0] == target:
            total += target
            found = True
        if found:
            break

print(total)
        

