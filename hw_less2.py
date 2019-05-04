# easy

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2. банан
# 3. киви
# 4. арбуз

# Подсказка: воспользоваться методом .format ()

fruit_list = ["яблоко", "банан", "киви", "арбуз"]
number = 1
for _ in fruit_list:
    print(f'{number}. {_}')
    number += 1

# Задача-2:
# Даны два возможных списка.
# Удалите из первого списка элементы, присутствующие во втором списке

list1, list2 = [12, 3, 56, 'wre', 5, 7, 'rew', 1], [2, 7, 14, 'wre', 3, 28, 14]
for _ in list2:
    if _ in list1:
        list1.remove(_)
print(list1)

# Задача-3:
# Дан список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# Если элемент кратны два, то разделить его на 4, если не кратно, то умножить на два.

list_of_numbers = [2, 18, 19, 8, 11, 46, 123, 987, 987676, 7654, 123312, 1233]
new_list_of_numbers = []
for i in list_of_numbers:
    if i % 2 == 0:
        new_list_of_numbers.append(i/4)
    else:
        new_list_of_numbers.append(i*2)
print(list_of_numbers)
print(new_list_of_numbers)

# normal


# Задача-1:
# Дан список, заполненный доступными целыми числами, получите новый список,
# Элементами которого будут квадратные корни элементов исходного списка,
# Но только если результаты извлечения корня не имеет десятичную часть и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4] Результат: [3, 5, 2]

list_of_integers = [2, -5, 8, 9, -25, 25, 4]
root_function_list =[]
for n in list_of_integers:
    if n > 0 and int(n**0.5) == n**0.5:
        root_function_list.append(int(n**0.5))
print(root_function_list)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

first_data = '02.11.2013'
day, month, year = first_data.split('.')
month_dict = { '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня', '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря' }
day_dict = { '01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвёртое', '05': 'пятое', '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое', '11': 'одиннадцатое',
               '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое',
               '20': 'двадцатое', '21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвёртое', '25': 'двадцать пятое', '26': 'двадцать шестое',
               '27': 'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое' }
print(day_dict[day], month_dict[month], year,'года')


# Задача-3: Напишите алгоритм, заполняющий список
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint () модуля random

n = int(input('Введите количество элементов списка'))
list_n =[]
import random
for _ in range(n):
    list_n.append(random.randint(-100, 100))
print(list_n)


# Задача-4: Дан список, заполненный доступными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 2, 4, 5, 6, 2, 5, 2]

# a):
lst2 = list(set(lst))
print(lst2)

# б):
lst3 = []
for i in lst:
    if lst.count(i) == 1:
        lst3.append(i)
print(lst3)

# hard

# Задание-1: уравнение прямого вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# уравнение =  ' y = -12x + 11111140.2121 '
# х =  2,5
# вычислите и выведите y

x = 2.5
equation = ' y = -12x + 11111140.2121 '
equation = equation.replace(' ','')
equation = equation.replace('y','')
equation = equation.replace('=','')
first_n, second_n = equation.split('x')
print('Y =',float(first_n)* x + float(second_n))

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен быть в диапазоне от 1 до 30 (31)
#   (в зависимости от месяца, февраль не учитываем)
# № 2. Количество участников в диапазоне от 1 до 12
# № 3. Год должен быть представлен в диапазоне от 1 до 9999
# # 4. Длина исходной строки для частей должна быть в соответствии с форматом
# №   (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)
# Пример корректной даты
# дата =  ' 01.11.1985 '
# Примеры недостных дат
# дата =  ' 01.22.1001 '
# дата =  ' 1.12.1001 '

new_data = input('Введите дату в формате дд.мм.гггг')
day, month, year = new_data.split('.')
if len(day) != 2 or len(month) != 2 or len(year) != 4:
    print('Дата введена некорректно!')
elif int(day) < 1 or int(day) > 31 or int(month) < 1 or int(month) > 12 or int(year) < 1 or int(year) > 9999:
    print('Дата введена некорректно!')
else:
    print('Дата введена корректно!')