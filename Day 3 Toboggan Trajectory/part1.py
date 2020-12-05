data = [["y" for x in range(31)] for y in range(323)]

with open('input.txt') as f:
    for yIndex, line in enumerate(f):
        line = line.rstrip()
        for xIndex, char in enumerate(line):
            data[yIndex][xIndex] = char

y, x, treeCount = 0, 0, 0
while y < 323:
    print(x)
    if data[y][x] == "#":
        treeCount += 1
    x += 3
    if x > 30:
        x = x - 31
    y += 1

print(f"You're going to hit {treeCount} trees.")
