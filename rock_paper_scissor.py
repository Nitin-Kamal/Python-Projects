import random
play_choose = input('who do you want to play with. Computer or custom?: ')
play = ['rock', 'paper', 'scissors']
play_bot = ""
player = ""
chance = 0
score_player = 0
score_bot = 0
player_name = ''
if play_choose.upper() == "COMPUTER":
    player_name = 'the computer'
else:
    player_name = input('Type in the name of your opponent: ')
while chance < 10:
    player = input('your choice, rock or paper or scissors?: ')
    play_bot = random.choice(play)
    if player.upper() == "ROCK" and play_bot.upper() == "SCISSORS":
        print(f'you win, {player_name} picked {play_bot}')
        chance += 1
        score_player += 1
    if player.upper() == "ROCK" and play_bot.upper() == "PAPER":
        print(f'you lose, {player_name} picked {play_bot}')
        chance += 1
        score_bot += 1
    if player.upper() == "ROCK" and play_bot.upper() == "ROCK":
        print(f'draw, {player_name} picked {play_bot}')
        chance += 1

    if player.upper() == "PAPER" and play_bot.upper() == "SCISSORS":
        print(f'you lose, {player_name} picked {play_bot}')
        chance += 1
        score_bot += 1
    if player.upper() == "PAPER" and play_bot.upper() == "ROCK":
        print(f'you win, {player_name} picked {play_bot}')
        chance += 1
        score_player += 1
    if player.upper() == "PAPER" and play_bot.upper() == "PAPER":
        print(f'draw, {player_name} picked {play_bot}')
        chance += 1

    if player.upper() == "SCISSORS" and play_bot.upper() == "PAPER":
        print(f'you win, {player_name} picked {play_bot}')
        chance += 1
        score_player += 1
    if player.upper() == "SCISSORS" and play_bot.upper() == "ROCK":
        print(f'you lose, {player_name} picked {play_bot}')
        chance += 1
        score_bot += 1
    if player.upper() == "SCISSORS" and play_bot.upper() == "SCISSORS":
        print(f'draw, {player_name} picked {play_bot}')
        chance += 1


if score_player > score_bot:
    result1 = "you won"
elif score_player < score_bot:
    result1 = "the computer won"
elif score_player == score_bot:
    result1 = "its a draw"
if chance >= 10:
    print(f"game over, you scored {score_player} and {player_name} scored {score_bot}, {result1}")