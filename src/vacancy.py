class Vacancy:
    """
        Класс для представления вакансии.
        """
    all = []

    def __init__(self, name, salary_ot, salary_do, responsibility, date, url):
        """
        Инициализация объекта вакансии.

        :param name: Название вакансии
        :param salary_ot: Нижняя граница зарплаты (может быть None)
        :param salary_do: Верхняя граница зарплаты (может быть None)
        :param responsibility: Обязанности по вакансии
        :param date: Дата публикации вакансии
        :param url: Ссылка на вакансию
        """
        self.name = name
        self.salary_ot = salary_ot
        self.salary_do = salary_do
        self.responsibility = responsibility
        self.date = date
        self.url = url
        self.__class__.all.append(self)

    def __str__(self):
        """
        Возвращает строковое представление вакансии.
        """
        return f'Вакансия {self.name}'

    def __sub__(self, other):
        """
        Вычитает нижние границы зарплат двух вакансий.

        :param other: Другой объект Vacancy
        :return: Разница в зарплате
        :raises Exception: Если other не является объектом Vacancy
        """
        if isinstance(other, Vacancy):
            return float(self.salary_ot or 0) - float(other.salary_ot or 0)
        else:
            raise TypeError("Вычитать можно только между элементами одного типа")

    def __le__(self, other):
        """
        Сравнивает вакансии по нижней границе зарплаты (salary_ot).

        :param other: Объект Vacancy или число (float)
        :return: True, если текущая вакансия имеет зарплату не ниже, чем у другой вакансии
        :raises ValueError: Если сравнение невозможно
        """
        if isinstance(other, Vacancy):
            return (self.salary_ot or 0) <= (other.salary_ot or 0)
        elif isinstance(other, (int, float)):
            return (self.salary_ot or 0) <= other
        else:
            raise ValueError("Несравниваемые объекты")

    def __ge__(self, other):
        """
        Сравнивает вакансии по нижней границе зарплаты (salary_ot).

        :param other: Объект Vacancy или число (float)
        :return: True, если текущая вакансия имеет зарплату не выше, чем у другой вакансии
        :raises ValueError: Если сравнение невозможно
        """
        if isinstance(other, Vacancy):
            return (self.salary_ot or 0) >= (other.salary_ot or 0)
        elif isinstance(other, (int, float)):
            return (self.salary_ot or 0) >= other
        else:
            raise ValueError("Несравниваемые объекты")

    def __int__(self):
        """
        Возвращает среднее значение зарплаты.

        :return: Средняя зарплата или 0, если данные не указаны
        """
        if self.salary_ot is not None and self.salary_do is not None:
            return int((self.salary_ot + self.salary_do) / 2)
        elif self.salary_ot is not None:
            return int(self.salary_ot)
        elif self.salary_do is not None:
            return int(self.salary_do)
        else:
            return 0

    def to_dict(self):
        """Преобразование объекта в словарь для сохранения в JSON."""
        return {
            "name": self.name,
            "salary_ot": self.salary_ot,
            "salary_do": self.salary_do,
            "responsibility": self.responsibility,
            "date": self.date,
            "url": self.url
        }

    @staticmethod
    def from_dict(data: dict):
        """Создание объекта Vacancy из словаря."""
        return Vacancy(
            name=data.get("name"),
            salary_ot=data.get("salary_ot"),
            salary_do=data.get("salary_do"),
            responsibility=data.get("responsibility"),
            date=data.get("date"),
            url=data.get("url")
        )

    @classmethod
    def get_max(cls):
        """
        Определяет и выводит вакансии с максимальной нижней границей зарплаты.
        """
        all_salaries = {}

        for vacancy in cls.all:
            if vacancy.salary_ot is not None:
                all_salaries[vacancy.name] = int(vacancy.salary_ot)
            else:
                all_salaries[vacancy.name] = 0

        if not all_salaries:
            print("Нет вакансий для анализа.")
            return

        max_salary = max(all_salaries.values())
        max_list = [name for name, salary in all_salaries.items() if salary == max_salary]

        print(f'Вакансии с максимальной зарплатой {max_salary} рублей: {max_list}')
        print('Информация по данным вакансиям:')
        for vacancy in cls.all:
            if vacancy.name in max_list:
                vacancy.print_info()

    def print_info(self, number=None):
        """
        Выводит информацию о вакансии.

        :param number: Номер вакансии в списке (необязательно)
        """
        if number:
            print(f'{number} - опубликовано {self.date} {self.name}:')
        else:
            print(f'Опубликовано {self.date} {self.name}:')

        print(f'Обязанности: {self.responsibility if self.responsibility else "не указано"}')

        if self.salary_ot is None and self.salary_do is None:
            print('Зарплата: не указана')
        elif self.salary_ot is None:
            print(f'Зарплата: до {self.salary_do} рублей')
        elif self.salary_do is None:
            print(f'Зарплата: от {self.salary_ot} рублей')
        else:
            print(f'Зарплата: от {self.salary_ot} до {self.salary_do} рублей')
        print()

    @classmethod
    def print_info_all(cls, length_list=None):
        """
        Выводит информацию о всех вакансиях, ограничивая количество по желанию.

        :param length_list: Количество вакансий для отображения (если None, выводятся все)
        """
        print('Вакансии:\n')
        for idx, vac in enumerate(cls.all[:length_list] if length_list else cls.all, 1):
            vac.print_info(idx)
