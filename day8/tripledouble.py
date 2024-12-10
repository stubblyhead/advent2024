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
            # TODO get delta_x and delta_y between two points; find point 
            # that far away on opposite side of other point
            point_a,point_b = sites[i],sites[j]
            if point_a[0] > point_b[1]:
                delta_x = point_a[0] - point_b[0]
                delta_y = point_a[1] - point_b[1]
                antinode_a = [point_a[0] + delta_x, point_a[1] + delta_y]
                antinode_b = [point_b[0] - delta_x, point_b[1] - delta_y]
            else:
                delta_x = point_b[0] - point_a[0]
                delta_y = point_b[1] - point_a[1]
                antinode_a = [point_a[0] - delta_x, point_a[1] - delta_y]
                antinode_b = [point_b[0] + delta_x, point_b[1] + delta_y]

            antinodes.add(tuple(antinode_a))
            antinodes.add(tuple(antinode_b))

to_remove = []
for a in antinodes:
    if a[0] < 0 or a[0] >= height or a[1] < 0 or a[1] >= width:
        to_remove.append(a)

for i in to_remove:
    antinodes.remove(i)

print(len(antinodes))