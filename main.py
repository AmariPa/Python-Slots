MAX_LINES = 3
MAX_BET = 500
MIN_BET = 1

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
                f"This bet exceeds your balance, your current balance is ${balance}")
        else:
            break
    bet = get_bet()
    total_bet = bet * lines
    print(
        f'You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}.')


main()
