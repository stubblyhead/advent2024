diskmap = list(open('testcase').readline().strip())

# making it a single string seems like a trap, but i might end up
# doing it anyway
files = []
freespace = []

# split diskmap into data and freespace lists
while len(diskmap) > 1:
    files.append(int(diskmap.pop(0)))
    freespace.append(int(diskmap.pop(0)))
files.append(int(diskmap.pop()))

print(files, freespace)
gaplength = sum(freespace)  # upper bound for how many blocks need to move
backfill = []
rev_files = files[::-1]
backfill_total = 0
for i in range(len(files)-1,-1,-1):
    if backfill_total > gaplength:
        break
    backfill_total.append([i,])