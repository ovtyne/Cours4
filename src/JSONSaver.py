import json
from os import path

from src.saver import Saver
from src.vacancies import Vacancies


def is_complex(z):
    """Служебная функция для работы метода десериализации JSON"""
    return Vacancies(
            z['title'],
            z['url'],
            z['payment_from'],
            z['payment_to'],
            z['description'],
            z['platform']
    )


class JSONSaver(Saver):
    """класс для сохранения информации о вакансиях в JSON-файл"""
    def save_vacancies(self, vacancies, filename="vacancies.json"):
        """метод для сохранения информации о вакансиях в JSON-файл"""
        with open(filename, "w") as write_file:
            json.dump(vacancies, write_file, indent=2, ensure_ascii=False, default=lambda x: x.__dict__)

    def is_file_saved(self, filename="vacancies.json"):
        """Проверка, существует ли файл с ранее сохраненными вакансиями"""
        return path.exists(filename)

    def load_vacancies(self, filename="vacancies.json"):
        """метод для загрузки информации о вакансиях из JSON-файла"""
        with open(filename, "r") as file:
            return json.load(file, object_hook=is_complex)

