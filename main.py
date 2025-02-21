from src.parser import HeadHunterParsel

if __name__ == '__main__':
    # блок кода HeadHunterAPI
    hh_vacancies = HeadHunterParsel('тестировщик')
    hh_vacancies.get_data()
    vacancies = hh_vacancies.get_data()
    print(vacancies)

