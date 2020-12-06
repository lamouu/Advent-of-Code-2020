with open('input.txt') as f:
    data = [line.rstrip() for line in f]

seatMatrix = [[0 for x in range(8)] for y in range(128)]
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

    seatMatrix[row[0] - 1][column[0] - 1] = 1

for column in range(8):
    for row in range(128):
        if seatMatrix[row][column] == 0 and seatMatrix[row - 1][column] == 1  and seatMatrix[row + 1][column] == 1:
            id_ = row * 8 + column

print(f"Your seat ID is {id_}.")