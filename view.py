from datetime import datetime

import controller
import note


class View:
    def __init__(self, _controller):
        self.__controller = _controller

    def run(self):
        while True:
            command = str(input('Введите команду (0 - посмотреть команды): '))
            if command.lower() == '5':
                return

            if command.lower() == '2':
                title = str(input('Введите заголовок: '))
                msg = str(input('Введите текст: '))
                if isinstance(self.__controller, controller.Controller):
                    self.__controller.save_note(note.Note('0', title, msg, str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))))
                else:
                    print('Ошибка!')


            elif command.lower() == '1':
                if isinstance(self.__controller, controller.Controller):
                    notes = self.__controller.read_notes()
                    notes.sort()
                    for _note in notes:
                        print(_note)
                else:
                    print('Ошибка')


            elif command.lower() == '4':
                note_id = str(input('Введите ID: '))
                if isinstance(self.__controller, controller.Controller):
                    self.__controller.delete_note(note_id)
                else:
                    print('Ошибка!')

            elif command.lower() == '3':
                note_id = str(input('Введите ID: '))
                title = str(input('Введите заголовок: '))
                msg = str(input('Введите текст: '))
                if isinstance(self.__controller, controller.Controller):
                    self.__controller.edit_note(note.Note(note_id, title, msg, str(datetime.now().strftime("%Y.%m.%d %H:%M:%S"))))

            elif command.lower() == '0':
                print('команды:')
                print('1 - все заметки')
                print('2 - создать заметку')
                print('3 - редактировать заметку')
                print('4 - удалить заметку')
                print('5 - выход')
            else:
                print('Ошибка!')