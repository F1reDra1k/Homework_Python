# 1. Наведено список рядків my_list. Створити новий список до якого помістити елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщо на парному – залишити без зміни. Завдання зробити за допомогою enumerate або range.

# my_list = ["qwe", "rty", "uio", "asd", "fgh"]
# new_list = []
#
# for i in range(len(my_list)):
#     if i % 2 != 0:
#         new_list.append(my_list[i][::-1])
#     else:
#         new_list.append(my_list[i])
#
# print(new_list)

# 2. Наведено список рядків my_list. Створити новий список до якого помістити елементи my_list
# у яких перший символ - буква "a".

# my_list = ["qwe", "aty", "uio", "asd", "ggh"]
# new_list = []
#
# for i in my_list:
#     if i.startswith('a'):
#         new_list.append(i)
# print(new_list)

# 3. Наведено список рядків my_list. Створити новий список до якого помістити
# елементи з my_list, у яких є символ - буква "a" на будь-якому місці.

# my_list = ["qwea", "aty", "uaio", "asd", "ggh"]
# new_list = []
#
# for i in my_list:
#     if i.count('a'):
#         new_list.append(i)
# print(new_list)

# 4) Даний список словників людей у форматі [{"name": "John", "age": 15}, ..., {"name": "Jack", "age": 45}]
# а) Створити список і помістити туди ім'я наймолодшої людини. Якщо вік збігається – помістити всі імена наймолодших.

# people = [
#     {"name": "John", "age": 15},
#     {"name": "Kris", "age": 20},
#     {"name": "Bob", "age": 25},
#     {"name": "Zed", "age": 5}
# ]
# young_people =[]
# min_age = people[0]["age"]
#
# for person in people:
#     if person["age"] < min_age:
#         min_age = person["age"]

# for person in people:
#     if person["age"] == min_age:
#         young_people.append(person["name"])
#
# print(young_people)

# б) Створити список та помістити туди найдовше ім'я. Якщо довжина імені збігається - помістити такі імена.
#
# people = [
#     {"name": "John", "age": 5},
#     {"name": "Kris", "age": 20},
#     {"name": "Bob", "age": 25},
#     {"name": "Zed", "age": 5}
# ]
# leng_name_people =[]
#
# max_len = len(people[0]["name"])
# for person in people:
#     if len(person["name"]) < max_len:
#         min_age = person["name"]
#
# print(max_len)
# for person in people:
#     if len(person["name"]) == max_len:
#         lens_name_people.append(person["name"])
#
# print(leng_name_people)

# в) Порахувати середню вік усіх людей із початкового списку.
#
# people = [
#     {"name": "John", "age": 5},
#     {"name": "Kris", "age": 10},
#     {"name": "Bob", "age": 25},
#     {"name": "Zed", "age": 5}
# ]
#
# total_age = 0
# count = 0
#
# for person in people:
#     total_age += person["age"]
#     count += 1
#
# average_age = total_age / count
#
# print(round(average_age))

# 5) Дано два словники my_dict_1 і my_dict_2.
# а) Створити список із ключів, які є в обох словниках.

# my_dict_1 = {
#     "name11": "John", "age11": 5,
#     "name2": "Kris", "age2": 20,
#     "name3": "Bob", "age3": 25,
#     "name": "Zed", "age": 5
# }
# my_dict_2 = {
#     "name1": "John", "age1": 5,
#     "name2": "Kris", "age2": 20,
#     "name3": "Bob", "age3": 25,
#     "name": "Zed", "age": 5
# }
# my_list = []
#
# for key in my_dict_1.keys():
#     if key in my_dict_2:
#         my_list.append(key)
#
# print(my_list)
#
# б) Створити список із ключів, які є у першому, але немає у другому словнику.
# my_dict_1 = {
#     "name11": "John", "age11": 5,
#     "name2": "Kris", "age2": 20,
#     "name3": "Bob", "age3": 25,
#     "name": "Zed", "age": 5
# }
# my_dict_2 = {
#     "name1": "John", "age1": 5,
#     "name2": "Kris", "age2": 20,
#     "name3": "Bob", "age3": 25,
#     "name": "Zed", "age": 5
# }
#
# my_list = list(set(my_dict_1.keys()) - set(my_dict_2.keys()))
#
#
# print(my_list)
#
# в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.

# my_dict_1 = {
#     "name11": "John", "age11": 5,
#     "name2": "Kris", "age2": 20,
#     "name3": "Bob", "age3": 25,
#     "name": "Zed", "age": 5
# }
# my_dict_2 = {
#     "name11": "John", "age1": 5,
#     "name2": "Kris", "age2": 20,
#     "name3": "Bob", "age3": 25,
#     "name": "Zed", "age": 5
# }
# new_dict = {}
#
# for key in my_dict_1:
#     if key not in my_dict_2:
#         new_dict[key] = my_dict_1[key]
# print(new_dict)

# г) Об'єднати ці два словники у новий словник за правилом:
# якщо ключ є тільки в одному з двох словників - помістити пару ключ: значення,
# якщо ключ є у двох словниках - помістити пару {ключ: [значення_з_першого_словника, значення_з_другого_словника]},
#
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
#
#
# my_dict_1 = {
#     "name1": "Kris", "age": 20,
#
# }
# my_dict_2 = {
#     "name2": "Kim", "age": 25,
# }
# new_dict = {}
#
# for key, value in my_dict_1.items():
#     if key not in my_dict_2:
#         new_dict[key] = value
#
# for key, value in my_dict_2.items():
#     if key not in my_dict_1:
#         new_dict[key] = value
#
# for key in my_dict_1.keys():
#     if key in my_dict_2:
#         new_dict[key] = [my_dict_1[key], my_dict_2[key]]
#
# print(new_dict)