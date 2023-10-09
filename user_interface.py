def print_start_messege():
    print('Добро пожаловать в телефонный справочник')
    print('Ознакомьтесь с командами управления справочником')

def print_rules():
    print('1. Для добавления записи в справочник напишите команду «Добавить» в формате: \n\t-Добавить ИМЯ ФАМИЛИЯ НОМЕР')
    print('2. Для поиска записи в файле необходимо ввести команду «ПОИСК» в формате: \n\t- Поиск ИМЯ;\n\t- Поиск ФАМИЛИЯ;\n\t- Поиск ИМЯ ФАМИЛИЯ')
    print('3. Для удаления товара введите команду «Удалить» в формате: \n\t- Удалить НОМЕР')
    print('4. Для повторного вывода информации используйте команду «Команды»')

def valid_command():
    command = input()
    if command == '':
        return -1
    split_command = command.split()
    head_cmd = split_command[0].lower() 
    if head_cmd == 'добавить':
        if len(split_command) == 4:
            return 'добавить'
        else: return 'неправильный ввод'
    
    elif head_cmd == 'поиск':
        if len(split_command) == 3 or len(split_command) == 2:
            return 'поиск'
        else: return 'неправильный ввод'

    elif head_cmd == 'удалить':
        if len(split_command) == 2:
            return 'удалить'
        else: return 'неправильный ввод'

    elif head_cmd == 'команды':
        if len(split_command) == 1:
            return 'команды'
        else: return 'неправильный ввод'
    else:
        print('Такой команды нет')
    
