# 1. Дано рядок.
#      a. виведіть третій символ цього рядка.

my_str_1 = "виведіть третій символ цього рядка"

#print(my_str_1[2])

#      b. виведіть передостанній символ цього рядка.

my_str_2 = "виведіть передостанній символ цього рядка"

#print(my_str_2[-2])

#      c. виведіть перші п'ять символів цього рядка.

my_str_3 = "виведіть перші п'ять символів цього рядка"

#print(my_str_3[:5])

#      d. виведіть весь рядок, крім двох останніх символів.

my_str_4 = "виведіть весь рядок, крім двох останніх символів"

#print(my_str_4[:-2])

#      e. виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0, тому символи виводяться
#      починаючи з першого).

my_str_5 = ("виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0, "
            "тому символи виводяться починаючи з першого)")

#print(my_str_5[::2])

#      f. виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.

my_str_6 = "виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка"

#print(my_str_6[1::2])
#      g. виведіть усі символи у зворотному порядку.

my_str_7 = "виведіть усі символи у зворотному порядку"

#print(my_str_7[::-1])

#      h. виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.

my_str_8 = "виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього"

back_my_str_8 = my_str_8[::-1]

#print(back_my_str_8[::2])

#      i. виведіть довжину цього рядка.

my_str_9 = "виведіть довжину цього рядка"

#print(len(my_str_9))

# 2. Дано рядок, що складається зі слів, розділених пробілами. Визначте, скільки у ній слів.
# Використовуйте для вирішення завдання функцію `count`

my_str_space = ("Дано рядок, що складається зі слів, розділених пробілами. Визначте, скільки у ній слів. "
                "Використовуйте для вирішення завдання функцію `count`")

#print(my_str_space.count(" ") +1)

# 3. Користувач вводить окремо рядок `s` та один символ `ch`. Необхідно здійснити пошук у рядку `s` всіх символів `ch`.
# Для вирішення можна використовувати тільки функцію `find` (rfind), оператори `if` та `for` (while).

s = "hello"
ch = "l"
b = 0

for index in s:
    if (index == ch):
        b = b + 1

#print(b)

# 4. Дано рядок. Замініть у цьому рядку всі появи літери `h` на літеру `H`, крім першого та останнього входження.

string = "hello world how are you"
first_h = string.index('h')
last_h = string.rindex('h')

new_string = ''
for i in range(len(string)):
    if i == first_h or i == last_h:
        new_string += string[i]
    elif string[i] == 'h':
        new_string += 'H'
    else:
        new_string += string[i]

#print(new_string)