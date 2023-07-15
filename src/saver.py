from abc import ABC, abstractmethod


class Saver(ABC):
    """абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл, получения данных из файла """
    @abstractmethod
    def save_vacancies(self, vacancies):
        pass

    @abstractmethod
    def load_vacancies(self):
        pass

