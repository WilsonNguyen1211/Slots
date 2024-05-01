import random

MAX_LINES = 5
MAX_BET = 1000
MIN_BET = 1

ROWS = 5
COLS = 3

symbol_count = {
    "S": 2,
    "A": 5,
    "B": 7,
    "D": 9,
    "F": 10
}

symbol_values = {
    "S": 10,
    "A": 5,
    "B": 3,
    "D": 2,
    "F": 1
}

def check_win(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for colum in columns:
            symbol_check = colum[line]
            if symbol_check != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for col in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slots(columns): # transpose rows to columns
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()



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
    return deposit_amount


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

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Sorry, you don't have enough to bet that amount, your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Your total bet is equal to: ${total_bet}")
    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slots(slots)
    winnings, winning_lines = check_win(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current is ${balance}")
        play = input("Press enter to spin (q to quit).")
        if play == "q":
            break
        balance += spin(balance)




if __name__ == "__main__":
    main()


