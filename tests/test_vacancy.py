from src.vacancy import Vacancy


def test_vacancy_creation(sample_vacancy):
    """Тест создания вакансии"""
    assert sample_vacancy.name == "Python Developer"
    assert sample_vacancy.salary_ot == 100000
    assert sample_vacancy.salary_do == 150000
    assert sample_vacancy.responsibility == "Разработка и поддержка Python-приложений"
    assert sample_vacancy.date == "2025-02-22"
    assert sample_vacancy.url == "https://example.com/vacancy/123"


def test_vacancy_str(sample_vacancy):
    """Тест строкового представления вакансии"""
    assert str(sample_vacancy) == "Вакансия Python Developer"


def test_vacancy_salary_subtraction(sample_vacancy, another_vacancy):
    """Тест оператора вычитания (разница зарплат)"""
    assert sample_vacancy - another_vacancy == 20000  # 100000 - 80000


def test_vacancy_comparison(sample_vacancy, another_vacancy):
    """Тест операторов сравнения по salary_ot"""
    assert sample_vacancy >= another_vacancy  # 100000 >= 80000
    assert another_vacancy <= sample_vacancy  # 80000 <= 100000
    assert not (another_vacancy >= sample_vacancy)  # 80000 >= 100000 (False)


def test_vacancy_conversion_to_int(sample_vacancy, another_vacancy):
    """Тест метода __int__ (средняя зарплата)"""
    assert int(sample_vacancy) == 125000  # (100000 + 150000) / 2
    assert int(another_vacancy) == 100000  # (80000 + 120000) / 2


def test_vacancy_to_dict(sample_vacancy):
    """Тест конвертации вакансии в словарь"""
    vacancy_dict = sample_vacancy.to_dict()

    assert vacancy_dict["name"] == "Python Developer"
    assert vacancy_dict["url"] == "https://example.com/vacancy/123"
    assert vacancy_dict["salary_ot"] == 100000
    assert vacancy_dict["salary_do"] == 150000
    assert vacancy_dict["responsibility"] == "Разработка и поддержка Python-приложений"
    assert vacancy_dict["date"] == "2025-02-22"


def test_vacancy_from_dict():
    """Тест восстановления вакансии из словаря"""
    data = {
        "name": "Data Scientist",
        "url": "https://example.com/vacancy/789",
        "salary_ot": 120000,
        "salary_do": 180000,
        "responsibility": "Разработка моделей машинного обучения"
    }
    vacancy = Vacancy.from_dict(data)

    assert vacancy.name == "Data Scientist"
    assert vacancy.url == "https://example.com/vacancy/789"
    assert vacancy.salary_ot == 120000
    assert vacancy.salary_do == 180000
    assert vacancy.responsibility == "Разработка моделей машинного обучения"
