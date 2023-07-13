import json
from src.saver import Saver
from src.vacancies import Vacancies


class VacanciesEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, Vacancies):
            return z.title, z.url, z.payment_from, z.payment_to, z.description, z.platform
        else:
            super().default(self, z)


class JSONSaver(Saver):
    def get_vacancies_by_salary(self, salary):
        pass

    def delete_vacancy(self, vacancy):
        pass

    def add_vacancy(self, vacancy):
        pass

    def __init__(self):
        self.file_name = "vacancies.json"

    def save_vacancies(self, vacancies):
        with open(self.file_name, "w") as write_file:
            json.dump(vacancies, write_file, indent=2, ensure_ascii=False, cls=VacanciesEncoder)

