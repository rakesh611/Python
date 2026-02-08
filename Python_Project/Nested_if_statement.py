print("Welcome to Rollarcoaster Ride")
height = int(input("What is your height in centimeters?\n"))
if height > 90:
    print("you are welcome to Rollarcoaster")
    age = int(input("what is your age?\n"))
    if age >= 18:
        print("pay the money of 120Rs")
    else:
        print("pay the money of 60Rs")
else:
    print("you are not welcome to Rollarcoaster")