from abc import ABC, abstractmethod

import requests


class Parser(ABC):
    """Абстрактный класс для работы с API сервисов вакансий."""
    @abstractmethod
    def _connection(self):
        """Метод для установления соединения с API."""
        pass

    @abstractmethod
    def get_data(self):
        """Метод для получения данных с API."""
        pass


class HeadHunterParser(Parser):
    """
        Класс для работы с API hh.ru.

        Позволяет отправлять запросы на платформу hh.ru для получения вакансий
        по заданному ключевому слову.
        """
    HH_API_URL = 'https://api.hh.ru/vacancies/'

    def __init__(self, keyword: str):
        """
        Инициализирует объект парсера HeadHunter.

        :param keyword: Ключевое слово для поиска вакансий.
        """
        self.keyword = keyword

    def _connection(self) -> dict | None:
        """
        Проверяет доступность API и отправляет запрос на сервер.

        :return: JSON-ответ от сервера в виде словаря или None в случае ошибки.
        """
        params = {
            'text': self.keyword,
            'per_page': 100,
            'only_with_salary': True
        }
        try:
            response = requests.get(self.HH_API_URL, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка: {e}")
            return None

    def get_data(self) -> list:
        """
        Получает список вакансий с hh.ru.

        :return: Список вакансий (словарей) или пустой список, если данные отсутствуют.
        """
        response_data = self._connection()
        if response_data and 'items' in response_data:
            return response_data['items']
        return []
