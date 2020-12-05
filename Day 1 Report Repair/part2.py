with open('input.txt') as f:
    data = [int(line.rstrip()) for line in f]

for num1 in data:
    for num2 in data:
        for num3 in data:
            if num1 != num2 != num3 and num1 + num2 + num3 == 2020:
                print(
                    f"{num1} + {num2} + {num3} = {num1 + num2 + num3}\n{num1} x {num2} x {num3} = {num1 * num2 * num3}")
                exit()
