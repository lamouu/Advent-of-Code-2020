file = open("input.txt")
data = file.read().replace("\n", " ").split('  ')
file.close()

requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
validPassports = 0
for passport in data:
    validField = 0
    for field in passport.split(' '):
        if field.split(':')[0] in requiredFields:
            validField += 1
    if validField == 7:
        validPassports += 1

print(f"{validPassports} passports are valid.")
