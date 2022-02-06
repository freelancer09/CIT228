import random
counter=0
numberCorrect=0
while counter < 10:
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
    if ((counter+1) - numberCorrect) > 5:
        print("You should consult with a tutor.")
        break
    counter +=1

print("You answered",numberCorrect,"questions correctly!")
print("Thank you for playing!")