from operator import add, mul
def concat(a,b):
    return int(str(a)+str(b))

ops = {'0':add,'1':mul,'2':concat}  # this makes me feel kind of dirty but it beats 10 billion calls to int()
lines = open('testcase').readlines()

def bin(s):
    return str(s) if s<=1 else bin(s>>1) + str(s&1)

def num_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]



eqns = {}
for l in lines:
    a,b = l.split(':')
    eqns[int(a)] = tuple(map(int,b.split()))

total = 0

def check_if_valid(target, operands, base):
    perm = len(eqns[target]) - 1
    found = False
    for i in range(pow(base,perm)):
        this_operands = list(operands) # will let me manipulate list without affecting future iterations
        this_total = 0
        i = num_to_base(i,base)
        binstr = '{:>0{length}}'.format(''.join(map(str,i)),length=perm)
        for j in binstr:
            this_total = ops[j](this_operands[0],this_operands[1])
            this_operands = [this_total]+this_operands[2:]
        if this_operands[0] == target:
            found = True
            break
    return found

for k,v in eqns.items():
    if check_if_valid(k,v,2):
        total += k
print(total)
        
total = 0
for k,v in eqns.items():
    if check_if_valid(k,v,3):
        total += k
print(total)

