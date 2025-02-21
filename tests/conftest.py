import pytest

from src.parser import HeadHunterParser


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
