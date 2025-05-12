import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking between 1 to 100.")
choose_a_level = input("Choose a difficulty!Type 'Hard' or 'Easy': ").lower()
hidden_number = random.randint(1, 100)


def easy_level(num):
    attemps = 10

    while attemps != 0:
        guess = int(input(f"You have {attemps} attemps remaining to guess the number.\n "
                          f"Make a guess: "))
        attemps -= 1
        if guess > hidden_number:
            print(f'Too high.\n '
                  f'Guess again.')
        elif guess < hidden_number:
            print((f'Too low.\n '
                  f'Guess again.'))
        else:
            print(f'You got it. It is number {hidden_number}')
            break
    else:
        print(f'Sorry,but you lose')


def hard_level(num):
    attemps = 5

    while attemps != 0:
        guess = int(input(f"You have {attemps} attemps remaining to guess the number.\n "
                          f"Make a guess: "))
        attemps -= 1
        if guess > hidden_number:
            print(f'Too high.\n '
                  f'Guess again.')
        elif guess < hidden_number:
            print((f'Too low.\n '
                  f'Guess again.'))
        else:
            print(f'You got it. It is number {hidden_number}')
            break
    else:
        print(f'Sorry,but you lose')


def game():
    if choose_a_level == 'hard':
        hard_level(hidden_number)
    elif choose_a_level == 'easy':
        easy_level(hidden_number)
    else:
        print("Wrong input")

game()