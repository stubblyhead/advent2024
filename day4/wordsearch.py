#calling it now, part 2 will be with rows/cols wrapping around

class Grid:
    def __init__(self, lines):
        self.grid = []
        for l in lines:
            self.grid.append(list(l.strip()))
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def valid_dirs(self, row, col):
        """
        in: row and column of 'X' character
        out: list of valid directions to look for word going clockwise from upper left
        """
        u = row-3 >= 0
        d = self.height-row >= 4
        l = col-3 >= 0
        r = self.width-col >= 4
        return [u and l, u, u and r, r, d and r, d, d and l, l]
    
    def get_xmas_count(self,row,col):
        valid = self.valid_dirs(row,col)
        count = 0
        word = ''  # i hate this, but I'm not sure how else to do it
        if valid[0]:   # up and left
            word = self.grid[row][col]  
            t_row,t_col = row,col
            for i in range(3):
                t_row -= 1
                t_col -= 1
                word += self.grid[t_row][t_col]
            if word == 'XMAS':
                count += 1
       
        if valid[1]:  # up
            word = self.grid[row][col]
            t_row = row
            for i in range(3):
                t_row -= 1
                word += self.grid[t_row][col]
            if word == 'XMAS':
                count += 1
        
        if valid[2]:  # up and right
            word = self.grid[row][col]
            t_row,t_col = row,col
            for i in range(3):
                t_row -= 1
                t_col += 1
                word += self.grid[t_row][t_col]
            if word == 'XMAS':
                count += 1

        if valid[3]:  # right
            word = self.grid[row][col]
            t_col = col
            for i in range(3):
                t_col += 1
                word += self.grid[row][t_col]
            if word == 'XMAS':
                count += 1

        if valid[4]:  # down and right
            word = self.grid[row][col]
            t_col,t_row = col,row
            for i in range(3):
                t_col += 1
                t_row += 1
                word += self.grid[t_row][t_col]
            if word == 'XMAS':
                count += 1

        if valid[5]:  # down
            word = self.grid[row][col]
            t_row,t_col = row,col
            for i in range(3):
                t_row += 1
                word += self.grid[t_row][col]
            if word == 'XMAS':
                count += 1
       
        if valid[6]:  # down and left
            word = self.grid[row][col]
            t_row, t_col = row, col
            for i in range(3):
                t_row += 1
                t_col -= 1
                word += self.grid[t_row][t_col]
            if word == 'XMAS':
                count += 1
        
        if valid[7]:  # left
            word = self.grid[row][col]
            t_col = col
            for i in range(3):
                t_col -= 1
                word += self.grid[row][t_col]
            if word == 'XMAS':
                count += 1
        return count


lines = open('testcase').readlines()
my_grid = Grid(lines)
count = 0
for row in range(len(my_grid.grid)):
    for col in range(len(my_grid.grid[0])):
        if my_grid.grid[row][col] == 'X':
            count += my_grid.get_xmas_count(row,col)

print(count)