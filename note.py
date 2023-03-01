class Note:
    def __init__(self, id, title, text, date):
        self.__id = id
        self.__title = title
        self.__text = text
        self.__date = date

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_text(self, text):
        self.__text = text

    def get_text(self):
        return self.__text

    def set_date(self, date):
        self.__date = date

    def get_date(self):
        return self.__date

    def __str__(self):
        return 'ID: ' + self.__id + '. Заголовок: ' + self.__title + '. Текст: ' + self.__text + \
            '. Date modified: ' + self.__date

    def __lt__(self, other):
        return self.__date < other.get_date()
