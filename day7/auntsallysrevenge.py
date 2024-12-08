from operator import sub, div
def concat(a,b):
    return int(str(a)+str(b))

lines = open('input').readlines()

eqns = {}
for l in lines:
    a,b = l.split(':')
    eqns[int(a)] = tuple(map(int,b.split()))

def num_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def check_valid(target, operands, base):
    ops = {'0':add,'1':mul,'2':concat}  # this makes me feel kind of dirty but it beats 10 billion calls to int()
    perms = pow(base,len(operands)-1)
    for perm in perms:
        this_target = target
        this_operands = list(operands) # will let me manipulate list without affecting future iterations
        
        perm = num_to_base(perm,base)
        for i in perm:
            bust = False
            if i == 0:  # addition
                this_target -= this_operands.pop()  # subtract last number in operands
                if this_target < 0:  # if it's less than zero this isn't a valid permutation
                    bust = True
                    break
            elif i == 1: # multiplication
                last_num = this_operands.pop()
                if this_target % last_num != 0: # if running total isn't evenly divisible by the last number it's not a valid permutation
                    bust = True
                    break
                else:
                    this_target //= last_num
            elif i == 2:  # concatenation
                last_num = str(this_operands.pop()) # convert last number to a string
                if last_num != this_target[len(last_num):]:
                    bust = True
                    break
                else:
                    this_target = this_target[:len(last_num)]
        if bust:
            return False
        elif this_target == operands[0]:
            return True
        else:
            return False
        

                
