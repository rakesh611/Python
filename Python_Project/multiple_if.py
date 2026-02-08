print("welcome to Rollarcoaster")
height = int(input("enter the height in centimeters: \n"))
bill =0
if height >= 120:
    print("you are welcome to Rollarcoaster")
    age = int(input("enter the age in years: \n"))
    if 8 <= age <= 18:
        bill = 180
        print("your bill is Rs180")
    elif age >=18:
        bill = 250
        print("your bill is Rs250")
    else:
        bill = 100
        print("your bill is Rs100")
    want_photo = input("Do you want a photo? y/n\n")
    if want_photo == "y":
        #Add RS20 in bill
        bill+= 20
        print(f"your bill is Rs{bill}")
else:
    print("you are not welcome to Rollarcoaster")

