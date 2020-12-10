# INCOMPLETE

with open('input.txt') as f:
    data = [line.rstrip() for line in f]
    data.append("terminated")

acc = 0
i = 0
prevI = []
while True:
    if i in prevI:
        break
    else:
        prevI.append(i)

    instruction = data[i]

    if "terminated" in instruction:
        found = False
        break

    if instruction.split(" ")[0] == "acc":
        acc += int(instruction.split(" ")[1])
        i += 1
    elif instruction.split(" ")[0] == "jmp":
        i += int(instruction.split(" ")[1])
    elif instruction.split(" ")[0] == "nop":
        i += 1

acc = 0
found = False
tempData = data
for instruction in tempData:

    if instruction.split(" ")[0] == "jmp":
        pass

        
        


print(f"{data}")