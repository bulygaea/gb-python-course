class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.__name = name
        self.__surname = surname
        self.__position = position
        self._income = dict(wage=wage, bonus=bonus)

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def position(self):
        return self.__position

    @property
    def income(self):
        return self._income

    @property
    def wage_income(self):
        return self._income['wage']

    @property
    def bonus_income(self):
        return self._income['bonus']


class Position(Worker):
    @property
    def full_name(self):
        return f'Name: {self.name}\n' \
               f'Surname: {self.surname}'

    @property
    def total_income(self):
        return f'Total income: {self.wage_income + self.bonus_income}'


first_worker = Position('Joshua', 'Brown', 'teacher', 50000, 20000)
second_worker = Position('Emmanuel', 'Zvavamve', 'translator', 100000, 30000)
print(first_worker.full_name)
print(first_worker.total_income)
print(second_worker.full_name)
print(second_worker.total_income)
