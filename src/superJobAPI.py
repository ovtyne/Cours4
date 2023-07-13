import json
import math
import requests

from src.APIs import APIs
from src.vacancies import Vacancies


class SuperJobAPI(APIs):
    def get_request(self, keyword='Python', page=0):
        url = "https://api.superjob.ru/2.0/vacancies/"

        params = {
            "count": 100,
            "page": page,
            "keyword": keyword,
            "archive": False
        }
        headers = {
           "X-Api-App-Id": "v3.r.137664768.383c01e40472d7c7e7446757f89483fa8bb087c2.28fd07e1e3f67bd823f92eabcebab429ba983aef"
        }
        response = requests.get(url, headers=headers, params=params).json()
        return response

    def get_vacancies(self, keyword='Python', vac_n=500):
        pages = math.ceil(vac_n / 100)
        sj_vacancies = []
        for page in range(pages):
            request = self.get_request(keyword=keyword, page=page)
            if len(request['objects']):
                sj_vacancies.extend(request['objects'])

        vacancies = []
        if not len(sj_vacancies):
            return vacancies

        for v in sj_vacancies:
            payment_from = v['payment_from']
            payment_to = v['payment_to']
            if not isinstance(payment_from, int):
                payment_from = 0
            if not isinstance(payment_to, int):
                payment_to = 0
            vacancy = Vacancies(
                v['profession'],
                v['link'],
                payment_from,
                payment_to,
                v['candidat'],
                'SJ'
            )
            vacancies.append(vacancy)

        return vacancies
