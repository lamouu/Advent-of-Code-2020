with open('input.txt') as f:
    data = [line.rstrip() for line in f]

acc = 0
i = 0
prevI = []
while True:
    if i in prevI:
        break
    else:
        prevI.append(i)

    instruction = data[i]
    if instruction.split(" ")[0] == "acc":
        acc += int(instruction.split(" ")[1])
        i += 1
    elif instruction.split(" ")[0] == "jmp":
        i += int(instruction.split(" ")[1])
    elif instruction.split(" ")[0] == "nop":
        i += 1

print(f"The accumulator value is {acc}.")