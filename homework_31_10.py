Для завданнь 1-7 за основу можете взяти код із попередніх ДЗ.

1. Написати функцію яка приймає один параметр – список рядків my_list. Функція повертає новий список у якому міститься
елементи з my_list за таким правилом:
Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
Якщо на парному – залишити без зміни.

2. Написати функцію яка приймає один параметр – список рядків my_list.
Функція повертає новий список у якому міститься елементи my_list у яких перший символ - буква "a".

3. Написати функцію яка приймає один параметр – список рядків my_list.
Функція повертає новий список у якому міститься елементи з my_list, у яких є символ - буква "a" на будь-якому місці.

4. Написати функцію яка приймає один параметр - список рядків my_list у якому може бути як рядки (type str) і цілі числа (type int).
Функція повертає новий список у якому містяться лише рядки з my_list.

5. Написати функцію яка приймає один параметр – рядок my_str.
Функція повертає новий список у якому містяться ті символи з my_str, які зустрічаються у рядку лише один раз.

6. Написати функцію яка приймає один параметр - два рядки.
Функція повертає список у який помістити ті символи, які є в обох рядках хоча б один раз.

7. Написати функцію яка приймає два параметри - два рядки.
Функція повертає список до якого входять ті символи, які є в обох рядках, але в кожному лише по одному разу.

8. Дано списки names та domains (створити самостійно). Написати функцію для генерування e-mail у форматі:
    "ім'я . число від 100 до 999 @ стрінга з літер довжиною від 5 до 7 символів . домен"
Прізвище та домен брати випадковим чином із заданих списків переданих у функцію у вигляді параметрів.
Рядок і число генерувати випадковим чином.

Приклад використання функції:

names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)
print(e_mail)

Відповідь: miller.249@sgdyyur.com