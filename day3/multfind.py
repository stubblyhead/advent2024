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

def extract_do(memstr):
    if memstr.count("don't()"):
        dont_start = memstr.index("don't()")
        return memstr[:dont_start]
    else:
        return memstr
def remove_dont(memstr):
    if memstr.count("do()"):
        do_start = memstr.index("do()")
        return memstr[do_start:]
    else:
        return ''

total = 0
mem = open('input').read()

do_part = ''
while len(mem) > 0:
    cur = extract_do(mem)  #get up to the next don't()
    do_part += cur  #add it to the stuff you're supposed to use
    mem = mem[len(cur):]  #remove that from the current line; should now either start with don't() or be empty
    mem = remove_dont(mem)  #get from the next do() to EOL; should now either start with do() or be empty
total += do_mult(do_part)

print(total)


        