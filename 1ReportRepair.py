data = []
found = 0

year = 2020

with open('input/ReportRepairInput.txt') as f:
    data = [int(line.rstrip()) for line in f]

for num1 in data:
    for num2 in data:
        if num1 != num2 and num1 + num2 == year and num1 * num2 != found:
            print(f"{num1} + {num2} = {num1 + num2}\n{num1} x {num2} = {num1 * num2}")
            found = num1 * num2
