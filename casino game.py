import random
def get_deposit():
    while True:
        dep_amount = input('how much would you like to deposit?: ')
        if dep_amount.isdigit():
            dep_amount = int(dep_amount)
            if dep_amount > 0:
                break
            else:
                print('Please enter a number greater than 0')
        else:
            print('Please enter a number')
    return dep_amount

def get_line_amount():
    while True:
        line_amount = input('how much line would you like to bet on?: ')
        if line_amount.isdigit():
            line_amount = int(line_amount)
            if line_amount > 0:
                if line_amount <= 10:
                    break
                else:
                    print('Please enter a valid amount of lines')
            else:
                print('Please enter a number greater than 0')
        else:
            print('Please enter a number')
    return line_amount

def get_bet_amount():
    while True:
        bet_amount = input('how much would you like to bet?: ')
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if bet_amount > 0:
                if bet_amount <= balance:
                    total_per_bet = bet_amount * line
                    if total_per_bet <= balance:
                        print(F"You have chosen {line} lines for ${bet_amount}")
                        break
                    else:
                        print('Please choose a lower bet money.')
                else:
                    print('Please bet an amount lesser than your total deposit')
            else:
                print('Please enter a number greater than 0')
        else:
            print('Please enter a number')
    return bet_amount
def main():
    draw_count = 1
    print_message = ''
    line_amount = line * bet
    draw = ''
    while True:
        if draw_count == 1:
            print_message = 'First draw'
            print(print_message)
            row1 = ['apple', 'banana', 'orange']
            row2 = ['apple', 'banana', 'orange']
            row3 = ['apple', 'banana', 'orange']
            row1r = random.choice(row1)
            row2r = random.choice(row2)
            row3r = random.choice(row3)
            result_draw = [row1r, row2r, row3r]
            print(result_draw)
            draw_count = 2
            draw = 'first draw!'
            if result_draw == ['apple', 'apple', 'apple'] or result_draw ==  ['banana', 'banana', 'banana'] or result_draw == ['orange', 'orange', 'orange']:
                print(f'You won the {draw} You got {bet}$')
                line_amount = line_amount + bet
                print(f"The balance on bet is {line_amount}$")
            else:
                print(f"You lost the {draw} you lose {bet}$")
                line_amount = line_amount - bet
                print(f"The balance on bet is {line_amount}$")
        elif draw_count == 2:
            print_message = 'Second draw'
            print(print_message)
            row1 = ['apple', 'banana', 'orange']
            row2 = ['apple', 'banana', 'orange']
            row3 = ['apple', 'banana', 'orange']
            row1r = random.choice(row1)
            row2r = random.choice(row2)
            row3r = random.choice(row3)
            result_draw = [row1r, row2r, row3r]
            print(result_draw)
            draw_count = 3
            draw = 'second draw!'
            if result_draw == ['apple', 'apple', 'apple'] or result_draw ==  ['banana', 'banana', 'banana'] or result_draw == ['orange', 'orange', 'orange']:
                print(f'You won the {draw} You got {bet}$')
                line_amount = line_amount + bet
                print(f"The balance on bet is {line_amount}$")
            else:
                print(f"You lost the {draw} you lose {bet}$")
                line_amount = line_amount - bet
                print(f"The balance on bet is {line_amount}$")
        elif draw_count == 3:
            print_message = 'Third draw'
            print(print_message)
            row1 = ['apple', 'banana', 'orange']
            row2 = ['apple', 'banana', 'orange']
            row3 = ['apple', 'banana', 'orange']
            row1r = random.choice(row1)
            row2r = random.choice(row2)
            row3r = random.choice(row3)
            result_draw = [row1r, row2r, row3r]
            print(result_draw)
            draw_count = 4
            draw = 'third draw!'
            if result_draw == ['apple', 'apple', 'apple'] or result_draw ==  ['banana', 'banana', 'banana'] or result_draw == ['orange', 'orange', 'orange']:
                print(f'You won the {draw} You got {bet}$')
                line_amount = line_amount + bet
                print(f"The balance on bet is {line_amount}$")
            else:
                print(f"You lost the {draw} you lose {bet}$")
                line_amount = line_amount - bet
                print(f"The balance on bet is {line_amount}$")
        elif draw_count == 4:
            print_message = 'fourth draw'
            print(print_message)
            row1 = ['apple', 'banana', 'orange']
            row2 = ['apple', 'banana', 'orange']
            row3 = ['apple', 'banana', 'orange']
            row1r = random.choice(row1)
            row2r = random.choice(row2)
            row3r = random.choice(row3)
            result_draw = [row1r, row2r, row3r]
            print(result_draw)
            draw_count = 5
            draw = 'fourth draw!'
            if result_draw == ['apple', 'apple', 'apple'] or result_draw ==  ['banana', 'banana', 'banana'] or result_draw == ['orange', 'orange', 'orange']:
                print(f'You won the {draw} You got {bet}$')
                line_amount = line_amount + bet
                print(f"The balance on bet is {line_amount}$")
            else:
                print(f"You lost the {draw} you lose {bet}$")
                line_amount = line_amount - bet
                print(f"The balance on bet is {line_amount}$")
        elif draw_count == 5:
            print_message = 'fifth draw'
            print(print_message)
            row1 = ['apple', 'banana', 'orange']
            row2 = ['apple', 'banana', 'orange']
            row3 = ['apple', 'banana', 'orange']
            row1r = random.choice(row1)
            row2r = random.choice(row2)
            row3r = random.choice(row3)
            result_draw = [row1r, row2r, row3r]
            print(result_draw)
            draw_count = 6
            draw = 'fifth draw!'
            if result_draw == ['apple', 'apple', 'apple'] or result_draw ==  ['banana', 'banana', 'banana'] or result_draw == ['orange', 'orange', 'orange']:
                print(f'You won the {draw} You got {bet}$')
                line_amount = line_amount + bet
                print(f"The balance on bet is {line_amount}$")
            else:
                print(f"You lost the {draw} you lose {bet}$")
                line_amount = line_amount - bet
                print(f"The balance on bet is {line_amount}$")
        elif draw_count == 6:
            print_message = 'sixth draw'
            print(print_message)
            row1 = ['apple', 'banana', 'orange']
            row2 = ['apple', 'banana', 'orange']
            row3 = ['apple', 'banana', 'orange']
            row1r = random.choice(row1)
            row2r = random.choice(row2)
            row3r = random.choice(row3)
            result_draw = [row1r, row2r, row3r]
            print(result_draw)
            draw_count = 7
            draw = 'sixth draw!'
            if result_draw == ['apple', 'apple', 'apple'] or result_draw ==  ['banana', 'banana', 'banana'] or result_draw == ['orange', 'orange', 'orange']:
                print(f'You won the {draw} You got {bet}$')
                line_amount = line_amount + bet
                print(f"The balance on bet is {line_amount}$")
            else:
                print(f"You lost the {draw} you lose {bet}$")
                line_amount = line_amount - bet
                print(f"The balance on bet is {line_amount}$")
        elif draw_count == 7:
            print_message = 'seventh draw'
            print(print_message)
            row1 = ['apple', 'banana', 'orange']
            row2 = ['apple', 'banana', 'orange']
            row3 = ['apple', 'banana', 'orange']
            row1r = random.choice(row1)
            row2r = random.choice(row2)
            row3r = random.choice(row3)
            result_draw = [row1r, row2r, row3r]
            print(result_draw)
            draw_count = 8
            draw = 'seventh draw!'
            if result_draw == ['apple', 'apple', 'apple'] or result_draw ==  ['banana', 'banana', 'banana'] or result_draw == ['orange', 'orange', 'orange']:
                print(f'You won the {draw} You got {bet}$')
                line_amount = line_amount + bet
                print(f"The balance on bet is {line_amount}$")
            else:
                print(f"You lost the {draw} you lose {bet}$")
                line_amount = line_amount - bet
                print(f"The balance on bet is {line_amount}$")
        elif draw_count == 8:
            print_message = 'eighth draw'
            print(print_message)
            row1 = ['apple', 'banana', 'orange']
            row2 = ['apple', 'banana', 'orange']
            row3 = ['apple', 'banana', 'orange']
            row1r = random.choice(row1)
            row2r = random.choice(row2)
            row3r = random.choice(row3)
            result_draw = [row1r, row2r, row3r]
            print(result_draw)
            draw_count = 9
            draw = 'eighth draw!'
            if result_draw == ['apple', 'apple', 'apple'] or result_draw ==  ['banana', 'banana', 'banana'] or result_draw == ['orange', 'orange', 'orange']:
                print(f'You won the {draw} You got {bet}$')
                line_amount = line_amount + bet
                print(f"The balance on bet is {line_amount}$")
            else:
                print(f"You lost the {draw} you lose {bet}$")
                line_amount = line_amount - bet
                print(f"The balance on bet is {line_amount}$")
        elif draw_count == 9:
            print_message = 'ninth draw'
            print(print_message)
            row1 = ['apple', 'banana', 'orange']
            row2 = ['apple', 'banana', 'orange']
            row3 = ['apple', 'banana', 'orange']
            row1r = random.choice(row1)
            row2r = random.choice(row2)
            row3r = random.choice(row3)
            result_draw = [row1r, row2r, row3r]
            print(result_draw)
            draw_count = 10
            draw = 'ninth draw!'
            if result_draw == ['apple', 'apple', 'apple'] or result_draw ==  ['banana', 'banana', 'banana'] or result_draw == ['orange', 'orange', 'orange']:
                print(f'You won the {draw} You got {bet}$')
                line_amount = line_amount + bet
                print(f"The balance on bet is {line_amount}$")
            else:
                print(f"You lost the {draw} you lose {bet}$")
                line_amount = line_amount - bet
                print(f"The balance on bet is {line_amount}$")
        elif draw_count == 10:
            print_message = 'tenth draw'
            print(print_message)
            row1 = ['apple', 'banana', 'orange']
            row2 = ['apple', 'banana', 'orange']
            row3 = ['apple', 'banana', 'orange']
            row1r = random.choice(row1)
            row2r = random.choice(row2)
            row3r = random.choice(row3)
            result_draw = [row1r, row2r, row3r]
            print(result_draw)
            draw_count = 11
            draw = 'tenth draw!'
            if result_draw == ['apple', 'apple', 'apple'] or result_draw ==  ['banana', 'banana', 'banana'] or result_draw == ['orange', 'orange', 'orange']:
                print(f'You won the {draw} You got {bet}$')
                line_amount = line_amount + bet
                print(f"The balance on bet is {line_amount}$")
            else:
                print(f"You lost the {draw} you lose {bet}$")
                line_amount = line_amount - bet
                print(f"The balance on bet is {line_amount}$")
        if draw_count > line:
            break



balance = get_deposit()
line = get_line_amount()
bet = get_bet_amount()
main()