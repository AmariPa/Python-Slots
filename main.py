# imports
import random
import climage
from PIL import Image

# consts
MAX_LINES = 3
MAX_BET = 500
MIN_BET = 1
ROWS = 3
COLS = 3

# images for slots
A = climage.convert('apple.png')
B = climage.convert('banana.png')
C = climage.convert('cherry.png')
D = climage.convert('orange.png')

# assigns images a value
symbol_count = {
    A: 5,
    B: 3,
    C: 4,
    D: 5,
}


def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

# prints the slot machine in the CLI


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], '|')
            else:
                print(column[row])


# Asks user how much money they want to deposit. Requires a number


def deposit():
    while True:
        amount = input(
            'How much money would you like to deposit? Please enter a whole number. $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Deposit must be greater than zero.')
        else:
            print('Please enter a number.')
    return amount

# Asks user how many lines they wish to bet on with a limit


def get_number_of_lines():
    while True:
        lines = input(
            'Enter the number of lines you wish to bet on (1-' + str(MAX_LINES) + ')? ')
        if lines.isdigit():
            lines = int(lines)
        if 1 <= lines <= MAX_LINES:
            break
        else:
            print('Enter a valid number of lines.')
    else:
        print('Please enter a number.')

    return lines

# Asks user how much of their deposit they'd like to bet


def get_bet():
    while True:
        amount = input('How much would you like to bet on each line? $')
        if amount.isdigit():
            amount = int(amount)
        if MIN_BET <= amount <= MAX_BET:
            break
        else:
            print(f'Bet must be between ${MIN_BET} - ${MAX_BET}')
    else:
        print('Please enter a number.')

    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"This bet exceeds your balance, your current balance is: ${balance}")
        else:
            break
    print(
        f'You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}.')

# generates slot machine
    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)


main()
