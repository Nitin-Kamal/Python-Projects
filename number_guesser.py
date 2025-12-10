import random
guess = str(random.randint(1, 9))
chance = 0
while chance < 3:
    player_guess = input('your guess?, type quit to exit: ')
    guess_length = len(player_guess)
    if guess_length > 1 and player_guess.upper() != "QUIT":
        print('run the program again and please pick a number between 1 to 9')
        break
    if player_guess != guess and player_guess.upper() != "QUIT":
        print('wrong answer')
        chance += 1
    if player_guess == guess and chance == 0:
        print(f'you won in the first try!, the answer was {guess}')
        break
    if player_guess == guess and chance == 1:
        print(f'you won in the second try!, the answer was {guess}')
        break
    if player_guess == guess and chance == 2:
        print(f'you won in the third try!, the answer was {guess}')
        break
    if player_guess.upper() == "QUIT":
        print("bye!, play again later!")
        break
else:
    print(f"your chances are over, the answer was {guess}")
