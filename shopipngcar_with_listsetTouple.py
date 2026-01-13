foods = []
prices = []
total = 0

while True:
    food = input("enter a food to buy : ")
    if food.lower() == "q":
        break
    price = float(input(f"enter a price for the food {food}: $"))
    foods.append(food)
    prices.append(price)

print("----- Your cart ----")
for food in foods:
    print(food,end=" ")
for price in prices:
    total +=price
