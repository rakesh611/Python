print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to the Treasure Island game your Mission to find Treasure")
choice1 = input('you\'re at crossroad, '
                'where do you want to go ? '
                'type "left" or "right".\n').lower()
if choice1 == "left":
    choice2 = input('you\'ve come to the lake. '
                    'there is an island middle of the lake. '
                    'type "wait" to wait for a boat. '
                    'type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input('you\'ve arrive the island unharmed.'
                        'there is house with 3 doors. '
                        'one "red" ,one "yellow" and one "blue".\n ').lower()
        if choice3 == "red":
            print("It's a room of full of fire Game Over 🔥 🔥 🔥")
        elif choice3 == "yellow":
            print("you found the treasure You Won")
        elif choice3 == "blue":
            print("It's a room of again full of fire Game Over 🔥 🔥 🔥")
        else:
            print("your selection is not correct Game Over")
    else:
        print("you got attack by angry trout. Game Over")
else:
    print("you fell into a hole. Game Over")