import regex as re
import numpy as np

games = open('input').read().split('\n\n')

coins = 0
pattern = '\d+'
count = 0
for g in games:
    numbers = [ int(i) for i in re.findall(pattern, g) ]
    a_x, a_y, b_x, b_y, prize_x, prize_y = numbers
    
    # it's all simultaneous equations-- a_x*x + b_x*x = prize_x*x, a_y*y + b_y*y = prize_y*y; solve for x and y
    buttons = np.array([[a_x, b_x],[a_y,b_y]])
    prize = np.array([prize_x, prize_y])
    solution = np.linalg.solve(buttons, prize)
    if np.allclose(np.round(solution).astype(int),solution):
        count += 1
        coins += (solution[0]*3 + solution[1])
        
    
print(f'{count} of {len(games)} have a solution')
print(coins)

coins = 0
count = 0
for g in games:
    numbers = [ int(i) for i in re.findall(pattern, g) ]
    a_x, a_y, b_x, b_y, prize_x, prize_y = numbers
    
    # it's all simultaneous equations-- a_x*x + b_x*x = prize_x*x, a_y*y + b_y*y = prize_y*y; solve for x and y
    buttons = np.array([[a_x, b_x],[a_y,b_y]])
    prize = np.array([prize_x+10000000000000, prize_y+10000000000000])
    solution = np.linalg.solve(buttons, prize)
    rounded = np.round(solution).astype(int)
    if np.allclose(rounded,solution,rtol=1e-15):
        count += 1
        coins += (rounded[0]*3 + rounded[1])
        # print(solution[0], solution[1])
print(f'{count} of {len(games)} have a solution')
print(coins)