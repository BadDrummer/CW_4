import json
from abc import ABC, abstractmethod


class BaseFileWorker(ABC):
    """Add vacancy to file"""
    @abstractmethod
    def insert(self, data):
        pass

    """Get all vacancies from file"""
    @abstractmethod
    def get_all(self):
        pass

    """Delete vacancy from file"""
    @abstractmethod
    def delete(self, query):
        pass


class JSONWorker(BaseFileWorker):
    """Validation"""
    def __init__(self, file_path):
        self.__file_path = file_path
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump([], file, ensure_ascii=False, indent=2)

    def insert(self, data):
        file_data = self.get_all()
        file_data.append(data)
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(file_data, file, ensure_ascii=False, indent=2)

    def get_all(self):
        with open(self.__file_path, encoding='utf-8') as file:
            file_data = json.load(file)
        return file_data

    def delete(self, query: dict):
        file_data = self.get_all()

        for_save = []
        deleted = []
        for data in file_data:
            if not all(data.get(param) == value for param, value in query.items()):
                for_save.append(data)
            else:
                deleted.append(data)

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(for_save, file, ensure_ascii=False, indent=2)

        return deleted
