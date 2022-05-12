class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.__name = name
        self.__surname = surname
        self.__position = position
        self._income = dict(wage=wage, bonus=bonus)

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_position(self):
        return self.__position

    def get_income(self):
        return self._income

    def get_wage_income(self):
        return self._income['wage']

    def get_bonus_income(self):
        return self._income['bonus']


class Position(Worker):
    def get_full_name(self):
        return f'Name: {self.get_name()}\n' \
               f'Surname: {self.get_surname()}'

    def get_total_income(self):
        return f"Total income: {self.get_wage_income() + self.get_bonus_income()}"


first_worker = Position('Joshua', 'Brown', 'teacher', 50000, 20000)
second_worker = Position('Emmanuel', 'Zvavamve', 'translator', 100000, 30000)
print(first_worker.get_full_name())
print(first_worker.get_total_income())
print(second_worker.get_full_name())
print(second_worker.get_total_income())
