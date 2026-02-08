print("Welcome to Rollarcoaster")
height = int(input("what is your height in centimeters?\n"))
if height >= 120:
    print("you are welcome to Rollarcoaster")
    age = int(input("what is you age?\n"))
    if age <=12:
        print("you have to pay 100Rs")
    elif age<=18:
        print("you have to pay 120Rs")
    else:
        print("you have to pay 180Rs")
else:
    print("you are Not welcome to Rollarcoaster")