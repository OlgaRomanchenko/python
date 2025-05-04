import random

stages =[ """
 +---+
 |   |
 0   |
/|\  |
/ \  |
     |
======     
""",""" 
 +---+
 |   |
 0   |
/|\  |
/    |
     |
====== 
""", """
 +---+
 |   |
 0   |
/|\  |
     |
     |
====== 
""", """
 +---+
 |   |
 0   |
/|   |
     |
     |
====== 
""","""
 +---+
 |   |
 0   |
 |   |
     |
     |
====== 
""", """
 +---+
 |   |
 0   |
     |
     |
     |
====== 
""","""
 +---+
 |   |
     |
     |
     |
     |
====== 
"""]

life = 6
words = ['aardwark', 'baboon', 'camel']
word = random.choice(words)
print(word)
word_len = len(word)
blank = ''

for position  in range(word_len):
    blank += '_'
print(blank)

game_over = False
correct_letters = []


while not game_over:
    letter = input('Try to guess word. Print first letter:\n').lower()
    dysplay = ''

    if letter not in word:
        life -= 1
        if life == 0:
            game_over = True
            print("You lose")

    for i in word:
        if letter == i:
            dysplay += letter
            correct_letters.append(letter)
        elif i in correct_letters:
            dysplay += i
        else:
            dysplay += '_'


    print(dysplay)

    if '_' not in dysplay:
        game_over = True
        print('You win')


    print(stages[life])