warehouse, moves = list(open('testcase1').read().split('\n\n'))
warehouse = [ list(w.strip()) for w in warehouse.split() ]

for row in range(len(warehouse)):
    if warehouse[row].count('@'):
        robot = (row, warehouse[row].index('@'))

