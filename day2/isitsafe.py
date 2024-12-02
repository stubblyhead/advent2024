reports = open('input').readlines()

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

def is_safe(report):
    """
    in: report as list of ints
    out: True if report is safe, False otherwise
    """
    safe = True
    increasing = None
    if report[0] > report[-1]:  #generally decreasing
            increasing = False
    elif report[0] < report[-1]:  #generally increasing
            increasing = True
    else:  #generally static (not safe), so go to next report
        return False
    if increasing:
        for n in range(len(report)-1): #compare the current number to the next number
            diff = report[n+1]-report[n]
            if diff > 3 or diff <= 0: #delta is more than two or is static or decreasing
                safe = False  #report is unsafe, so we can stop checking this one
                break 
    else:
        for n in range(len(report)-1): #now do the same thing but check for decreasing
            diff = report[n]-report[n+1]
            if diff > 3 or diff <= 0: 
                safe = False
                break 
    return safe


#part 2
safecount = 0
for r in reports:
    levels = list(map(int,r.split()))
    safe = is_safe(levels)
    if safe:  #if the list is safe as-is, no need to do anything further
        safecount += 1
    else:  #remove each element in turn.  if any of these are safe, then the full report is safe as well
        for i in range(len(levels)):
            if is_safe(levels[0:i]+levels[i+1:]):
                safecount += 1
                break

print(safecount)