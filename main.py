___version___ = 0.2

# import target modules
from time import sleep
import file_writing, generator

#Main    
print('Вы запустили программу генерации паролей.')

if input('Сгенерировать пароль(-и)? ').lower() == 'да':
   file_writing.write_to_file(generator.start_password_generator())
else:
   print('Либо было введено "Нет", либо иные данные. Программа завершает свою работу .')
   exit(f'{sleep(15)}')