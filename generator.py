# import file-modules
import main
import check_functions

#import python modules
from math import ceil
from random import sample, shuffle
from string import ascii_lowercase, ascii_uppercase, digits



def start_program():
    """ Основной модуль программы, где создаются пароли """

    password_numbers = check_functions.correct_password_number(input('Введите необходимое количество сгенерированных паролей: '))
    print()
        
    password_length = check_functions.correct_password_lenght(input('Введите длину(кол-во символов) одного пароля(не менее 8): '))
    print()        

    for i in range(1, password_numbers + 1):
        password = sample(digits, ceil(password_length / 4)) + sample(ascii_lowercase, ceil(password_length / 4)) + sample(ascii_uppercase, ceil(password_length / 4)) + sample(punctuation, ceil(password_length / 4))
        shuffle(password)
        password.append('\n')        
        main.password_list.append(''.join(password))
        del password
        
    return main.password_list


