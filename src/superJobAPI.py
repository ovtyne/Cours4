import secret_key
import math
import requests

from src.APIs import APIs
from src.vacancies import Vacancies


class SuperJobAPI(APIs):
    def get_request(self, keywords, page=0):
        """подключается к API и получает вакансии с применением фильтра"""
        url = "https://api.superjob.ru/2.0/vacancies/"

        params = {
            "count": 100,
            "page": page,
            "archive": False,
            'keywords': f'{keywords}'
        }
        #код, получаемый с HeadHunter при регистрации, сохраненный в файле secret_key.py
        headers = secret_key
        response = requests.get(url, headers=headers, params=params).json()
        return response

    def get_vacancies(self, keywords, vac_n=100):
        """олучает вакансии, оставляет только нужные данные и возвращает список вакансий"""
        pages = math.ceil(vac_n / 100)
        v = {}
        for page in range(pages):
            request = self.get_request(keywords, page=page)
            if len(request['objects']):
                v.update(request)

        vacancies = []
        if not len(v['objects']):
            return vacancies

        for d in range(len(v)):
            pay_from = 0
            pay_to = 0
            if isinstance(v['objects'][d]['payment_from'], int):
                pay_from = v['objects'][d]['payment_from']
            if isinstance(v['objects'][d]['payment_to'], int):
                pay_to = v['objects'][d]['payment_to']
            vacancy = Vacancies(
                v['objects'][d]['profession'],
                v['objects'][d]['link'],
                pay_from,
                pay_to,
                v['objects'][d]['candidat'],
                'SJ'
            )
            vacancies.append(vacancy)

        return vacancies
