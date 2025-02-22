import json
from abc import ABC, abstractmethod

class VacancySaver(ABC):
    """
    Абстрактный класс для сохранения вакансий.
    """
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, criteria: dict = None) -> list:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        pass


class VacancySaverJson(VacancySaver):
    """Реализация хранения вакансий в JSON-файле."""
    def __init__(self, file_path="data/vacancies.json"):
        self.file_path = file_path

    def _load_data(self) -> list:
        """Загружает данные из JSON - файла."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Ошибка: Файл данных поврежден. Используется пустой список.")
            return []

    def _save_data(self, data: list):
        """Сохраняет данные в JSON-файл."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: Vacancy):
        """Добавляет вакансию в JSON-файл."""
        data = self._load_data()
        data.append(vacancy.to_dict())
        self._save_data(data)
        print(f"Вакансия '{vacancy.title}' добавлена.")

    def get_vacancies(self, criteria: dict = None) -> list:
        """Получает список вакансий с фильтрацией по критериям."""
        data = self._load_data()
        vacancies = [Vacancy.from_dict(item) for item in data]

        if criteria:
            if "keyword" in criteria:
                vacancies = [v for v in vacancies if criteria["keyword"].lower() in v.description.lower()]
            if "min_salary" in criteria:
                vacancies = [v for v in vacancies if v.salary >= criteria["min_salary"]]
            if "max_salary" in criteria:
                vacancies = [v for v in vacancies if v.salary <= criteria["max_salary"]]

        return vacancies

    def delete_vacancy(self, vacancy: Vacancy):
        """Удаляет вакансию из JSON-файла по URL."""
        data = self._load_data()
        new_data = [item for item in data if item.get("url") != vacancy.url]

        if len(new_data) == len(data):
            print("Ошибка: Вакансия не найдена.")
            return

        self._save_data(new_data)
        print(f"Вакансия '{vacancy.title}' удалена.")
