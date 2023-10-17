first_while = True
input_error = "It should be a number"
value_float_1 = 0
value_operator = 0
value_float_2 = 0


while True:
    try:
        value_float_1 = float(input("Please type a number: "))
    except ValueError:
        print(input_error)
        continue
    break

while True:
    try:
        value_operator = input("Please choose an operator: \n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/' \n 5 '**'\nYour answer: ")
        if value_operator not in ["1", "2", "3", "4", "5"]:
            raise ValueError

    except ValueError:
        print("Invalid symbol")
        continue
    break

while True:
    try:
        value_float_2 = float(input("Please type another number: "))
    except ValueError:
        print(input_error)
        continue
    break

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
        result = ("You can't divide to 0")
elif value_operator == "5":
    result = value_float_1 ** value_float_2

print(result)