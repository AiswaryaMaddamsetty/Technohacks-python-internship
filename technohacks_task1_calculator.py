def calculate():
    """
    This function performs basic arithmetic operations.
    """
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
Type your operator here:
''')

    try:
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
    except ValueError:
        print('One or both of your inputs are not valid numbers.')
        calculate()

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

def again():
    """
    This function allows the user to decide if they want to perform another calculation.
    """
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()

    elif calc_again.upper() == 'N':
        print('See you later.')

    else:
        again()

def main():
    """
    This function is the main entry point of the program.
    """
    calculate()
    again()

if __name__ == '__main__':
    main()