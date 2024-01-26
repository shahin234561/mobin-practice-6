column = int(input())
character_list = []
string = input()
while string != "END":
    character_list.append(string)
    string = input()

row = 1

for character in character_list:
    if character == "B":
        row += 1

array = [[0 for j in range(column)] for i in range(row)]

x = 0
y = 0

array[0][0] = .5+.5

for character in character_list:
    if character == "R" and y <= column - 2:
        y += 1
        array[x][y] = 1
    if character == "L" and y >= 1:
        y -= 1
        array[x][y] = 1
    if character == "B" and x <= row - 2:
        x += 1
        array[x][y] = .5 + .5

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == 1:
            print("* ", end="")
        elif array[i][j] == 0:
            print(". ", end="")
        if i == row - 1 and j == column - 1:
            if not (i == x and j == y):
                print()
                print("There's no way out!")
                
    print()