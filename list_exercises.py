def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    numbers = []
    get_number(numbers)
    print("The first number is ", numbers[0])
    print("The last number is ", numbers[-1])
    print("The smallest number is ", min(numbers))
    print("The largest number is ", max(numbers))
    print("The average number is ", sum(numbers) / 5)
    def_user_name(usernames)


def get_number(numbers):
    for i in range(5):
        number = float(input("Number:"))
        numbers.append(number)
    return numbers


def def_user_name(usernames):
    username = str(input("Your name:"))
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
