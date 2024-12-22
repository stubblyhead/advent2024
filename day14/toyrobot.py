filename = 'testcase'
lines = open(filename).readlines()
if filename == 'testcase':
    size = (7,11)
else:
    size = (103,101)

class Robot:
    def __init__(self, p, v):
        self.x, self.y = p
        self.dx, self.dy = v

    def move(self, seconds, size):
        h,w = size
        self.x = (self.x+seconds*self.dx) % w
        self.y = (self.y+seconds*self.dy) % h
    

#for l in lines:
for _ in range(1):
    p,v = "p=2,4 v=2,-3".split()
    pos = tuple(map(int, p[2:].split(',')))
    vel = tuple(map(int,v[2:].split(',')))
    cur = Robot(pos,vel)
    cur.move(3,size)
    print(cur.x,cur.y)