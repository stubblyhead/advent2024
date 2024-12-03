import regex as re

mem = open('input').readlines()
def do_mult(memstr):
    pattern = "mul\(\d+,\d+\)"
    total = 0
    matches = re.findall(pattern, memstr)
    for i in matches:
        args = i[4:-1].split(',')
        total += int(args[0]) * int(args[1])
    return total

ans = 0
for m in mem:
    ans += do_mult(m)
print(ans)

print(total)