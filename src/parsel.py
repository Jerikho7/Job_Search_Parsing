from abc import ABC, abstractmethod

import requests


class Parsel(ABC):

    @abstractmethod
    def __connection(self):
        pass

    @abstractmethod
    def get_data(self):
        pass


class HeadHunterParsel(Parsel):
    HH_API_URL = 'https://api.hh.ru/vacancies/'

    def __init__(self, keyword):
        self.params = {
            'text': keyword,
            'per_page': 100,
            'only_with_salary': True
        }

    def __connection(self):
        """Метод проверяющий доступность API"""
        try:
            response = requests.get(self.HH_API_URL, self.params)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Ошибка: {e}")

    def get_data(self):
        data = self.__connection().json()['items']
        return data
