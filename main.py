MAX_LINES = 7
MAX_BET = 1000
MIN_BET = 1
def start_screen():
    while True:
        print("Welcome to Slots!\n"
              "-----------------\n"
              "1. Deposit\n"
              "2. Withdraw\n"
              "3. Check Balance\n"
              "4. Play\n"
              "5. Exit")

        break


def deposit():
    while True:
        deposit_amount = input("How much money would you like to deposit: $")
        if deposit_amount.isdigit():
            deposit_amount = int(deposit_amount)
            if deposit_amount > 0:
                break
        else:
            print("Please enter a valid amount.")
    print(f"${deposit_amount} has been deposited")


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you would like to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines to bet on.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("How much money would you like to bet on each line: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Bet amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a valid number")
    return amount

def main():
    start = start_screen()
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Your total bet is equal to: ${total_bet}")



if __name__ == "__main__":
    main()


