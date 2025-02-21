import pytest
import requests
from unittest.mock import patch


def test_connection_success(hh_parser, mock_response):
    """Тест успешного соединения с API."""

    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        response = hh_parser._connection()

        assert response == mock_response
        assert "items" in response
        assert response["items"][0]["name"] == "Python Developer"


def test_connection_failure(hh_parser):
    """Тест обработки ошибки соединения."""
    with patch("requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("Ошибка соединения")

        response = hh_parser._connection()

        assert response is None


def test_get_data_success(hh_parser, mock_response):
    """Тест успешного получения данных."""

    with patch.object(hh_parser, "_connection", return_value=mock_response):
        vacancies = hh_parser.get_data()

        assert isinstance(vacancies, list)
        assert len(vacancies) == 1
        assert vacancies[0]["name"] == "Python Developer"


def test_get_data_empty_response(hh_parser):
    """Тест обработки пустого ответа API."""
    with patch.object(hh_parser, "_connection", return_value={"items": []}):
        vacancies = hh_parser.get_data()

        assert vacancies == []


def test_get_data_no_items_key(hh_parser):
    """Тест, если в ответе API отсутствует ключ 'items'."""
    with patch.object(hh_parser, "_connection", return_value={}):
        vacancies = hh_parser.get_data()

        assert vacancies == []
