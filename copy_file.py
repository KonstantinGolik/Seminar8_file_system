from return_data_file import data_file
from print_data import print_file

def copy_row():
    data, nf = data_file()
    count_rows = len(data)
    if count_rows == 0:
        print("Файл пуст!")
        return
    number_row = int(input(f"Введите номер строки "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
    
    copied_file = f'db/data_{nf}.txt'
    print_file()
    
    edite_nf = int(input("Выберите номер файла, в который хотите скопировать строку: "))
    while edite_nf < 1 or edite_nf > 2:
        edite_nf = int(input("Ошибка!!! Введите цифру 1 или 2: "))

    with open(f'db/data_{edite_nf}.txt', 'r', encoding='utf-8') as edite_file:
        now_number_row = len(edite_file.readlines()) + 1

    with open(copied_file, 'r', encoding='utf-8') as copied_file:
        rows = copied_file.readlines()
        if number_row < 1 or number_row > len(rows):
            print("Введенный номер строки некорректен.")
            return
        row_to_copy = rows[number_row - 1]
        new_row = f'{now_number_row};{row_to_copy.strip().split(";", 1)[1]}\n'
    
    with open(f'db/data_{edite_nf}.txt', 'a', encoding='utf-8') as edite_file:
        edite_file.write(new_row)
    print(f"Данные успешно скопированы.")
    
    