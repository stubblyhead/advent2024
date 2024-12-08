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
    places = len(operands)-1
    perms = pow(base,places)
    for perm in range(perms):
        this_target = target
        this_operands = list(operands) # will let me manipulate list without affecting future iterations
        
        perm = num_to_base(perm,base)
        if base == 3 and 2 not in perm:  # can skip this permutation if there's no concatenation because we already checked it
            continue  
        for _ in range(places-len(perm)):
            perm = [0] + perm
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
                if last_num != str(this_target)[len(str(this_target))-len(last_num):]:
                    bust = True
                    break
                else:
                    this_target = int(str(this_target)[:len(last_num)+1])
        if bust:
            next
        elif this_target == operands[0]:
            return True
        # else:
        #     return False
        
total = 0
valid = []
for k,v in eqns.items():
    if check_valid(k,v,2):
        valid.append(k)  # keep track of valid equations so we can remove them later
        total += k
print(total)
for i in valid:
    eqns.pop(i)  # remove the ones we already know are valid

total2 = 0
for k,v in eqns.items():
    if check_valid(k,v,3):
        # print(f'{k}: {v} is valid')
        total2+= k
    # else:
        # print(f'{k}: {v} is not valid')
print(total+total2)
                
