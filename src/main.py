from src.JSONSaver import JSONSaver
from src.headHunterAPI import HeadHunterAPI
from src.superJobAPI import SuperJobAPI
from src.vacancies import Vacancies

if __name__ == '__main__':
    json_saver = JSONSaver()
    vacancies = []

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    answer = "y"
    if json_saver.is_file_saved():
        answer = input("загрузить данные из файла? (д/н)").lower()
    top_n = int(input("Введите количество вакансий для вывода: "))
    keywords = input("Введите ключевые слова для фильтрации вакансий: ").split()

    if answer in ('y', 'д', 'да'):
        vacancies = json_saver.load_vacancies()
    else:
        # Получение вакансий с разных платформ
        print('\nЗагружаем данные из интернет\n')
        vacancies = hh_api.get_vacancies(keywords)
        sj_vacancies = superjob_api.get_vacancies(keywords)
        vacancies.extend(sj_vacancies)
        # Сохранение информации о вакансиях в файл
        json_saver.save_vacancies(vacancies)

    if not vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")

    #Сортировка вакансий и вывод на экран избранного
    top_vacancies = Vacancies.get_top_vacancies_by_payment(vacancies, top_n)
    Vacancies.print_vacancies(top_vacancies)

    #Сохранение избранных вакансий в файл
    json_saver.save_vacancies(top_vacancies, "FilteredVacancies.json")

