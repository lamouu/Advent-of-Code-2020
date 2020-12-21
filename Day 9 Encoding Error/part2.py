# INCOMPLETE

with open('input.txt') as f:
    data = [line.rstrip() for line in f]

range_ = []
for i, num1 in enumerate(data):
    sum_ = int(num1)
    for j, num2 in enumerate(data):
        if j < i:
            continue

        #print(f"i:{i} j:{j}")
        #print(sum_)

        sum_ += int(num2)
        if sum_ == 1639024365:
            print("ding")
            #range_ = data[i:j]
            #break
