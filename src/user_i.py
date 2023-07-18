from src.JSONSaver import JSONSaver
from src.vacancies import Vacancies


def user_i(vacancies):
    """
    Функция взаимодействия с пользователем
    :param vacancies:
    :return:
    """
    json_saver = JSONSaver()

    while True:
        com = input('\nВыберите 0 - 4:\n'
                    '1 - Сортировать по возрастанию зарплаты;\n'
                    '2 - Сортировать по убыванию зарплаты;\n'
                    '3 - Вывести топ вакансий;\n'
                    '4 - Сохранить в отдельный файл FilteredVacancies.json\n'
                    '0 - Выход;\n'
                    )

        if com == '0':  # exit
            return
        elif com == '1':  # sort asc
            vacancies = Vacancies.sort_vacancies_by_payment(vacancies, False)
        elif com == '2':  # sort dsc
            vacancies = Vacancies.sort_vacancies_by_payment(vacancies)
        elif com == '3':  # print top n
            print_n = int(input("\n\tВведите количество вакансий для вывода: "))
            Vacancies.print_top_vacancies(vacancies, print_n)
        elif com == '4':  # save results
            json_saver.save_vacancies(vacancies, "FilteredVacancies.json")
            print('\n\tДанные сохранены в файл FilteredVacancies.json')
