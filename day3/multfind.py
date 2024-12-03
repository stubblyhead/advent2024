import regex as re

mem = open('input').readlines()

pattern = "mul\(\d+,\d+\)"
total = 0
for m in mem:
    matches = re.findall(pattern, m)
    for i in matches:
        args = i[4:-1].split(',')
        total += int(args[0]) * int(args[1])

print(total)