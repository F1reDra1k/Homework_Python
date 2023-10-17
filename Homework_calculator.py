def modified_calculator():
    first_while = True
    second_while = True
    third_while = True
    fourth_while = True
    input_error = "It should be a number"
    value_float_1 = 0
    value_operator = 0
    value_float_2 = 0
    result = 0
    desire_to_continue = 0
    forgiveness = "Good bue"

    while first_while:
        try:
            value_float_1 = float(input("Please type a number: "))
        except ValueError:
            print(input_error)
            continue
        first_while = False

    while second_while:
        try:
            value_operator = input("Please choose an operator: \n 1 '+'\n 2 '-'\n 3 '*'"
                                   "\n 4 '/' \n 5 '**'\nYour answer: ")
            if value_operator not in ["1", "2", "3", "4", "5"]:
                raise ValueError

        except ValueError:
            print("Invalid symbol")
            continue
        second_while = False

    while third_while:
        try:
            value_float_2 = float(input("Please type another number: "))
        except ValueError:
            print(input_error)
            continue
        third_while = False

    if value_operator == "1":
        result = value_float_1 + value_float_2
    elif value_operator == "2":
        result = value_float_1 - value_float_2
    elif value_operator == "3":
        result = value_float_1 * value_float_2
    elif value_operator == "4":
        try:
            result = value_float_1 / value_float_2
        except ZeroDivisionError:
            result = "You can't divide to 0"
    elif value_operator == "5":
        result = value_float_1 ** value_float_2

    print(result)

    while fourth_while:
        try:
            desire_to_continue = input("desire to continue\nplease make a choice: \n '1' Yes \n '2' No\nYour answer:")
            if desire_to_continue not in ["1", "2"]:
                raise ValueError

        except ValueError:
            print(input_error)
            continue
        fourth_while = False

    if desire_to_continue == "1":
        forgiveness = modified_calculator()
    elif desire_to_continue == "2":
        forgiveness = forgiveness

    print(forgiveness)


modified_calculator()