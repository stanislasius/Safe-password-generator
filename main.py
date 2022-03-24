___version___ = 0.2

# import target modules
from time import sleep
import file_writing, generator

#Main    
print('Вы запустили программу генерации паролей.')

if input('Сгенерировать пароль(-и)? ').lower() == 'да':
   file_writing.write_to_file(generator.start_password_generator())
   print(f'Пароли успешно сгенерированы и помещены в файл passwords.txt по пути {file_writing.home_directory}')
   exit(sleep(10))
else:
   print('Либо было введено "Нет", либо иные данные. Программа завершает свою работу.')
   exit(f'{sleep(5)}')