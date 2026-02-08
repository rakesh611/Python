print("welcome to Rollarcoaster")
height = int(input("enter the height in centimeters: \n"))
bill =0
if height >= 120:
    print("you are welcome to Rollarcoaster")
    age = int(input("enter the age in years: \n"))
    if 0 <= age <= 15:
        bill = 0
        print("your bill is Rs0")
    elif 16 <= age <= 35:
        bill = 250
        print("your bill is Rs250")
    want_photo = input("Do you want a photo? y/n\n")
    if want_photo == "y":
        #Add RS20 in bill
        bill+= 20
        print(f"your bill is Rs{bill}")
else:
    print("you are not welcome to Rollarcoaster")