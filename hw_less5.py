# easy

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
for i in range (1, 10):
    os.mkdir('dir_' + str(i))
for j in range (1, 10):
    os.rmdir('dir_' + str(j))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

all_list = os.listdir()
folder_list = []
for j in all_list:
    if os.path.isdir(j):
        folder_list.append(j)
print(folder_list)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
file_name = os.path.basename(__file__)
file = open(f'copy_{file_name}.py', 'w',  encoding='utf-8')
shutil.copyfile(file_name, f'copy_{file_name}.py')
file.close()




