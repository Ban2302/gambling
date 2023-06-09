import random


MAX_LINES = 3
MAX_BET = 200
MIN_BET = 50

ROWS = 3
COLS = 3

symbo_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbo_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
def check_winnings(colums, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = colums[0][line]
        for colum in colums:
            symbo_check = colum[line]
            if symbol != symbo_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines

def get_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)

    colums = []
    for _ in range(cols):
        colum = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            colum.append(value)
        
        colums.append(colum)
         
    return colums

def print_machine(colums):
    for row in range(len(colums[0])):
        for i, colum in enumerate(colums):
            if i != len(colums) - 1:
                print (colum[row], end= " | ")
            else:
                print(colum[row], end="")
            
        print()




def deposit():
    while True:
        amount = input("What would you like to deposit? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter number")
    
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) +")?  ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <=MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter number")
    
    return lines


def get_bet():
    while True:
        amount = input("Enter How Much you want to bet :")
        if amount.isdigit:
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f" Please give amount in a range of {MIN_BET}$ - {MAX_BET}$")
        else:
            print("Please enter numbers")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        les_balance = total_bet - balance
        if total_bet > balance:
            print( f" You can bot bet more thatn your total balance. Your Balance is {balance}$ you bet {total_bet}. Please Top Up your account for {les_balance}")
        else:
            break
    print( f"you are betting {bet} ob {lines} lines. Your total bet is {total_bet}")

    slots = get_machine_spin(ROWS, COLS, symbo_count)
    print_machine(slots)
    winnings = check_winnings(slots, lines, bet, symbo_value)
    print(f"You won ${winnings}.")
   
main()