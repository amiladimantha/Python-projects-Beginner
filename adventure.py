name = input("Enter your name: ")
print("Welcome to the adventure!",name)

answer = input("You are at a junction. You can go left or right. Which way will you go? ").lower()

if answer == "left":
    answer = input("You find a wobbly bridge, do you cross it?(yes/no)").lower()
    if answer == "yes":
        print("The bridge broke and you fell into the abyss. You lose.")
    elif answer == "no":
        answer = input("You continue ahead and find a cave. Do you venture in?(yes/no)").lower()
        if answer == "yes":
            print("You find a hidden chest in the cave. In it there is a golden nugget. You found a small fortune. You win!")
        elif answer == "no":
            print("You turn back and did not find any gold. You lose.")
        else:
            print("Not a valid option, you lose.")
    else:
        print("Not a valid option, you lose.")
        
elif answer == "right":
    answer = input("You find an old haunted mansion, do you go in?(yes/no)").lower()
    if answer == "no":
        print("You turn back and did not find any gold. You lose.")
    elif answer == "yes":
        answer = input("You go in and find a stranger. Do you talk to him?(yes/no)").lower()
        if answer == "yes":
            answer = input("He asks for your help. Do you help him? (yes/no)").lower()
            if answer == "yes":
                answer = input("He tells you to find an old locket from a room in the mansion and bury it in the backyard where a tomb stone is located. Do you do it or not?(yes/no)").lower()
                if answer == "yes":
                    print("After you do it. He takes you near an old tree at the back of the mansion and tells you to dig near it. After diggin a few feet you find a big chest. In it you find a huge amount of gold. As you joyfully exclaim and turn around to thank the stranger you find that both the mansion and the stranger has vanished and a piece of paper with the words 'thank you' remains where the stranger stood. You win!")
                elif answer == "no":
                    print("You turn back leave the mansion and the garden. As you walk out of your vision goes dark. When you wake up next the mansion is gone and you are still where you fainted. You lose since you did not find the tresure.")
                else:
                    print("Not a valid option, you lose.")        
            elif answer == "no":
                print("You turn back leave the mansion. As you walk out of the mansion your vision goes dark. When you wake up next the mansion is gone and you are still where you fainted. You lose since you did not find the tresure.")
            else:
                print("Not a valid option, you lose.")
        elif answer == "no":
            print("You turn back leave the mansion. As you walk out of the mansion your vision goes dark. When you wake up next the mansion is gone and you are still where you fainted. You lose since you did not find the tresure.")
        else:
            print("Not a valid option, you lose.")
    else:
        print("Not a valid option, you lose.")
else:
    print("Not a valid option, you lose.")
    
print("Thank you for playing. Good bye!", name)