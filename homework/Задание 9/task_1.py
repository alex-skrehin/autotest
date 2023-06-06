# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
from pathlib import Path

path = Path('C:\\Alex_git\\homework\\Задание 9\\test_file\\task1_data.txt')
file = open(path, mode='r', encoding='utf8')
path_answer = Path('C:\\Alex_git\\homework\\Задание 9\\test_file\\task1_answer.txt')
file_answer = open(path_answer, mode='w+', encoding='utf8')
for line in file.readlines():
    for j in line:
        if not j.isdigit():
            file_answer.write(j)
file_answer.close()
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
