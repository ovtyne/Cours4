import json
import requests

from src.APIs import APIs


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
        print(type(response))
        return response

    def get_vacancies(self, keyword='Python', pages=1):
        v = {}
        for page in range(pages):
            v.update(self.get_request(keyword=keyword, page=page))

        vacancies = json.dumps(v, ensure_ascii=False, indent=2)

        print(vacancies)
        return vacancies
