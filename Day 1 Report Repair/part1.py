data = []
year = 2020

with open('input.txt') as f:
    data = [int(line.rstrip()) for line in f]

for num1 in data:
    for num2 in data:
        if num1 != num2 and num1 + num2 == year:
            print(f"{num1} + {num2} = {num1 + num2}\n{num1} x {num2} = {num1 * num2}")
            exit()
