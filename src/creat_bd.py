import json
from abc import ABC, abstractmethod


class FileWork(ABC):

    @abstractmethod
    def read_file(self):
        """Чтение файла"""
        pass

    @abstractmethod
    def save_file(self, data):
        """Сохранения файла"""
        pass

    @abstractmethod
    def del_file(self):
        """Удаление"""
        pass


class WorkWithJson(FileWork):
    """Класс по работе с JSON файлом"""

    def __init__(self):
        self.__file_name = "vacancy.json"

    def read_file(self):
        """Считывание данных из JSON файла"""
        with open(f"data/{self.__file_name}", "r", encoding="utf-8") as file:
            return json.load(file)

    def save_file(self, data):
        """Добавляет новые данные в JSON файл"""
        vacancy = []
        try:
            vacancy.extend(self.read_file())
        except json.decoder.JSONDecodeError as err:
            pass
        vacancy.extend(data)
        with open(f"data/{self.__file_name}", 'w', encoding='utf-8') as file:
            json.dump(vacancy, file, ensure_ascii=False, indent=4)

    def del_file(self):
        """Удаление данных из JSON файла"""
        with open(f"data/{self.__file_name}", "w") as file:
            pass
