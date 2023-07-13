import json

from src.JSONSaver import JSONSaver
from src.headHunterAPI import HeadHunterAPI
from src.superJobAPI import SuperJobAPI

if __name__ == '__main__':
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    top_n = int(input("Введите количество вакансий для вывода: "))
    keywords = input("Введите ключевые слова для фильтрации вакансий: ").split()

    # Получение вакансий с разных платформ
    vacancies = hh_api.get_vacancies(keywords, top_n)
    sj_vacancies = superjob_api.get_vacancies(keywords, top_n)
    vacancies.extend(sj_vacancies)

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    json_saver.save_vacancies(vacancies)

    if not vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")

    for vacancy in vacancies:
        print(vacancy)
