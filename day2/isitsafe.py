reports = open('testcase').readlines()

safecount = 0
for l in reports:
    levels = list(map(int, l.split()))
    increasing = None
    safe = True #assume list is safe and try to prove it's not
    #going to do this naively though I will probably reget it
    if levels[0] > levels[-1]:  #generally decreasing
        increasing = False
    elif levels[0] < levels[-1]:  #generally increasing
        increasing = True
    else:  #generally static (not safe), so go to next report
        next
    if increasing:
        for n in range(len(levels)-1): #compare the current number to the next number
            diff = levels[n+1]-levels[n]
            if diff > 3 or diff <= 0: #delta is more than two or is static or decreasing
                safe = False  #report is unsafe, so we can stop checking this one
                break 
    else:
        for n in range(len(levels)-1): #now do the same thing but check for decreasing
            diff = levels[n]-levels[n+1]
            if diff > 3 or diff <= 0: 
                safe = False
                break 
    if safe:  #didn't find a reason to mark the report unsafe
        safecount += 1 

print(safecount)

#part 2
safecount = 0
for r in reports:
    levels = list(map(int,r.split()))
    safe = True  #still assume true and try to prove false
    damped = False #keep track of if damper has triggered for this report
    increasing = None #don't really like how I'm doing this, feels yucky
    if levels[0] > levels[-1]:  #generally decreasing
            increasing = False
    elif levels[0] < levels[-1]:  #generally increasing
            increasing = True
    else:  #generally static (not safe), so go to next report
        next
    
    while len(levels) > 1:
        cur = levels.pop() #get one off the end
        if increasing:
            if cur-levels[-1] in [1,2,3]: #last two differ by at least one and no more than three
                continue #can check new last pair
        else:
            if levels[-1]-cur in [1,2,3]:
                continue
        if damped:
            safe = False #second unsafe level change for this report, so entire report is unsafe
            break #don't need to keep checking this one
        else:
            levels[-1] = cur #replace last item with one we popped previously and try again
            damped = True
    if safe:
        safecount += 1

print(safecount)