warehouse, moves = list(open('input').read().split('\n\n'))
warehouse = [ list(w.strip()) for w in warehouse.split() ]

for row in range(len(warehouse)):
    if warehouse[row].count('@'):
        robot = [row, warehouse[row].index('@')]

moves = list(moves)

def move_up(robot,warehouse):
    r,c = robot
    adj = warehouse[r-1][c]
    if adj == '.':
        robot[0] -= 1
        warehouse[r][c] = '.'
        warehouse[r-1][c] = '@'

    elif adj == '#':
        return
    
    else:
        adj_to_edge = [ i[c] for i in warehouse[r-1::-1] ]
        if adj_to_edge.count('.') == 0:  # nowhere for boxes to go so just quit
            return
        elif adj_to_edge.index('.') < adj_to_edge.index('#'): # there's an empty space between the obstacle and the nearest wall
            warehouse[r-1-adj_to_edge.index('.')][c] = 'O' # adjacent box moves into that empty space
            robot[0] -= 1 # robot moves into new empty space
            warehouse[r][c] = '.'
            warehouse[r-1][c] = '@'

def move_down(robot,warehouse):
    r,c = robot
    adj = warehouse[r+1][c]
    if adj == '.':
        robot[0] += 1
        warehouse[r][c] = '.'
        warehouse[r+1][c] = '@'

    elif adj == '#':
        return
    
    else:
        adj_to_edge = [ i[c] for i in warehouse[r+1:] ]
        if adj_to_edge.count('.') == 0:  # nowhere for boxes to go so just quit
            return
        elif adj_to_edge.index('.') < adj_to_edge.index('#'): # there's an empty space between the obstacle and the nearest wall
            warehouse[r+1+adj_to_edge.index('.')][c] = 'O' # adjacent box moves into that empty space
            robot[0] += 1 # robot moves into new empty space
            warehouse[r][c] = '.'
            warehouse[r+1][c] = '@'

def move_left(robot,warehouse):
    r,c = robot
    adj = warehouse[r][c-1]
    if adj == '.':
        robot[1] -= 1
        warehouse[r][c] = '.'
        warehouse[r][c-1] = '@'

    elif adj == '#':
        return
    
    else:
        adj_to_edge = warehouse[r][c-1::-1]
        if adj_to_edge.count('.') == 0:  # nowhere for boxes to go so just quit
            return
        elif adj_to_edge.index('.') < adj_to_edge.index('#'): # there's an empty space between the obstacle and the nearest wall
            warehouse[r][c-1-adj_to_edge.index('.')] = 'O' # adjacent box moves into that empty space
            robot[1] -= 1 # robot moves into new empty space
            warehouse[r][c] = '.'
            warehouse[r][c-1] = '@'

def move_right(robot,warehouse):
    r,c = robot
    adj = warehouse[r][c+1]
    if adj == '.':
        robot[1] += 1
        warehouse[r][c] = '.'
        warehouse[r][c+1] = '@'

    elif adj == '#':
        return
    
    else:
        adj_to_edge = warehouse[r][c+1:]
        if adj_to_edge.count('.') == 0:  # nowhere for boxes to go so just quit
            return
        elif adj_to_edge.index('.') < adj_to_edge.index('#'): # there's an empty space between the obstacle and the nearest wall
            warehouse[r][c+1+adj_to_edge.index('.')] = 'O' # adjacent box moves into that empty space
            robot[1] += 1 # robot moves into new empty space
            warehouse[r][c] = '.'
            warehouse[r][c+1] = '@'

def print_warehouse(w):
    for r in range(len(w)):
        print(''.join(w[r]))

for m in moves:
    if m == '>':
        move_right(robot, warehouse)
    elif m == '<':
        move_left(robot, warehouse)
    elif m == '^':
        move_up(robot, warehouse)
    elif m == 'v':
        move_down(robot, warehouse)

coord_sum = 0
for row in range(len(warehouse)):
    for col in range(len(warehouse[row])):
        if warehouse[row][col] == 'O':
            coord_sum = coord_sum + 100*row + col
print(coord_sum)