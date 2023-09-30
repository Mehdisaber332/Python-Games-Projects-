print("Welcome to GAMBLING GAME")
print("-------------------------")
print("-------------------------")
Max_lines = 3
Min_bet = 20
Max_bet = 100 

""" Deposit part """
def deposit():
    while True:
        amount = input("How much would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break 
            else:
                print("Please enter a number greater than 0.")
        else: 
            print(" Please enter a valid number!")
    return amount 

"""Number of lines part """
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(Max_lines) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= Max_lines:
                break 
            else: 
                print("Please enter a valid number")
        else: 
            print("Please enter a number")
    return lines 

"""Bet part"""
def get_bet():
    while True:
        bet = input("Please enter your bet: ")
        if bet.isdigit():
            bet = int(bet)
            if Min_bet <= bet <= Max_bet:
                break 
            else: 
                print(f"Please enter a bet between {Min_bet} and {Max_bet}")
        else:
            print("Please enter a valid number to bet ")
    return bet

def main():
    your_money = deposit()
    lines = get_number_of_lines() 
    while True:
        your_bet = get_bet()
        total_bet = your_bet * lines 
        if total_bet > your_money:
            print(f"You don't have enough amount, your current money is {your_money}$")
        else:
            break
    print(f"You are betting {your_bet}$ on {lines}.")
    print(f"Total bet : {total_bet}")

    main()
