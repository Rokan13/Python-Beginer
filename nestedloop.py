
rows=int(input("enter the number of rows: "))
columns=int(input("enter the number of columns: "))
symbol=input("enter the symble to use:")

for x in range(rows):
    for y in range(columns):
        print(symbol,end="")
    print()