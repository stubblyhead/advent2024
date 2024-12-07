lines = open('testcase').readlines()

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

for k,v in eqns:
    perm = len(v) - 1
    for i in range(pow(2,perm)):
        binstr = '{:>0{length}}'.format(bin(i),length=perm)
        

