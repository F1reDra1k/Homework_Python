import random
from string import ascii_letters


# Для завданнь 1-7 за основу можете взяти код із попередніх ДЗ.
#
# 1. Написати функцію яка приймає один параметр – список рядків my_list. Функція повертає новий список у якому міститься
# елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщо на парному – залишити без зміни.

# def Creation_new_list(obj_list: list) -> list:
#     new_list = []
#     for i in range(len(obj_list)):
#         if i % 2 != 0:
#             new_list.append(obj_list[i][::-1])
#         else:
#             new_list.append(obj_list[i])
#
#     return new_list
#
#
# my_list = ["qwe", "dabc", "def", "ghi", "jkl"]
# result_list = Creation_new_list(my_list)
# print(result_list)

# 2. Написати функцію яка приймає один параметр – список рядків my_list.
# Функція повертає новий список у якому міститься елементи my_list у яких перший символ - буква "a".

# def list_first_character(obj_list: list) -> list:
#     new_list = []
#     for i in obj_list:
#         if i.startswith('a'):
#             new_list.append(i)
#
#     return new_list
#
#
# my_list = ["aqwe", "aty", "uio", "asd", "ggh"]
#
# char_list = list_first_character(my_list)
# print(char_list)
#
# 3. Написати функцію яка приймає один параметр – список рядків my_list.
# Функція повертає новий список у якому міститься елементи з my_list, у яких є символ - буква "a" на будь-якому місці.

# def list_any_character(obj_list: list) -> list:
#     new_list = []
#
#     for i in obj_list:
#         if i.count('a'):
#             new_list.append(i)
#     return new_list
#
#
# my_list = ["qwea", "aty", "aio", "asd", "ggh"]
#
# char_list = list_any_character(my_list)
# print(char_list)

# 4. Написати функцію яка приймає один параметр - список рядків my_list у якому може бути як рядки (type str) і цілі числа (type int).
# Функція повертає новий список у якому містяться лише рядки з my_list.

# def only_string(obj_list: list) -> list:
#     new_list = []
#
#     for s in obj_list:
#         if type(s) == str:
#             new_list.append(s)
#     return new_list
#
#
# my_list = [1, "w", 3, "11", "22", 33, "hello"]
# finish_list = only_string(my_list)
# print(finish_list)
# #
# 5. Написати функцію яка приймає один параметр – рядок my_str.
# Функція повертає новий список у якому містяться ті символи з my_str, які зустрічаються у рядку лише один раз.

# def exclusive_symb(obj_string: str) -> list:
#     my_list = []
#
#     for s in set(obj_string):
#         if obj_string.count(s) == 1:
#             my_list.append(s)
#     return my_list
#
#
# my_str = "hello world"
# fin_list = exclusive_symb(my_str)
# print(fin_list)

# 6. Написати функцію яка приймає один параметр - два рядки.
# Функція повертає список у який помістити ті символи, які є в обох рядках хоча б один раз.

# def character_from_two_lines(first_str: str, second_str: str) -> list:
#     my_list = []
#
#     for s in first_str:
#         for i in second_str:
#             if i == s:
#                 my_list.append(s)
#     return my_list
#
#
# my_str = "hello"
# my_str_2 = "world"
#
# fin_list = character_from_two_lines(my_str, my_str_2)
# print(fin_list)
#
# 7. Написати функцію яка приймає два параметри - два рядки.
# Функція повертає список до якого входять ті символи, які є в обох рядках, але в кожному лише по одному разу.

# def crosshair_symb_with_two_lines(first_str: str, second_str: str) -> list:
#     my_list = []
#
#     for s in my_str:
#         if first_str.count(s) == second_str.count(s):
#             my_list.append(s)
#     return my_list
#
#
# my_str = "aaaasdgf12"
# my_str_2 = "asdfff2g"
# fin_list = crosshair_symb_with_two_lines(my_str, my_str_2)
# print(fin_list)
#
# 8. Дано списки names та domains (створити самостійно). Написати функцію для генерування e-mail у форматі:
#     "ім'я . число від 100 до 999 @ стрінга з літер довжиною від 5 до 7 символів . домен"
# Прізвище та домен брати випадковим чином із заданих списків переданих у функцію у вигляді параметрів.
# Рядок і число генерувати випадковим чином.

# def create_email(names: list, domains: list) -> str:
#     name = random.choice(names)
#     number = random.randint(100, 999)
#     string_length = random.randint(5, 7)
#     random_string = ''.join(random.choice(ascii_letters) for _ in range(string_length))
#     domain = random.choice(domains)
#     email = f"{name}.{number}@{random_string}.{domain}"
#     return email
#
#
# names_email = ["john", "alice", "bob", "emma", "king", "miller", "kean"]
# domains_email = ["com", "net", "org", "ua"]
# email = create_email(names_email, domains_email)
# print(email)
