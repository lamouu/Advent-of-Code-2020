with open('input.txt') as f:
    data = [line.rstrip() for line in f]

bagArray = ['shiny gold bag']
lastLength = 0

while len(bagArray) != lastLength:
    lastLength = len(bagArray)
    for line in data:
        for bag in bagArray:
            if bag in line.split(' bags contain ')[1] and line.split(' bags contain ')[0] not in bagArray:
                bagArray.append(line.split(' bags contain ')[0])

print(f"{len(bagArray) - 1} different bag colours can eventually contail at least one shiny gold bag.")