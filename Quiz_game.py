print("WELCOME TO MY QUIZ GAME")
print("-----------------------")

playing = input("Do you want to start the game? ")
if playing.lower() != "yes":
    quit()
print("Okay! lets play :)")
score = 0 

answer = input("What does HTML stand for? ")
if answer.lower() == "hyperText markup language":
    print("Correct!")
    score += 1 
else:
    print("Incorrect")

answer = input("What does CSS stand for? ")
if answer.lower() == "cascading style sheet":
    print("Correct!")
    score += 1 
else:
    print("Incorrect")

answer = input("What does JS stand for? ")
if answer.lower() == "javascript":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

if score > 0:
    print("Good game, you got " + str(score) + " questions corrects!")
else:
    print("Good luck next time,you got " + str(score) + " questions corrects!")