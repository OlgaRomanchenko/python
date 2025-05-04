import random

num = random.randint(0, 20)
guess = int(input('Guess number:  '))

while guess != num:
    if guess < num:
        print(' Your number less')
    else:
        print("Your number bigger")
    guess = int(input('try again:  '))
print(f'You win! This is correct number {guess}')