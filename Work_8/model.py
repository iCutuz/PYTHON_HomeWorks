def read_phonebook():
    with open("filename.txt", 'r', encoding='utf-8') as f:
        data = []
        for i in f:
            data.append(i)
        return data


def add_contact():
    first_name = input("Введите имя ").capitalize()
    last_name = input("Введите фамилию ").capitalize()
    phone_number = input("Введите номер телефона ")
    contact = first_name + " " + last_name + " " + phone_number + "\n"
    with open("filename.txt", 'a', encoding='utf-8') as f:
        f.write(contact)


def find(data):
    info = input("Введите известные данные").capitalize()
    count = 0
    find_info = []
    for i in data:
        if info in i:
            count += 1
            find_info.append(i)
        else:
            continue
    return count, find_info


def delete(data):
    info = input("Введите удаляемый контакт ").capitalize()
    for i in data:
        if info not in i:
            with open("filename.txt", 'w', encoding='utf-8') as f:
                f.write(i)


def change(data):
    info = input("Введите изменяемый контакт ").capitalize()
    with open("filename.txt", 'w', encoding='utf-8') as f:
        for i in range(len(data)):
            if info in data[i]:
                data[i] = data[i].replace(info, add_contact()) #не знаю, как обработать проблему с None
                f.write(data[i])
            else:
                f.write(data[i])