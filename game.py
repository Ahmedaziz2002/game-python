import sys

def room_A():
    print("\nSorry, bro, you fumbled hard. Here you meet her boyfriend, and he kills you. Easy death, bro! Hahaha.")
    print("Next time, don't be guided by your dick... Hahaha.\n")

def room_B():
    print("\nWelcome to Room B. You find a treasure chest here.")
    print("Do you want to open it? (yes or no)\n")

    choice = input("> ").strip().lower()
    if choice == "yes":
        print("\nCongratulations! You found a hidden exit and escaped the house safely.\n")
    elif choice == "no":
        print("\nYou decide to leave the chest alone and walk away. Unfortunately, you get lost in the house forever.\n")
    else:
        print("\nInvalid choice! You need to decide whether to open the chest or not. Try again.\n")
        room_B()

def room_C():
    print("\nWelcome to Room C. It's a dark room with two doors: one red and one blue.")
    print("Which door will you choose? (red or blue)\n")

    choice = input("> ").strip().lower()
    if choice == "red":
        print("\nThe red door leads to a fiery pit. You didn't survive.\n")
    elif choice == "blue":
        print("\nThe blue door leads to a safe passage out of the house. You escaped!\n")
    else:
        print("\nInvalid choice! You need to choose between the red and blue doors. Try again.\n")
        room_C()

def room_Z():
    print("\nHello, welcome to Room Z.")
    print("Here you meet two kinds of people: a man and a woman.")
    print("They both offer to guide you through the hotel.")
    print("WHO WILL YOU FOLLOW?\n")

    choice = input("Type 'man' or 'woman': ").strip().lower()
    if choice == "man":
        print("\nYou got saved, bro. Lucky guy, he leads you through the exit.\n")
    elif choice == "woman":
        room_A()
    else:
        print("\nLearn what to type and follow instructions, idiot!\n")
        room_Z()

def house():
    print("""
    HELLO THERE! WELCOME TO DEAD HOUSE.
    PLEASE PICK A KEY.
    AND BE FAST BECAUSE WE CAN'T WAIT TO ENTERTAIN YOU.
    HAVE IT EASY... HAHAH, NO, I'M KIDDING. YOU AIN'T GETTING OUT OF HERE ALIVE.
    """)

    choice = input("Enter your pick (key 1, key 2, key 3, or key 4): ").strip().lower()

    if choice == "key 1":
        room_Z()
    elif choice == "key 2":
        print("\nYou got lucky, bro... Have a nice view on your way out!")
        print("Lucky guy.\n")
    elif choice == "key 3":
        room_B()
    elif choice == "key 4":
        room_C()
    else:
        print("\nInvalid choice! Exiting the game. Better luck next time.\n")
        sys.exit()

house()
