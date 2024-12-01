lines = open('testcase')

left = []
right = []

for l in lines:
    parts = l.split()
    left.append(int(parts[0]))
    right.append(int(parts[1]))

left.sort()
right.sort()

dist = 0
for i in range(len(left)):
    dist += abs(left[i] - right[i])
print(dist)