file = open("input.txt")
data = file.read().replace("\n", " ").split('  ')
file.close()

sum_ = 0
for group in data:
    sum_ += len(set(group.replace(" ", "")))

print(f"The sum of counts is {sum_}.")