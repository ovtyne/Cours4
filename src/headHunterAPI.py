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

    def get_vacancies(self, keyword='Python', vac_n=200):
        pages = math.ceil(vac_n/100)
        v = {}

        for page in range(pages):
            request = self.get_request(keyword=keyword, page=page)
            if len(request['items']):
                v.update(request)

        vacancies = []

        if not len(v['items']):
            return vacancies

        for d in range(len(v)):
            pay = v['items'][d]['salary']

            if pay is None:
                pay_from = 0
                pay_to = 0
            else:
                pay_from = pay['from']
                pay_to = pay['to']
            vacancy = Vacancies(
                v['items'][d]['name'],
                v['items'][d]['alternate_url'],
                pay_from,
                pay_to,
                '',
                'HH'
            )
            vacancies.append(vacancy)

        return vacancies
