from abc import ABC, abstractmethod


class APIs(ABC):
    """абстрактный класс для работы с API сайтов с вакансиями"""
    @abstractmethod
    def get_vacancies(self, keywords):
        pass