# easy

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

num_list = [1, 2, 4, 0]
num_list2 =[i*i for i in num_list]
print(num_list2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

list_fruits =["яблоко", "банан", "киви", "арбуз", "апельсин", "мандарин", "груша"]
list_fruits2 = ["банан", "киви","авакадо", "арбуз","слива"]
new_list_fruits = [i for i in list_fruits if i in list_fruits2]
print(new_list_fruits)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

list_of_num = [1, 23, -4, 3253, 544, 87448, 2243, 123, 55, -26]
list_of_num2 = [i for i in list_of_num if i > 0 and i%3 == 0 and i%4 != 0]
print(list_of_num2)


# normal

# Эти задачи необходимо решить используя регулярные выражения!

import re

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

data = input('Введите Имя Фамилию e-mail через пробел')
name, surname, email = data.split(' ')
name_pat, surname_pat, email_pat ='(^[A-ZА-Я][a-zа-я]+)', '(^[A-ZА-Я][a-zа-я]+)', '(^[a-z0-9_]+@[a-z0-9]+\.(ru|org|com))'
if re.match(name_pat, name) != None and re.match(surname_pat, surname) != None  and re.match(email_pat, email) != None:
    print('Данные введены корректно!')
if re.match(name_pat, name) == None:
    print('Неверно указано имя!')
if re.match(surname_pat, surname) == None:
    print('Неверно указана фамилия!')
if re.match(email_pat, email) == None:
    print('Неверно указан email')


# Задача - 2:
# Вам дан текст:

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!

patt_dot = '(\.{2})'

if re.findall(patt_dot, some_str) != None:
    print('В тексте есть более одной точки подряд!')
else:
    print('В тексте нет более одной токи подряд!')


