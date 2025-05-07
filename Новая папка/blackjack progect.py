import random


def deal_cards():
    """Return a random card """
    game_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(game_cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(users_score, computers_score):
    if users_score == computers_score:
        return "Draw"
    elif computers_score == 0:
        return "Lose! opponent has a BlackJack"
    elif users_score == 0:
        return "Win with BlackJack"
    elif users_score > 21:
        return "You went over. You Lose!"
    elif computers_score > 21:
        return "opponent went over. You Win"
    elif users_score > computers_score:
        return "You Win!"
    else:
        return "you Lose"


def play_game():
    user = []
    computer = []
    computer_score = -1
    user_score = -1
    game_over = False

    for _ in range(2):
        user.append(deal_cards())
        computer.append(deal_cards())

    while not game_over:
        user_score = calculate_score(user)
        computer_score = calculate_score(computer)
        print(f'Your cards {user} .Score {user_score}')
        print(f'Computer cards {computer[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_dear = input("Would you like add one card? Type 'y' or 'n' ?: ")
            if user_should_dear == 'y':
                user.append(deal_cards())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer.append(deal_cards())
        computer_score = calculate_score(computer)
    print(f"Your card {user} and final score is {user_score}")
    print(f"computer card {computer} and final score is {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play in BlackJack game? Type 'y' or 'n': ") == 'y':
    print("\n" * 15)
    play_game()
