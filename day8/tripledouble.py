lines = open('testcase1').readlines()

# i thought it was about pythagorean triples but it's not really at least not exclusively

frequencies = {}

grid = [ list(l.strip()) for l in lines ]

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] != '.':
            try:
                frequencies[grid[row][col]].append((row,col))
            except KeyError:
                frequencies[grid[row][col]] = [(row,col)]
print(frequencies)

antinodes = set()

for _, sites in frequencies.items():
    for i in range(len(sites)-1):  
        for j in range(i+1,len(sites)):  # should do a round robin of each group of points
            # TODO get delta_x and delta_y between two points; find point 
            # that far away on opposite side of other point
            delta_row = sites[i][0] - sites[j][0]
            delta_col = sites[i][1] - sites[j][1]
            print(sites[i][0]-delta_row, sites[i][1] - delta_row)
            print(sites[j][0]-delta_row, sites[j][1] - delta_row)
            # TODO add those points to antinodes set, then remove any with either coordinate
            # < 0 or > max.  then length should be number of antinodes