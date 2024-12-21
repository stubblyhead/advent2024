grid = [ list(i.strip()) for i in open('input').readlines() ]

# padding grid for easier OOB testing
for l in range(len(grid)):
    grid[l] = ['.'] + grid[l] + ['.']

row_pad = [list(''.join(len(grid[0])*'.'))]
grid = row_pad + grid + row_pad

def paint(grid, start):
    """
    given a grid and a starting point, return a list of plots in that region and its perimeter
    """


    row,col = start
    crop = grid[row][col]
    horizon = [start]
    region = set()
    perimeter = 0
    while horizon:
        cur = horizon.pop(0) # get a point off the horizon
        region.add(cur) # add it to the region
        t_row,t_col = cur
        adj = [(t_row-1,t_col),(t_row+1,t_col),(t_row,t_col-1),(t_row,t_col+1)] # spaces in cardinal directions
        for r,c in adj:
            adj_crop = grid[r][c]
            if crop == adj_crop:  # if the adjacent crop is the same as the starting crop
                if (r,c) not in horizon and (r,c) not in region: # and it's not already on the horizon
                    horizon.append((r,c))  # add it to the horizon
            else: # if the crops are different then it's a boundary between regions
                perimeter += 1  # so we need to add a fence
    return {'perimeter': perimeter, 'region': region}

field = []
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] != '.':
            field.append((row,col))
cost = 0
while field:
    plot = field[0]
    ans = paint(grid, plot)
    perimeter = ans['perimeter']
    region = ans['region']
    cost += perimeter * len(region)
    for p in region:
        if p in field:
            field.remove(p)
print(cost)

