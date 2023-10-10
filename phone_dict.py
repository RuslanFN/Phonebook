import os

class Note():
    def __init__(self, f_name, s_name, number):
        self.f_name = f_name
        self.s_name = s_name
        self.number = number
    def to_str(self):
        return f"{self.f_name} {self.s_name}: {self.number}"


class dictionary():
    def __init__(self, file_name = 'dict_number.txt'):
        self.file_name = file_name
        self.f = open(file_name, 'r')
        self.notes = []
        print(self.f)
        for note in self.f:   
            split_note = note.split()
            if len(split_note) == 3:
                self.notes.append(Note(split_note[0], split_note[1][:-1], split_note[2]))
        print([note.to_str() for note in self.notes])
        self.f.close()
    def __add_note__(self, f_name, s_name, number):
        self.f = open(self.file_name, 'a')
        if not number in [n.number for n in self.notes]:
            note = Note(f_name, s_name, number) 
            self.notes.append(note)
            self.f.write(note.to_str() + '\n')
            print('Номер добавлен')
        else:
            print('Такой номер уже есть')
        self.f.close()
    def __find_note__(self, f_name = '', s_name = ''):
        if f_name != '' and s_name == '':
            notes_by_name = []
            for note in self.notes:
                if note.f_name == f_name:
                    notes_by_name.append(note)
            if notes_by_name: print(*[note.to_str() for note in notes_by_name], sep='\n')
            else: print('Номер не найден')
        elif f_name == '' and s_name != '':
            notes_by_sname = []
            for note in self.notes:
                if note.s_name == s_name:
                    notes_by_sname.append(note)
            if notes_by_sname: print(*[note.to_str() for note in notes_by_sname], sep='\n')
            else: print('Номер не найден')
        elif f_name != '' and s_name != '':
            notes_by_fname_and_sname = []
            for note in self.notes:
                if note.f_name == f_name and note.s_name == s_name:
                    notes_by_fname_and_sname.append(note)
            if notes_by_fname_and_sname:print(*[note.to_str() for note in notes_by_fname_and_sname], sep='\n')
            else: print('Номер не найден')
        else: print('Номер не найден')
    def __del_note__(self, number):
        try:
            i = [n.number for n in self.notes].index(number)
        except ValueError:
            print('Такого номера нет.')
        else:
            self.notes.pop(i)
            self.f.close()
            os.remove(self.file_name)
            f = open(self.file_name, 'a+')
            f.writelines([note.to_str() for note in self.notes])
            self.f = f
            print('Номер удалён')
    def command_manager(self, cmd):
        split_cmd = cmd.split()
        if split_cmd:
            head = split_cmd[0]
            args = []
            if len(split_cmd) > 1:
                args = split_cmd[1:]
            if head == 'добавить' and len(args) == 3:
                self.__add_note__(*args)
            elif head == 'поиск' and len(args) == 2 or len(args) == 3:
                self.__find_note__(*args)
            elif head == 'удалить' and len(args) == 1:
                self.__del_note__(*args)
            else: print('Нверная команда')
        else: print('Нверная команда')
            
            
        


