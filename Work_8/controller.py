import model
import view


def run():
    view.greetings()
    while True:
        view.menu()
        answer = input()
        if answer == "1":
            data = model.read_phonebook()
            view.show_phonebook(data)

        elif answer == "2":
            model.add_contact()

        elif answer == "3":
            data = model.read_phonebook()
            count, find_info = model.find(data)
            view.show_find_result(count, find_info)

        elif answer == "4":
            data = model.read_phonebook()
            model.delete(data)

        elif answer == "5":
            data = model.read_phonebook()
            model.change(data)

        elif answer == "6":
            break
