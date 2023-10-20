# 1) У вас є рядок my_string = '0123456789'.
# Згенерувати цілі числа (тип int) від 0 до 99 та роздрукувати їх.
# Завдання потрібно виконати через цикл у циклі (див. приклад нижче) та наведення типів.
# Генерування через range або інші "фішки" можна в якості альтернативного вирішення, але спершу через цикл у циклі))

# my_string_1 = "0123456789"
# my_string_2 = "0123456789"

# for symb_int_1 in my_string_1:
#     for symb_int_2 in my_string_2:
#         print(symb_int_1 + symb_int_2)

my_string = '0123456789'

for i in range(100):
    number_str = ''
    if i > 9:
        number_str += my_string[i // 10]
    number_str += my_string[i % 10]
    number = int(number_str)
    #print(number)

###################### Приклад ###############################

# my_string_1 = "12"
# my_string_2 = "34"
#
# for symb_1 in my_string_1:      # перебирається всі елементи з my_string_2 для елемента "1" з my_string_1
#     for symb_2 in my_string_2:  # перебирається всі елементи з my_string_2 для елемента "2" з my_string_1
#         print(symb_1 + symb_2)  # складає символи з першої та другої строки
