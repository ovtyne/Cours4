import json
import requests

from src.APIs import APIs


class HeadHunterAPI(APIs):
    def get_request(self, keyword='python', page=0):
        url = "https://api.hh.ru/"

        params = {
            'text': f'NAME:{keyword}',  # Текст фильтра.
            'area': 1,  # Поиск ощуществляется по вакансиям города Москва
            'page': page,  # Индекс страницы поиска на HH
            'per_page': 100,  # Кол-во вакансий на 1 странице
            'archive': False
        }

        response = requests.get('https://api.hh.ru/vacancies', params).json()  # Посылаем запрос к API
        data = json.dumps(response, indent=2, ensure_ascii=False)
        return data

    def get_vacancies(self, keyword='python', pages=1):
        v = {}

        for page in range(pages):
            v.update(self.get_request(page))

        return v
