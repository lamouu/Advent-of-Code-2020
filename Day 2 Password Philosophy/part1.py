with open('input.txt') as f:
    data = [line.rstrip() for line in f]

valid = 0
for line in data:
    if int(line.split(" ", 1)[0].split("-", 1)[1]) >= int(line.split(': ',1)[1].count(line[line.find(':') - 1])) >= int(line.split(" ", 1)[0].split("-", 1)[0]):
        valid += 1

print(f"{valid} valid passwords.")
