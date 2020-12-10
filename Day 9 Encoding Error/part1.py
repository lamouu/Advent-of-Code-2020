with open('input.txt') as f:
    data = [line.rstrip() for line in f]

prevArray = []
for i in range(0, 25):
    prevArray.append(data[i])

for i in range(0, len(data)):
    found = False
    if i < 26:
        continue

    prevArray.append(data[i - 1])
    prevArray.pop(0)

    for num1 in prevArray:
        for num2 in prevArray:
            if int(num1) != int(num2) and int(num1) + int(num2) == int(data[i]):
                found = True
                continue
    
    if found == False:
        firstNo = data[i]
        break

print(f"The first number without the property is {firstNo}.")