warehouse, moves = list(open('testcase1').read().split('\n\n'))
warehouse = [ list(w.strip()) for w in warehouse.split() ]

for row in range(len(warehouse)):
    if warehouse[row].count('@'):
        robot = [row, warehouse[row].index('@')]
        warehouse[robot[0]][robot[1]] = '.'

moves = list(moves)

def move_up(robot,warehouse):
    r,c = robot
    adj = warehouse[r-1][c]
    if adj == '.':
        robot[0] -= 1

    elif adj == '#':
        return
    
    else:
        pass
        #TODO obstacle fuckery

def move_down(robot,warehouse):
    r,c = robot
    adj = warehouse[r+1][c]
    if adj == '.':
        robot[0] += 1

    elif adj == '#':
        return
    
    else:
        pass
        #TODO obstacle fuckery

def move_left(robot,warehouse):
    r,c = robot
    adj = warehouse[r][c-1]
    if adj == '.':
        robot[1] -= 1

    elif adj == '#':
        return
    
    else:
        pass
        #TODO obstacle fuckery

def move_up(robot,warehouse):
    r,c = robot
    adj = warehouse[r][c+1]
    if adj == '.':
        robot[1] += 1

    elif adj == '#':
        return
    
    else:
        pass
        #TODO obstacle fuckery

