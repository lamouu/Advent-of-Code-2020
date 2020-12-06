file = open("input.txt")
data = file.read().replace("\n", " ").split('  ')
file.close()

count = 0
for group in data:
    group = group.split(" ")
    for char in group[0]:
        charInGroup = 0
        for j in range(len(group)):
            if j == 0:
                pass
            if char in group[j]:
                charInGroup += 1
        if charInGroup == len(group):
            count += 1
        
print(f"The sum of counts is {count}.")