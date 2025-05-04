logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
game_over = False
bits = {}
while not game_over:
    name_input = input("What is your name?  ")
    bit_input = int(input('What is your bit $  '))

    bits[name_input] = bit_input
    new_users = input("Anyone else want to do bit? type 'yes' or 'no'  ").lower()
    biggest = 0
    winner = ''

    if new_users == "yes":
        print('\n' * 100)
    elif new_users == 'no':
        for key in bits:
            if bits[key] > biggest:
                biggest = bits[key]
                winner = key
                game_over = True
        print(f'Win {winner} with bit {biggest}')
