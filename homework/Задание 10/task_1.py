# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string

alphabet = string.ascii_lowercase


def generate_random_name():
    while True:
        first_word = ''
        second_word = ''
        for i in range(random.randrange(1, 15, 1)):
            first_word += random.choice(alphabet)
        for i in range(random.randrange(1, 15, 1)):
            second_word += random.choice(alphabet)
        yield second_word + ' ' + first_word


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# Здесь пишем код
