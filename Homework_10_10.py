value_int_1 = int(input("Please type a number: "))
value_operator = input("Please choose an operator: \n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/' \n 5 '**'\nYour answer: ")
value_int_2 = int(input("Please type another number: "))


if value_operator == "1":
    result = value_int_1 + value_int_2
elif value_operator == "2":
    result = value_int_1 - value_int_2
elif value_operator == "3":
    result = value_int_1 * value_int_2
elif value_operator == "4":
    result = value_int_1 / value_int_2
elif value_operator == "5":
    result = value_int_1 ** value_int_2

else:print(result)
print(result)