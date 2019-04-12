# this gives the exact same output requested.
# hackerrank, however, isn't quite happy with this output...

# this is more of an example of a recursive algo in python

def findfruit(x,y):
    node = []
    global found
    if found:
        return 
    pacMan[0] = x
    pacMan[1] = y
    if grid[x][y] == '.':
        found = True
        return
    if grid[x][y] == '%':
        return
    if grid[x][y] == 2:
        return
    grid[x][y] = 2
    node = [x,y]
    node_list.append(node)
    findfruit(x + 1, y)
    findfruit(x, y + 1)
    findfruit(x - 1, y)
    findfruit(x, y - 1)



def printnodes():
    print(len(node_list)+1)
    for item in node_list:
        print('{0} {1}'.format(item[0],item[1]))
    print('{0} {1}'.format(fruit[0],fruit[1]))


pacMan = [int(i) for i in input().split(' ')]
fruit = [int(i) for i in input().split(' ')]
grid_dimensions = [int(i) for i in input().split(' ')]
grid = [[j for j in input().strip()] for i in range(grid_dimensions[0])]
node_list = []
found = False
findfruit(pacMan[0],pacMan[1])
if found == True:
    printnodes()
