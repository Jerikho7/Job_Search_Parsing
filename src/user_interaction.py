from datetime import datetime, date

from src.parser import HeadHunterParser
from src.vacancy import Vacancy
from src.vacancy_saver import VacancySaverJson


def user_interaction():
    print('Поиск вакансий на сайте hh.ru.')
    keyword = input("Введите ключевые слова для поиска вакансий: ").strip()

    if not keyword:
        print("Ошибка: ключевое слово не может быть пустым.")
        return

    hh_api = HeadHunterParser(keyword)
    vacancies_data = hh_api.get_data()

    if not vacancies_data:
        print("По вашему запросу вакансий не найдено.")
        return

    # Очистка старого списка вакансий и добавление новых
    Vacancy.all.clear()
    for vac in vacancies_data:
        raw_date = vac.get("published_at")
        formatted_date = datetime.strptime(raw_date, "%Y-%m-%dT%H:%M:%S%z").strftime(
            "%d.%m.%Y") if raw_date else "Не указано"

        Vacancy(
            name=vac.get("name"),
            salary_ot=vac.get("salary", {}).get("from"),
            salary_do=vac.get("salary", {}).get("to"),
            responsibility=vac.get("snippet", {}).get("responsibility", "Не указано"),
            date=formatted_date,
            url=vac.get("alternate_url")
        )

    user_answer = input('Сортировать вакансии по убыванию зарплаты? (yes/no): ').strip().lower()

    if user_answer == 'yes':
        sorted_vacancies = sorted(Vacancy.all, key=lambda x: -int(x))
        view_number = int(input('Сколько вакансий вывести? '))
        for item in sorted_vacancies[:view_number]:
            print(f"{item.name} - {int(item)} руб.")
    else:
        user_answer = input('Вывести вакансию с максимальной зарплатой? (yes/no): ').strip().lower()
        if user_answer == 'yes':
            Vacancy.get_max()
        else:
            view_number = int(input('Сколько вакансий вывести? '))
            Vacancy.print_info_all(view_number)

    save_answer = input('Хотите сохранить вакансии в файл? (yes/no): ').strip().lower()
    if save_answer == 'yes':
        file_name = input('Введите имя файла (например, vacancies.json): ').strip()
        js_saver = VacancySaverJson(file_name)
        for vacancy in Vacancy.all:
            js_saver.add_vacancy(vacancy)
        print(f'Вакансии сохранены в файл {file_name}.')

    print('Всего доброго!')
