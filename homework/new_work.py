t1 = str(input("Введите текст 1: "))
t2 = str(input("Введите текст 2: "))
print(t1.replace(t1[0:2], t2[0:2]) + ' ' + t2.replace(t2[0:2], t1[0:2]))
