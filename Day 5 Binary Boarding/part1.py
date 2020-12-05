data = []

with open('input.txt') as f:
    data = [line.rstrip() for line in f]

highestId = 0
for seat in data:
    row = [*range(1, 129)]
    column = [*range(1, 9)]

    for index in range(10):
        if seat[index] == "F":
            row = row[:len(row)//2]
        if seat[index] == "B":
            row = row[len(row)//2:]
        if seat[index] == "R":
            column = column[len(column)//2:]
        if seat[index] == "L":
            column = column[:len(column)//2]

    rowIndex = row[0] - 1
    columnIndex = column[0] - 1
    id_ = rowIndex * 8 + columnIndex

    if id_ > highestId:
        highestId = id_

print(f"The highest seat ID is {highestId}")