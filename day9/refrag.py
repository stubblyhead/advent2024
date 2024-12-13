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
filelength = sum(files)
gaplength = sum(freespace)  # upper bound for how many blocks need to move
backfill = []
backfill_total = 0
for i in range(len(files)-1,-1,-1):
    if backfill_total > gaplength:
        break
    backfill.append([i,files[i]])
    backfill_total += files[i]

refragged = []
file_count = len(files)
for i in range(file_count):
    this_files = files.pop(0)
    refragged += [ i for _ in range(this_files) ]
    if freespace:
        this_freespace = freespace.pop(0)
        to_move = []
        if this_freespace == 0:
            continue
        while len(to_move) < this_freespace:
            backfill_val, backfill_count = backfill.pop(0)
            to_move += [ backfill_val for _ in range(min(backfill_count, this_freespace)) ]
        to_move = to_move[:this_freespace]
        extra = backfill_count - to_move.count(backfill_val)
        if extra:
            backfill = [[backfill_val,extra]] + backfill
        refragged += to_move
            
refragged = refragged[:filelength]
checksum = 0
for i in range(len(refragged)):
    checksum += i * refragged[i]

print(checksum)

# part 2, might regret not splitting this into another file

diskmap = list(open('testcase').readline().strip())
files = []
freespace = []
while len(diskmap) > 1:
    files.append(int(diskmap.pop(0)))
    freespace.append(int(diskmap.pop(0)))
files.append(int(diskmap.pop()))

diskmap = []
for i in range(len(freespace)):
    diskmap += [ i for _ in range(files[i]) ]
    diskmap += [ '.' for _ in range(freespace[i] )]
diskmap += [ len(files)-1 for _ in range(files[-1]) ]
print(diskmap)