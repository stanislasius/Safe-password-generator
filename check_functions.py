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
    
