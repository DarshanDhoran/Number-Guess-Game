# Number guessing Game:-

import random
target = random.randint(1,10)

while True:
    userChoice = input("Guess the Number or Quit(press Q): ")
    if(userChoice == "Q"):
        break
    if(userChoice == target):
        print("Success : Correct Guess!")
        break
    elif(userChoice < target):
        print("Number is Samll...")
   
    else:
        print("Number is Big...")
       
print("-----Game Over-----")