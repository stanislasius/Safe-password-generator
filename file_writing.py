from pathlib import Path
home_directory = Path.home()

def write_to_file(data):
    with open(f'{home_directory}/passwords.txt', 'w') as file:
         file.writelines(data)