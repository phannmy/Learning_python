character = input("Give a character: ")
row = int(input("row: "))
column = int(input("column: "))
for x in range(row):
    for y in range(column):
        print(character,end=" ")
    print()