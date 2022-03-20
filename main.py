# import target modules
from math import ceil
from random import sample



# init variables and their values
password, password_list =  str(), list()
digits = [str(number) for number in range(0, 10)]
lowercase_letters = [chr(unicode_index) for unicode_index in range(97, 123)]
uppercase_letters = [chr(unicode_index) for unicode_index in range(65, 90)]
# punctuation = "!#$%&*+-=?@^_." --  not sure that it is necessary to use it now


# Init all functions you need
def correct_password_number(password_numbers):                       #check entered values, must be only digits 
    if password_numbers.isdigit() is False:
        password_numbers = input('Вводить нужно ТОЛЬКО ЦЕЛЫЕ ЧИСЛА, так что введите целое число: ')
        correct_password_number(password_numbers)
    else:
        return int(password_numbers)


def correct_password_lenght(password_length):                        #check entered values, must be only digits and length less than 8
    if password_length.isdigit() is False or int(password_length) < 8:
        password_length = input(f'Указаны неверные данные.\nДолжно быть введено только целое число и оно не должно быть меньше 8.\n Введите число: ')
        correct_password_lenght(password_length)
    elif password_length.isdigit() is True and int(password_length) >= 8:
        return int(password_length)


# start main program
print('Вы запустили программу генерации паролей.')

password_numbers = correct_password_number(input('Введите необходимое количество сгенерированных паролей: '))
print()
    
password_length = correct_password_lenght(input('Введите длину(кол-во символов) одного пароля(не менее 8): '))
print()            

for i in range(1, password_numbers + 1):
    password = sample(digits, ceil(password_length / 3)) + sample(lowercase_letters, ceil(password_length / 3)) + sample(uppercase_letters, ceil(password_length / 3))
    password_list.append(''.join(password))
    
print(*password_list, sep='\n')
    