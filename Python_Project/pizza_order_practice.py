print("Welcome to python pizza deliveries")
size = input("enter the size of the pizza you want? S, M, L \n")
pepperoni = input("do you want pepperoni in your pizza Y, N? \n")
extra_cheese = input("do you want extra cheese in your pizza Y, N? \n")
bill = 0
if size == "S":
    bill = 80
    print("your Bill for small size pizza is Rs80")
elif size == "M":
    bill = 120
    print("your Bill for medium size pizza is Rs120")
elif size == "L":
    bill = 160
    print("your Bill for large size pizza is Rs160")
else:
    print("you give the wrong input")
# pepperoni price
if pepperoni == "Y":
    if size == "S":
        bill += 10
    if size == "M":
        bill += 20
    if size == "L":
        bill += 30
# Extra Cheese Price
if extra_cheese == "Y":
    if size == "S":
        bill += 15
    if size == "M":
        bill += 20
    if size == "L":
        bill += 30
print(f"Your final bill is Rs{bill}")