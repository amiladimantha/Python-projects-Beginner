print("Let's begin the Computer Quiz!")

playing = input("Do you want to play the game? ")

if playing.lower() != "yes":
    quit()

print("Okay, Lets start :)")

count = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("That's correct")
    count += 1
else:
    print("That's incorrect")
    

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("That's correct")
    count += 1
else:
    print("That's incorrect")
    
    
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("That's correct")
    count += 1
else:
    print("That's incorrect")
    
    
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("That's correct")
    count += 1
else:
    print("That's incorrect")
    

print("You got "+ str(count) +" out of 4 questions right!")
print("Your score: "+ str(count/4*100) +"%")
