with open('input.txt') as f:
    data = [int(line.rstrip()) for line in f]

data.sort()
data.insert(0, 0)
data.append(data[-1] + 3)

onej, threej = 0, 0
for i in range(1, len(data)):
    diff = data[i] - data[i - 1]
    if diff == 1:
        onej += 1
    elif diff == 3:
        threej += 1
    
print(f"The number of 1-jolt differences multiplied by the number of 3-jolt differences is {onej * threej}.")
