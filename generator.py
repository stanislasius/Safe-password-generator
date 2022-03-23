# import file-modules
import check_functions

#import python modules
from math import ceil
from random import choice, shuffle
from string import ascii_lowercase, ascii_uppercase, digits



def start_password_generator():
    """ Основной модуль программы, где создаются пароли """

    # init variables and their values
    password, password_list =  str(), list()
    punctuation = "!#$%&()*/_"
    symbols_for_password = ascii_lowercase + ascii_uppercase + digits + punctuation

    # 
    password_numbers = check_functions.correct_password_number(input('Введите необходимое количество сгенерированных паролей: '))
    print()
        
    password_length = check_functions.correct_password_lenght(input('Введите длину(кол-во символов) одного пароля(не менее 8): '))
    print()        

    for i in range(1, password_numbers + 1):
        password = [str(choice(symbols_for_password)) for _ in range(1, password_length + 1)]
        shuffle(password)
        password.append('\n')        
        password_list.append(''.join(password))
        del password
        
    return password_list
