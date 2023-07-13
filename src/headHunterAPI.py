import math
import requests

from src.vacancies import Vacancies
from src.APIs import APIs


class HeadHunterAPI(APIs):
    def get_request(self, keyword='Python', page=0):
        url = "https://api.hh.ru/vacancies"

        params = {
            'text': f'NAME:{keyword}',  # Текст фильтра.
            'area': 1,  # Поиск ощуществляется по вакансиям города Москва
            'page': page,  # Индекс страницы поиска на HH
            'per_page': 100,  # Кол-во вакансий на 1 странице
            'archive': False
        }

        response = requests.get(url, params).json()  # Посылаем запрос к API
        return response

    def get_vacancies(self, keyword='Python', vac_n=500):
        pages = math.ceil(vac_n/100)
        hh_vacancies = []

        for page in range(pages):
            request = self.get_request(keyword=keyword, page=page)
            if len(request['items']):
                hh_vacancies.extend(request['items'])

        vacancies = []

        if not len(hh_vacancies):
            return vacancies

        pay = []
        for v in hh_vacancies:
            pay_from = 0
            pay_to = 0

            if isinstance(pay, dict):
                if type(v['salary']['from']) == int:
                    pay_from = v['salary']['from']
                if type(v['salary']['to']) == int:
                    pay_to = v['salary']['to']

            vacancy = Vacancies(
                v['name'],
                v['alternate_url'],
                pay_from,
                pay_to,
                '',
                'HH'
            )
            vacancies.append(vacancy)

        return vacancies
