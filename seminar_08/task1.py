# Задача №49. Решение в группах
# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
#     записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

# добавление записи
def add_data():
    with open('seminar_08/file.txt', 'a', encoding='utf-8') as file:
        file.writelines(input('Введите Фамилию, Имя и телефон: '))
        file.write('\n')
        print('\nЗапись добавлена\n')
    x = int(input('Для вывода полного списка введите 1:\nДля добавления еще одной записи введите 2:\n' +
                    'Для выхода в основное меню введите 3: \nДля выхода из программы введите 0: '))
    if x != 1 and x != 2 and x != 0:
        print('Запрос неверный, Вы перенаправленыи в главное меню')
        main_menu()
    elif x == 1:
        output_data()
    elif x == 2:
        add_data()
    elif x == 0:
        print('Программа завершена')

# вывод данных
def output_data():
    print('\nВсе записи телефонной книги: ')
    with open('seminar_08/file.txt', 'r', encoding='utf-8') as file:
        print(file.read())
    main_menu()

# поиск определенной записи
def search_data(text):
    with open('seminar_08/file.txt', 'r', encoding='utf-8') as file:
        k = 0
        l = 0
        for line in file:
            k += 1
            if str(text).lower() in str(line).lower():
                print('Найдена запись: ')
                print(line)
                search_text = str(line)
                return(search_text)
            else:
                l += 1
        if k == l:
            print('Совпадения не найдены')
            main_menu() #
    x = int(input('Для поиска другой записи введите 1:\n' +
                    'Для выхода в основное меню введите 2: \nДля выхода из программы введите 0: '))
    if x != 1 and x != 0:
        main_menu()
    elif x == 1:
        search_data()
    elif x == 0:
        print('Программа завершена')

# удаление и изменение записи
def delete_data(text):
    search_text = search_data(text)
    x = int(input('Для удаления введите 1: \nДля замены записи на новую введите 2: \n' + 
                  'Для отмены и выхода в основное меню введите 0: '))
    if x == 1:
        with open('seminar_08/file.txt', 'r', encoding='utf-8') as file:
            read_from_file_lst = file.readlines()
        if search_text in read_from_file_lst:
            n = read_from_file_lst.index(search_text)
            read_from_file_lst.pop(n)
            with open('seminar_08/file.txt', 'w', encoding='utf-8') as file:
                new_text_for_write = ''
                for i in read_from_file_lst:
                    new_text_for_write += i
                file.write(new_text_for_write)
                print('Запись удалена\n')
        else:
            print('Совпадения не найдены\n')
        main_menu()
    elif x == 2:
        with open('seminar_08/file.txt', 'r', encoding='utf-8') as file:
            read_from_file_lst = file.readlines()
        if search_text in read_from_file_lst:
            n = read_from_file_lst.index(search_text)
            read_from_file_lst.pop(n)
            newtext = input('\nВведите новую запись: ')
            read_from_file_lst.insert(n, newtext)
            with open('seminar_08/file.txt', 'w', encoding='utf-8') as file:
                new_text_for_write = ''
                for i in read_from_file_lst:
                    new_text_for_write += i + '\n'
                file.write(new_text_for_write)
                #file.write('\n')
                print('Запись заменена\n')
        else:
            print('Совпадения не найдены\n')
        main_menu()
    elif x == 0:
        print('Удаление отменено\n')
        main_menu()

# главное меню
def main_menu():
    n = user_input()
    if n != 1 and n != 2 and n != 3 and n != 0:
        print('\nЗапрос неверный. Повторите попытку!\n') 
        main_menu()
    elif n == 1:
        output_data()
    elif n == 2:
        add_data()
    elif n == 3:
        text = input('\nВведите данные для поиска: ')
        delete_data(text)
    elif n == 0:
        print('\nПрограмма зевершена\n')

# ввод пользователя
def user_input():
    n = int(input('\nДля вывода содержимого введите 1: \nДля добавления записи введите 2: \n' + 
                  'Для поиска, удаления и редактирования 3: \nДля выхода из программы введите 0: '))
    return n


main_menu()