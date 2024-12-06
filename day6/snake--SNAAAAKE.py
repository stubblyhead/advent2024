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
                    found_guard = True
                    self.visited.add([row,col])
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

    def guard_move(self):
        def next_space(self):  # determine what the next space is based on current direction of travel
            if self.guard_dir == 'up':
                return [self.guard_row-1,self.guard_col]
            elif self.guard_dir == 'right':
                return [self.guard_row,self.guard_col+1]
            elif self.guard_dir == 'down':
                return [self.guard_row+1,self.guard_col]
            elif self.guard_dir == 'left':
                return [self.guard_row,self.guard_col-1]
            
        next = next_space()
        if self.grid[next[0]][next[1]] == '#':  # turn right if the next space ahead is an obstacle
            self.guard_turn()
            return
        
        if next[0] in [-1,self.height] or next[1] in [-1,self.width]:  # if next space is OOB then mark exited and return
            self.guard_exited = True
            return
        
        # otherwise update current position and add to set of visited spaces
        [self.guard_row, self.guard_col] = next
        self.visited.add(next)



    

    