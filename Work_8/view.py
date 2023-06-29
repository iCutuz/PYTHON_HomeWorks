def greetings():
    print("Приветствуем Вас в электронной телефонной книге! Выберите необходимый для Вас пункт меню. ")


def menu():
    print("Меню:\nВывод контактов - 1 \n"
          "Добавление контакта - 2 \n"
          "Поиск контакта - 3 \n"
          "Удаление контакта - 4 \n"
          "Изменение контакт - 5 \n"
          "Выход - 6 ")


def show_phonebook(data):
    try:
        print(' '.join(data))
    except FileNotFoundError:
        print("Данные отсутствуют.")


def show_find_result(count, find_info):
    if count == 0:
        print("Контакт не найден")
    else:
        print(' '.join(find_info))