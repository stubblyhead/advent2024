test1 = '0 1 10 99 999'
test2 = '125 17'
input = '8069 87014 98 809367 525 0 9494914 5'
from math import log, floor

stones = list(map(int,input.split()))

# this will probably require an absurd number of calcs; memoization might be a good idea

def get_left_half(num):
    if floor(log(num,10)) % 2 == 1:
        p = floor(log(num,10))
        l = num // pow(10,p//2+1)
        return l


    else:
        return -1

for _ in range(25):
    new_stones = []
    for i in stones:
        if i == 0:
            new_stones += [1]
        elif floor(log(i,10)) % 2 == 1:
            p = floor(log(i,10))
            l = i // pow(10,p//2+1)
            r = i-l*pow(10,p//2+1)
            new_stones += [l,r]
        else:
            new_stones += [i * 2024]
    stones = new_stones

print(len(stones))