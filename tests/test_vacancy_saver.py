import json
from unittest.mock import mock_open

from src.vacancy_saver import VacancySaverJson


def test_add_vacancy(mocker, sample_vacancy):
    """Тест: добавление вакансии"""
    mocker.patch("builtins.open", mock_open())  # Имитация работы с файлом
    vacancy_saver = VacancySaverJson("test_vacancies.json")

    vacancy_saver.add_vacancy(sample_vacancy)

    open.assert_called_once_with("test_vacancies.json", "w", encoding="utf-8")  # Проверяем запись в файл


def test_get_vacancies(mocker, sample_vacancy):
    """Тест: получение списка вакансий"""
    mock_data = json.dumps([sample_vacancy.to_dict()])
    mocker.patch("builtins.open", mock_open(read_data=mock_data))

    vacancy_saver = VacancySaverJson("test_vacancies.json")
    vacancies = vacancy_saver.get_vacancies()

    assert len(vacancies) == 1
    assert vacancies[0].title == "Python Developer"


def test_get_vacancies_filtered(mocker, sample_vacancy):
    """Тест: фильтрация вакансий по ключевому слову и зарплате"""
    mock_data = json.dumps([sample_vacancy.to_dict()])
    mocker.patch("builtins.open", mock_open(read_data=mock_data))

    vacancy_saver = VacancySaverJson("test_vacancies.json")

    filtered_vacancies = vacancy_saver.get_vacancies({"keyword": "Python", "min_salary": 100000})
    assert len(filtered_vacancies) == 1

    filtered_vacancies = vacancy_saver.get_vacancies({"keyword": "Java"})
    assert len(filtered_vacancies) == 0


def test_delete_vacancy(mocker, sample_vacancy):
    """Тест: удаление вакансии"""
    mock_data = json.dumps([sample_vacancy.to_dict()])
    mocker.patch("builtins.open", mock_open(read_data=mock_data))

    vacancy_saver = VacancySaverJson("test_vacancies.json")
    vacancy_saver.delete_vacancy(sample_vacancy)

    open.assert_called_with("test_vacancies.json", "w", encoding="utf-8")
