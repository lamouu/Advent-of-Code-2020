data = [["y" for x in range(31)] for y in range(323)]

with open('input.txt') as f:
    for yIndex, line in enumerate(f):
        line = line.rstrip()
        for xIndex, char in enumerate(line):
            data[yIndex][xIndex] = char

stepArray = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
collisionList = []
for step in range(5):
    y, x, treeCount = 0, 0, 0
    while y < 323:
        if data[y][x] == "#":
            treeCount += 1
        x += stepArray[step][0]
        if x > 30:
            x = x - 31
        y += stepArray[step][1]
    print(f"Traveling with matrix {stepArray[step]}, you're going to hit {treeCount} trees!")
    
    if step == 0:
        treeProduct = treeCount
    else:
        treeProduct = treeProduct * treeCount

print(f"The product of these is {treeProduct}!")