import time
import random

a = 0
player_chances = int(input('How many chances do you want to play(in numbers)?: '))
print('''Heres how to play:
      1. A countdown will start before each round.
      2. You are expected to play(in real life) your guess just when the countdown ends(reaches 1).
      3. The computer's choice will be displayed at the same time.
      4. After both you and the computer play their move, you will be asked if you drawed/won/lost the round. We expect you to answer honestly.
      5. There will be as many rounds as you previously inputted.
      6. At the end of the last round, the winner will be announced.
      
      Enjoy!''')

player_wins = 0
bot_wins = 0

while a < player_chances:
    num_prefix = ''
    if (a + 1) in range(1, 10000, 10):
        num_prefix = 'st'
    elif (a + 1) in range(2, 10000, 10):
        num_prefix = 'nd'
    elif (a + 1) in range(3, 10000, 10):
        if (a + 1) in range(13, 10000, 100):
            num_prefix = 'th'
        else:
            num_prefix = 'rd'
    elif (a + 1) in range(4, 10000, 10):
        num_prefix = 'th'
    elif (a + 1) in range(5, 10000, 10):
        num_prefix = 'th'
    elif (a + 1) in range(6, 10000, 10):
        num_prefix = 'th'
    elif (a + 1) in range(7, 10000, 10):
        num_prefix = 'th'
    elif (a + 1) in range(8, 10000, 10):
        num_prefix = 'th'
    elif (a + 1) in range(9, 10000, 10):
        num_prefix = 'th'
    else:
        num_prefix = 'th'

    bot_choices = ['Rock', 'Paper', 'Scissors', 'Rock', 'Scissors', 'Paper', 'Scissors', 'Rock', 'Paper']
    bot_choice = random.choice(bot_choices)

    print(f'This is the {a + 1}{num_prefix} round: The round will start in,')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    print(f'{bot_choice}!')
    time.sleep(0.2)
    print(f'The bot has chosen {bot_choice}')
    
    
    player_round_result = input('Did you win this round? Type y for yes, n for no and d for draw: ')
    if player_round_result.lower() == 'y':
        player_wins += 1
    elif player_round_result.lower() == 'n':
        bot_wins += 1
    else:
        player_wins += 0.5
        bot_wins += 0.5
    
    a += 1
    time.sleep(0.5)

print(f'''Here are the results for the game:
      The bot has won {bot_wins} times
      And you have won {player_wins} times!''')