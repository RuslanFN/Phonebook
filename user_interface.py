def __print_start_messege__():
    print('Добро пожаловать в телефонный справочник')
    print('Ознакомьтесь с командами управления справочником')

def __print_rules__():
    print('1. Для добавления записи в справочник напишите команду «Добавить» в формате: \n\t-Добавить ИМЯ ФАМИЛИЯ НОМЕР')
    print('2. Для поиска записи в файле необходимо ввести команду «ПОИСК» в формате: \n\t- Поиск ИМЯ;\n\t- Поиск ФАМИЛИЯ;\n\t- Поиск ИМЯ ФАМИЛИЯ')
    print('3. Для удаления товара введите команду «Удалить» в формате: \n\t- Удалить НОМЕР')
    print('4. Для повторного вывода информации используйте команду «Команды»')

def start(phone_dict):
    __print_start_messege__()
    __print_rules__()
    while True:
        cmd = input().lower()
        if cmd == 'команды': __print_rules__()
        elif cmd == 'стоп': break
        else: phone_dict.command_manager(cmd)
