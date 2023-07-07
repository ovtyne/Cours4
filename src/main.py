from src.JSONSaver import JSONSaver
from src.headHunterAPI import HeadHunterAPI
from src.superJobAPI import SuperJobAPI


if __name__ == '__main__':
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    #hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    # Получение вакансий с разных платформ
    #hh_vacancies = hh_api.get_vacancies("Python")
    superjob_vacancies = superjob_api.get_vacancies("Python")

    json_saver = JSONSaver()
    json_saver.save_vacancies(superjob_vacancies)

