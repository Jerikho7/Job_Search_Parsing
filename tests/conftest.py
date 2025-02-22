import json

import pytest

from src.parser import HeadHunterParser
from unittest.mock import mock_open


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
        title="Python Developer",
        url="https://hh.ru/vacancy/1",
        salary=120000,
        description="Разработка на Python"
    )


@pytest.fixture
def mock_file():
    """Фикстура: имитация работы с файлом JSON"""
    return mock_open(read_data=json.dumps([]))
