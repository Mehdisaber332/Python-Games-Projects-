import random as rm 
print("Welcome to Guess Number game!")
print("=============================")
top_range = input("Please enter a number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Please enter a number larger than 0")
        quit()
else:
    print("Please enter a valid number") 

random_number = rm.randint(0, top_range)

while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print("Please enter a valid guess number!")
        continue
    if user_guess == top_range:
        print("Good job, you got it!")
        break
    else:
        print("You got it wrong")
