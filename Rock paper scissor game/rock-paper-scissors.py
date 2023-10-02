import random

uscore = 0
cscore = 0
options = ["rock", "paper", "scissor"]

while True:
    u_input = input("Type Rock/Paper/Scissor or Q to quit:").lower()
    if u_input == "q":
        break
    
    if u_input not in options:
        continue
    
    random_number = random.randrange(0,2)
    computer_pick = options[random_number]
    print("Computer picked:",computer_pick )
    
    if u_input == "rock" and computer_pick == "scissor":
        print("You won!")
        uscore += 1
    
    elif u_input == "paper" and computer_pick == "rock":
        print("You won!")
        uscore += 1
    
    elif u_input == "scissor" and computer_pick == "paper":
        print("You won!")
        uscore += 1
        
    elif u_input == computer_pick :
        print("Draw!")
    
    else:
        print("You lost!")
        cscore += 1
        
print("Final score=> Computer:",cscore,"You",uscore)
print("Bye!")