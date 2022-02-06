import random
sent = True
numberCorrect=0
while sent:
    randNumber1 = random.randrange(1,1000)
    randNumber2 = random.randrange(1,1000)
    randNumber3 = random.randrange(1,3)
    if randNumber3 == 1:
        correctAnswer = int(randNumber1 + randNumber2)
        yourAnswer = int(input(f"What is the integer value of {randNumber1} + {randNumber2}? "))
        if correctAnswer==yourAnswer:
            print("Great job, you answered correctly!")
            numberCorrect +=1
        else:
            print("Oops, the correct answer is ",correctAnswer)
    else:
        correctAnswer = int(randNumber1 - randNumber2)
        yourAnswer = int(input(f"What is the integer value of {randNumber1} - {randNumber2}? "))
        if correctAnswer==yourAnswer:
            print("Great job, you answered correctly!")
            numberCorrect +=1
        else:
            print("Oops, the correct answer is ",correctAnswer)
    userInput = input("Continue playing? Type y to continue: ")
    if userInput != "y":
        sent = False

print("You answered",numberCorrect,"questions correctly!")
print("Thank you for playing!")