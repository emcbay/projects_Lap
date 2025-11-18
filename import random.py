import random

def game():
    zahl = random.randint(1,100)
    max_hp = 5
    ff15 = 0

    while True:
        if max_hp == ff15:
            print("You lost the number was", zahl)
            break
        try:
            chosen_number = int(input("Bitte eine Zahl zwischen 1-100 eingeben: "))
        except ValueError:
            print("Please input Numbers")
            continue

        if chosen_number == zahl:
            print("You Won")
            break
        elif chosen_number >= zahl:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        ff15 += 1
    try_again = input("Try again? y=yes n=no: ")
    if try_again.lower() == "y":
        game()
    else:
        print("Thank you for playing!") 
game()