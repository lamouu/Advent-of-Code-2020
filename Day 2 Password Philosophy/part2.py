data = []

with open('input.txt') as f:
    data = [line.rstrip() for line in f]

valid = 0
for line in data:
    if (line.split(': ',1)[1][int(line.split(" ", 1)[0].split("-", 1)[0]) - 1] == line[line.find(':') - 1] and line.split(': ',1)[1][int(line.split(" ", 1)[0].split("-", 1)[1]) - 1] != line[line.find(':') - 1]) or (line.split(': ',1)[1][int(line.split(" ", 1)[0].split("-", 1)[0]) - 1] != line[line.find(':') - 1] and line.split(': ',1)[1][int(line.split(" ", 1)[0].split("-", 1)[1]) - 1] == line[line.find(':') - 1]):
        valid += 1

print(f"{valid} valid passwords")
