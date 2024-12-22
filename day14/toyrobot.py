filename = 'input'
lines = open(filename).readlines()
if filename == 'testcase':
    size = (7,11)
else:
    size = (103,101)

hh = int(size[0]/2)
hw = int(size[1]/2)

class Robot:
    def __init__(self, p, v):
        self.x, self.y = p
        self.dx, self.dy = v

    def move(self, seconds, size):
        h,w = size
        self.x = (self.x+seconds*self.dx) % w
        self.y = (self.y+seconds*self.dy) % h
    
ul,ur,ll,lr = 0,0,0,0
for l in lines:
    p,v = l.split()
    pos = tuple(map(int, p[2:].split(',')))
    vel = tuple(map(int,v[2:].split(',')))
    cur = Robot(pos,vel)
    cur.move(100,size)
    if cur.x < hw and cur.y < hh:
        ll += 1
    elif cur.x < hw and cur.y > hh:
        ul += 1
    elif cur.x > hw and cur.y < hh:
        lr += 1
    elif cur.x > hw and cur.y > hh:
        ur += 1
print(ll*lr*ur*ul)