import Model
import View
import Logger


def main_menu():
    while True:
        print('\nГлавное меню:')
        print('1. Показать все контакты')
        print('2. Открыть файл с контактами')
        print('3. Записать файл с контактами')
        print('4. Добавить контакт')
        print('5. Изменить контакт')
        print('6. Удалить контакт')
        print('7. Поиск по контактам')
        print('0. Выйти из программы')
        choice = int(input('Выберите пункт: '))
        match choice:
            case 1:
                show_phone_book()
                Logger.show_all()
                print('\nВсе контакты показаны\n')
            case 2:
                open_file()
                print('\nФайл открыт\n')
            case 3:
                save_file()
                print('\nФайл записан\n')
            case 4:
                to_add = add_contact()
                Logger.add(to_add)
                print('\nКонтакт добавлен\n')
            case 5:
                change_key = change_contact()
                Logger.change(change_key)
                print('\nКонтакт изменен\n')
            case 6:
                del_key = remove_contact()
                Logger.del_item(del_key)
                print('\nКонтакт удален\n')
            case 7:
                search_object = search_contact()
                Logger.search(search_object)
                print('\nКонтакт найден\n')
            case 0:
                print('\nВыход\n')
                break


def start():
    open_file()
    View.printPhoneBook()
    main_menu()


def open_file():
    with open(Model.path, "r", encoding="UTF-8") as data:
        contacts_list = data.read().split("\n")
        Model.phonebook = contacts_list


def save_file():
    with open(Model.path, "w", encoding="UTF-8") as data:
        data.write(('\n'.join(Model.phonebook)))


def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    last_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    contact = f'{name}; {surname}; {last_name}; {phone};\n'
    Model.phonebook.append(contact)
    View.printPhoneBook()


def remove_contact():
    choice = int(input('Введите номер элемента для удаления: '))
    Model.phonebook.pop(choice)
    View.printPhoneBook()


def change_contact():
    choice = int(input('Введите номер элемента для изменения: '))
    choice2 = int(input('Что изменяем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))

    contact = Model.phonebook.pop(choice).split(';')
    print(contact)
    contact[choice2] = input('Введите новое значение: ')
    print(contact)
    Model.phonebook.insert(choice, ';'.join(contact))
    View.printPhoneBook()


def show_phone_book():
    with open(Model.path, "r", encoding="UTF-8") as data:
        contacts_list = data.readlines()
        Model.phonebook = contacts_list
        View.printPhoneBook()


def search_contact():
    search = input('Что ищем?: ')
    found = False
    new_list = []
    for item in Model.phonebook:
        if search.lower() in item.lower():
            new_list.append(item)
            found = True
    if not found: print('Ничего не найдено!')

    print(new_list[0].upper())
