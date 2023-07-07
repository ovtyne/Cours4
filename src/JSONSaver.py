import json
from src.saver import Saver


class JSONSaver(Saver):
    def __init__(self):
        self.file_name = "vacancies.json"

    def save_vacancies(self, vacancies):
        with open(self.file_name, "w") as write_file:
            json.dump(vacancies, write_file, indent=2, ensure_ascii=False)

    def add_vacancy(self, vacancy):
        pass

    def get_vacancies_by_salary(self, salary="100 000-150 000 руб."):
        pass

    def delete_vacancy(self, vacancy):
        pass

