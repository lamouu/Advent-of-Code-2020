# INCOMPLETE

with open('input.txt') as f:
    data = [line.rstrip()[:-1] for line in f]


bagArray = []
def bagFunc(searchingBag):
    global bagArray

    for line in data:
        if searchingBag in line.split(' bags contain ')[0]:
            bagArray.append(line.split(' bags contain ')[1])
            for searchingBag in line.split(' bags contain ')[2:]:
                print(line.split(' bags contain ')[2:])
                bagFunc(searchingBag)

bagFunc("shiny gold")
print(bagArray)