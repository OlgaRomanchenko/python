



def calculate_love_score(name1, name2):
    count_love = 0
    count_true = 0
    true = 'true'
    love = 'love'
    names = name1 + name2
    for letter in names:
        if letter in true:
            count_true += 1
        if letter in love:
            count_love += 1

    print(str(count_true) + str(count_love))

calculate_love_score('true','love')

