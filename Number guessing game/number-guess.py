import random

max = input("Type a number: ")

if max.isdigit():
    max = int(max)
    if max <=0:
        print("Please enter a number larger than 0 next time.")
        quit()
else:
    print("Please a number next time.")
    quit()
 
random_num = random.randrange(max)

counter = 0

while True:
    counter += 1
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
        if guess > random_num:
            print("Try lower..")
            continue
        elif guess < random_num:
            print("Try higher..")
            continue
        else:
            print("You got it.")
            print("You took " +str(counter)+ " tries to guess the correct answer!")
            break
    else:
        print("Please type a number next time.")
        continue
    