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

