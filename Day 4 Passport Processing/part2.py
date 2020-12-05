import re

file = open("input.txt")
data = file.read().replace("\n", " ").split('  ')
file.close()

validPassports = 0
for passport in data:
    validField = 0
    for field in passport.split(' '):
        if field.split(':')[0] == "byr" and field.split(':')[1].isnumeric() and len(field.split(':')[1]) == 4:
            if 2002 >= int(field.split(':')[1]) >= 1920:
                validField += 1
        if field.split(':')[0] == "iyr" and field.split(':')[1].isnumeric() and len(field.split(':')[1]) == 4:
            if 2020 >= int(field.split(':')[1]) >= 2010:
                validField += 1
        if field.split(':')[0] == "eyr" and field.split(':')[1].isnumeric() and len(field.split(':')[1]) == 4:
            if 2030 >= int(field.split(':')[1]) >= 2020:
                validField += 1
        if field.split(':')[0] == "hgt" and field.split(':')[1][:-2].isnumeric():
            if field.split(':')[1][-2:] == "cm":
                if 193 >= int(field.split(':')[1][:-2]) >= 150:
                    validField += 1
            if field.split(':')[1][-2:] == "in":
                if 76 >= int(field.split(':')[1][:-2]) >= 59:
                    validField += 1
        if field.split(':')[0] == "hcl" and len(field.split(':')[1]) == 7 and field.split(':')[1][0] == "#" and re.match("[a-f]|\d", field.split(':')[1][1:]):
            validField += 1
        if field.split(':')[0] == "ecl" and field.split(':')[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            validField += 1
        if field.split(':')[0] == "pid" and field.split(':')[1].isdigit() and len(field.split(':')[1]) == 9:
            validField += 1
    if validField == 7:
        validPassports += 1

print(f"{validPassports} passports are valid")