# import time
# import statistics

class Grid:
    def __init__(self, lines):
        self.grid = []
        for l in lines:
            self.grid.append(list(l.strip()))
        self.guard_row = 0 
        self.guard_col = 0
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.visited = set()
        self.guard_exited = False

        found_guard = False
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == '^':
                    self.guard_row = row
                    self.guard_col = col
                    self.start_row = row  # need to note this for part 2
                    self.start_col = col
                    found_guard = True
                    self.visited.add(tuple([row,col]))
                    break
            if found_guard:
                break
        self.guard_dir = 'up'

    def guard_turn(self):
        if self.guard_dir == 'up':
            self.guard_dir = 'right'
        elif self.guard_dir == 'right':
            self.guard_dir = 'down'
        elif self.guard_dir == 'down':
            self.guard_dir = 'left'
        elif self.guard_dir == 'left':
            self.guard_dir = 'up'
        self.grid[self.guard_row][self.guard_col] = '+'

    def guard_move(self):
        # def next_space(self):  # determine what the next space is based on current direction of travel
        #     if self.guard_dir == 'up':
        #         return [self.guard_row-1,self.guard_col]
        #     elif self.guard_dir == 'right':
        #         return [self.guard_row,self.guard_col+1]
        #     elif self.guard_dir == 'down':
        #         return [self.guard_row+1,self.guard_col]
        #     elif self.guard_dir == 'left':
        #         return [self.guard_row,self.guard_col-1]
            
        # next = next_space(self)

        if self.guard_dir == 'up':
            while self.guard_row-1 >= 0 and self.grid[self.guard_row-1][self.guard_col] != '#':
                self.guard_row -= 1
                self.visited.add(tuple([self.guard_row,self.guard_col]))
            if self.guard_row == 0:
                self.guard_exited = True
                return
            else:
                self.guard_dir = 'right'
                return
        elif self.guard_dir == 'right':
            while self.guard_col < self.width-1 and self.grid[self.guard_row][self.guard_col+1] != '#':
                self.guard_col += 1
                self.visited.add(tuple([self.guard_row,self.guard_col]))
            if self.guard_col == self.width-1:
                self.guard_exited = True
                return
            else:
                self.guard_dir = 'down'
                return
        elif self.guard_dir == 'down':
            while self.guard_row < self.height-1 and self.grid[self.guard_row+1][self.guard_col] != '#':
                self.guard_row += 1
                self.visited.add(tuple([self.guard_row,self.guard_col]))
            if self.guard_row == self.height-1:
                self.guard_exited = True
                return
            else:
                self.guard_dir = 'left'
                return
        elif self.guard_dir == 'left':
            while self.guard_col-1 >= 0 and self.grid[self.guard_row][self.guard_col-1] != '#':
                self.guard_col -= 1
                self.visited.add(tuple([self.guard_row,self.guard_col]))
            if self.guard_col == 0:
                self.guard_exited = True
                return
            else:
                self.guard_dir = 'up'
                return
        
        # otherwise update current position and add to set of visited spaces
        # [self.guard_row, self.guard_col] = next
        # self.visited.add(tuple(next))
        # if self.guard_dir in ['up','down']:
        #     self.grid[self.guard_row][self.guard_col] = '|'
        # elif self.guard_dir in ['right','left']:
        #     self.grid[self.guard_row][self.guard_col] = '-'

lines = open('input').readlines()
# start = time.time()
my_grid = Grid(lines)
while not my_grid.guard_exited:
    my_grid.guard_move()

# my_grid.grid[my_grid.start_row][my_grid.start_col] = '^'
# for l in my_grid.grid:
#     print(''.join(l))
print(len(my_grid.visited))
# end = time.time()
# print(f'took {end-start}')
searchspace = my_grid.visited.copy() # only need to check visited spaces becuase adding an obstacle outside won't affect guard's movement
# i don't think copy() is strictly necessary here, but I've been bitten enough from not using it that it's probably a good idea anyway
searchspace.remove(tuple([my_grid.start_row, my_grid.start_col]))  # can't use starting position so remove from search space

loop_count = 0
check_count = 0
# durations = []
while searchspace:
    check_count += 1
    # start = time.time()
    cur = searchspace.pop() # get a candidate to check
    my_grid = Grid(lines)  # starting with a fresh instance each time is probably a good idea
    my_grid.grid[cur[0]][cur[1]] = '#' # put an obstacle there
    [my_grid.guard_col,my_grid.guard_row,my_grid.guard_dir] = [my_grid.start_col, my_grid.start_row, 'up'] # put guard back at start
    history = [[my_grid.start_row, my_grid.start_col, 'up']] # add starting position/orientation
    my_grid.guard_exited = False
    while True:
        my_grid.guard_move()
        if my_grid.guard_exited:  # if guard still exits then obstacle didn't cause a loop so move to next candidate
            break
        if [my_grid.guard_row, my_grid.guard_col, my_grid.guard_dir] in history:  # if guard is in same position and direction for a second time then they must be in a loop so add to count and move to next
            loop_count += 1
            # my_grid.grid[my_grid.start_row][my_grid.start_col] = '^'
            # my_grid.grid[cur[0]][cur[1]] = 'O'
            #print(f'adding {cur} to list:')
            # for l in my_grid.grid:
            #     print(''.join(l))
            # print('\n\n')
            break
        history.append([my_grid.guard_row,my_grid.guard_col,my_grid.guard_dir])
    #my_grid.grid[my_grid.start_row][my_grid.start_col] = '^'
    # durations.append(time.time() - start)

    
    
    
    # don't need to do this anymore since I'm using a new grid every time
    # my_grid.grid[cur[0]][cur[1]] = '.' # remove obstacle before moving to the next candidate

print(loop_count)
# print(f'max time: {max(durations)}, min time:{min(durations)}, average: {statistics.mean(durations)}, std dev: {statistics.stdev(durations)}')