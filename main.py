___version___ = 0.1

# import target modules
from math import ceil
from random import sample, shuffle
from string import ascii_lowercase, ascii_uppercase, digits


# init variables and their values
password, password_list =  str(), list()
punctuation = "!#$%&()*/_"

# Init all functions you need
def correct_password_number(password_numbers):
    """Функция проверки корректности введённых данных для количества сгенерированных паролей""" 
    if password_numbers.isdigit() is False:
        password_numbers = input('Вводить нужно ТОЛЬКО ЦЕЛЫЕ ЧИСЛА, так что введите целое число: ')
        return correct_password_number(password_numbers)
    else:
        return int(password_numbers)

def correct_password_lenght(password_length):
    """Функция проверки корректности введённых данных для длины пароля"""
    if password_length.isdigit() is False or int(password_length) < 8:
        new_password = input(f'Указаны неверные данные.\nДолжно быть введено только целое число и оно не должно быть меньше 8.\nВведите число: ')
        return correct_password_lenght(new_password)
    elif password_length.isdigit() is True and int(password_length) >= 8:
        return int(password_length)

def start_program():
    """ Основной модуль программы, где создаются пароли """

    password_numbers = correct_password_number(input('Введите необходимое количество сгенерированных паролей: '))
    print()
        
    password_length = correct_password_lenght(input('Введите длину(кол-во символов) одного пароля(не менее 8): '))
    print()        

    for i in range(1, password_numbers + 1):
        password = sample(digits, ceil(password_length / 4)) + sample(ascii_lowercase, ceil(password_length / 4)) + sample(ascii_uppercase, ceil(password_length / 4)) + sample(punctuation, ceil(password_length / 4))
        shuffle(password)
        password_list.append(''.join(password[0:password_length]))
        del password
        
    return print(*password_list, sep='\n')
    
#Main    
print('Вы запустили программу генерации паролей.')

if input('Сгенерировать пароль(-и)? ').lower() == 'да':
    start_program()
else:
    exit('Либо было введено "Нет", либо иные данные. Программа завершает свюо работу.')

