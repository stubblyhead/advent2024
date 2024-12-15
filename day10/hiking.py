lines = open('testcase').readlines()
grid = []
for l in lines:  # going to try padding grid in an attempt to avoid OOB errors
    grid.append([-1] + list(map(int,l.strip())) + [-1])
grid = [[ -1 for _ in range(len(grid[0])) ]] + grid + [[ -1 for _ in range(len(grid[0])) ]]

def bfs(g, root):
    horizon = [root]
    nines = set()
    while horizon:
        cur_row,cur_col = horizon.pop(0)
        cur_val = g[cur_row][cur_col]
        if cur_val == 9:
            nines.add((cur_row,cur_col))
            continue
        if g[cur_row+1][cur_col] == cur_val + 1:
            horizon.append([cur_row+1,cur_col])
        if g[cur_row-1][cur_col] == cur_val + 1:
            horizon.append([cur_row-1,cur_col])
        if g[cur_row][cur_col+1] == cur_val + 1:
            horizon.append([cur_row,cur_col+1])
        if g[cur_row][cur_col-1] == cur_val + 1:
            horizon.append([cur_row,cur_col-1])
    return len(nines)

count = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[col][row] == 0:
            count += bfs(grid, [col,row])

print(count)
    
        
            
