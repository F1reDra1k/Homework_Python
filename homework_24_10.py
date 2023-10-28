# 1. Дано ціле число (int). Визначити скільки нулів у цьому числі.

# num = 10020000
# num = str(num)
# print(num.count("0"))

# 2. Дано ціле число (int). Визначити скільки нулів наприкінці цього числа. Наприклад для числа 1002000 - три нулі

# num = 10020000
# count_zeros = 0
#
# for digit in reversed(str(num)):
#     if digit == '0':
#         count_zeros += 1
#     else:
#         break
#
# print(count_zeros)

# 3. Дано списки my_list_1 та my_list_2.
# Створити список my_result, який спочатку помістити
# елементи на парних місцях my_list_1, а потім всі елементи на парних місцях my_list_2.

# my_list_1 = [1, 2, 3, 4, 5, 6, 7]
# my_list_2 = [7, 8, 9, 0]
#
# my_result = my_list_1[::2] + my_list_2[::2]
# print(my_result)

# 4. Наведено список my_list. СТВОРИТИ НОВИЙ список new_list у якого перший елемент з my_list
# стоїть на останньому місці. Якщо my_list [1,2,3,4], то new_list[2,3,4,1]

# my_list = [1, 2, 3, 4]
# new_list = my_list[1:] + [my_list[0]]
#
# print(new_list)

# 5. Даний список my_list. У цьому списку перший елемент переставити на останнє місце.
# [1,2,3,4] -> [2,3,4,1]. Перестворювати список не можна! (використовуйте метод pop)

# my_list = [1, 2, 3, 4]
# print(my_list)
# my_list.append(my_list.pop(0))
# print(my_list)

# 6. Дано рядок у якому є числа (розділяються пробілами).
# Наприклад "43 більше ніж 34, але менше ніж 56". Знайти суму ВСІХ ЧИСЕЛ (А НЕ ЦИФР) у цьому рядку.
# Для цього прикладу відповідь - 133. (використовуйте split та перевірку isdigit)

# string = "43 більше ніж 34, але менше ніж 56"
# numbers = []
#
# for s in string.replace(',', " ").split():
#     if s.isdigit():
#         numbers.append(int(s))
# sum_of_numbers = sum(numbers)
# print(sum_of_numbers)

# 7. Наведено список чисел. Визначте, скільки в цьому списку елементів,
# які більше суми двох своїх сусідів (ліворуч і праворуч), і НАДРУКАЙТЕ КІЛЬКІСТЬ таких елементів.
# Останні елементи списку ніколи не враховуються, оскільки у них недостатньо сусідів.
# Для списку [2,4,1,5,3,9,0,7] відповіддю буде 3, тому що 4> 2+1, 5> 1+3, 9>3+0.

# my_list = [2, 4, 1, 5, 3, 9, 0, 7, 1]
# result = 0
#
# for i in range(len(my_list) - 1):
#     if my_list[i] > my_list[i - 1] + my_list[i + 1]:
#         result += 1
#
# print(result)

# 8. Даний список my_list, в якому можуть бути як рядки (type str), так і цілі числа (type int).
# Наприклад [1, 2, 3, "11", "22", 33]
# Створити новий список у який помістити лише рядки з my_list.

# my_list = [1, 2, 3, "11", "22", 33, "hello"]
# new_list = []
#
# for s in my_list:
#     if type(s) == str:
#         new_list.append(s)
# print(new_list)

# 9. Дано рядок my_str. Створити список в який помістити символи з my_str,
# які зустрічаються в рядку ТІЛЬКИ ОДИН разів.

# my_str = "hello"
# my_list = []
#
# for s in my_str:
#     if my_str.count(s) == 1:
#         my_list.append(s)
# print(my_list)

# 10. Дано два рядки. Створити список, у якому помістити ті символи,
# які є в обох рядках хоча б один раз.

# my_str = "hello"
# my_str_2 = "world"
# my_list = []
#
# for s in my_str_2:
#     for i in my_str:
#      if i == s:
#         my_list.append(s)
# print(my_list)

# 11. Дано два рядки. Створити список, у якому помістити ті символи, які є в обох рядках,
# але в кожній ТІЛЬКИ З одного разу.
# Приклад: для рядків "aaaasdf1" та "asdfff2" відповідь ["s", "d"], т.к. ці символи є в кожному рядку по одному разу

# my_str = "aaaasdgf1"
# my_str_2 = "asdfff2g"
# my_list = []
#
# for s in my_str:
#     if my_str.count(s) == my_str_2.count(s):
#         my_list.append(s)
# print(my_list)
