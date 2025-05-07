def add(n1, n2):
    return n1 + n2


def subtract(s1, s2):
    return s1 - s2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation = {'+': add,
             '-': subtract,
             '*': multiply,
             "/": divide,
             }

should_accumulate = True
num1 = int(input('What is the first number?: '))

while should_accumulate:
    for symbol in operation:
        print(symbol)
    operation_symbol = input('pick an operation: ')
    num2 = int(input('What is the second number: '))
    answer = operation[operation_symbol](num1, num2)
    print(f'{num1} {operation_symbol} {num2} = {answer}')
    choice = input(f"type 'y' to continue to calculate with {answer} or type 'n' to start a new calculation : ")
    if choice == 'y':
        num1 = answer
    else:
        should_accumulate = False
