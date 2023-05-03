first_string = 'wtf'
second_string = 'brick quz jmpy veldt wings fox'
c = second_string.find(first_string[0])
b = second_string.find(first_string[1])
f = second_string.find(first_string[-1])  # По условию задачи первая строка 3 символа
# поэтому создал 3 параметра которые показывают индекс при первом вхождении, конечно можно
# было через index(), но find вроде почти тоже-самое
print(second_string[min(c, b, f):max(c, b, f)+1])
# Далее нахожу минимальное и максимальное число в созданных параметрах и ставлю в искомое слово
# 'brick quz jmpy veldt wings fox'
