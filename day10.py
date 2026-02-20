print(''' _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')
def operation (symbol, num1, num2):
    if symbol == "+":
        return num1 + num2
    if symbol == "-":
        return num1 - num2
    if symbol == "*":
        return num1 * num2
    if symbol == "/":
        return num1 / num2

def calculator():
    should_accumulate = True

    first_number = int(input("What's the first number?: "))
    while should_accumulate:
        pick_operation = input('''
        +
        -
        *
        /
        Pick an operation: ''')
        next_number = int(input("What's the next number?: "))
        output = operation(symbol = pick_operation, num1 = first_number, num2 = next_number)
        print(float(output))

        continue_calc = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new caluclation: ")

        if continue_calc == 'yes':
            first_number = output
        else:
            should_accumulate = False
            print("/n" * 20)
            calculator()



calculator()


