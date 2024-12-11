lines = open('input').readlines()

# i thought it was about pythagorean triples but it's not really at least not exclusively

frequencies = {}

grid = [ list(l.strip()) for l in lines ]
height = len(grid)
width = len(grid[0])

for row in range(height):
    for col in range(width):
        if grid[row][col] != '.':
            try:
                frequencies[grid[row][col]].append((row,col))
            except KeyError:
                frequencies[grid[row][col]] = [(row,col)]

antinodes = set()

for _, sites in frequencies.items():
    for i in range(len(sites)-1):  
        for j in range(i+1,len(sites)):  # should do a round robin of each group of points
            point_a,point_b = sites[i],sites[j]
            delta_x = point_a[0] - point_b[0]
            delta_y = point_a[1] - point_b[1]
            antinode_a = (point_a[0] + delta_x, point_a[1] + delta_y)
            antinode_b = (point_b[0] - delta_x, point_b[1] - delta_y)
            antinodes.update({antinode_a, antinode_b})

to_remove = []
for a in antinodes:
    if a[0] < 0 or a[0] >= height or a[1] < 0 or a[1] >= width:
        to_remove.append(a)

for i in to_remove:
    antinodes.remove(i)

print(len(antinodes))

for _, sites in frequencies.items():
    for i in range(len(sites)-1):  
        for j in range(i+1,len(sites)):  
            point_a,point_b = list(sites[i]),list(sites[j])
            delta_x = point_a[0] - point_b[0]
            delta_y = point_a[1] - point_b[1]
            antinodes.add(tuple(point_a))
            while point_a[0] >= 0 and point_a[0] < height and point_a[1] >= 0 and point_a[1] < width:
                point_a[0] += delta_x
                point_a[1] += delta_y
                antinodes.add(tuple(point_a))
            point_a = list(sites[i])
            while point_a[0] >= 0 and point_a[0] < height and point_a[1] >= 0 and point_a[1] < width:
                point_a[0] -= delta_x
                point_a[1] -= delta_y
                antinodes.add(tuple(point_a))
            
to_remove = []
for a in antinodes:
    if a[0] < 0 or a[0] >= height or a[1] < 0 or a[1] >= width:
        to_remove.append(a)

for i in to_remove:
    antinodes.remove(i)
print(len(antinodes))
