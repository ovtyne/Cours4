from abc import ABC, abstractmethod


class APIs(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass