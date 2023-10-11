
try:
    value_int_1 = int(input("Please type a number: "))
    value_operator = input("Please choose an operator: \n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/' \n 5 '**'\nYour answer: ")
    value_int_2 = int(input("Please type another number: "))
except ValueError:
         print("It should be a number")
except ZeroDivisionError:
         print("You can't divide to 0")


if value_operator == "1":
    result = value_int_1 + value_int_2
elif value_operator == "2":
    result = value_int_1 - value_int_2
elif value_operator == "3":
    result = value_int_1 * value_int_2
elif value_operator == "4":
    try:
        result = value_int_1 / value_int_2
    except ValueError:
        print("It should be a number")
    except ZeroDivisionError:
        print("You can't divide to 0")

elif value_operator == "5":
    result = value_int_1 ** value_int_2
else:print(result)

 print(result)