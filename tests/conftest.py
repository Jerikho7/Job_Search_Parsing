import json

import pytest

from src.parser import HeadHunterParser
from unittest.mock import mock_open

from src.vacancy import Vacancy


@pytest.fixture
def hh_parser():
    """Фикстура для создания экземпляра HeadHunterParsel."""
    return HeadHunterParser("Python")


@pytest.fixture
def mock_response():
    """Фикстура с тестовыми данными о вакансиях."""
    return {
        "items": [
            {
                "id": "1",
                "name": "Python Developer",
                "salary": {"from": 100000, "to": 150000},
                "alternate_url": "https://hh.ru/vacancy/1"
            }
        ]
    }


@pytest.fixture
def sample_vacancy():
    """Фикстура: тестовая вакансия"""
    return Vacancy(
        name="Python Developer",
        salary_ot=100000,
        salary_do=150000,
        responsibility="Разработка и поддержка Python-приложений",
        date="2025-02-22",
        url="https://example.com/vacancy/123"
    )


@pytest.fixture
def another_vacancy():
    """Фикстура для второй тестовой вакансии."""
    return Vacancy(
        name="Java Developer",
        salary_ot=80000,
        salary_do=120000,
        responsibility="Разработка Java-приложений",
        date="2025-02-20",
        url="https://example.com/vacancy/456"
    )


@pytest.fixture
def mock_file():
    """Фикстура: имитация работы с файлом JSON"""
    return mock_open(read_data=json.dumps([]))


@pytest.fixture
def mock_vacancies():
    return [
        {
            "name": "Software Engineer",
            "salary": {"from": 50000, "to": 70000},
            "snippet": {"responsibility": "Develop software"},
            "published_at": "2025-02-20T12:00:00+03:00",
            "alternate_url": "https://example.com/vacancy1"
        },
        {
            "name": "Data Analyst",
            "salary": {"from": 60000, "to": 80000},
            "snippet": {"responsibility": "Analyze data"},
            "published_at": "2025-02-19T10:00:00+03:00",
            "alternate_url": "https://example.com/vacancy2"
        }
    ]
