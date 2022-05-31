class Date:

    def __init__(self, date):
        self.__date = Date.__date_to_int(date)

    @classmethod
    def __date_to_int(cls, string_date):
        try:
            result_date = tuple(map(int, string_date.split('-')))
            if Date.__is_date_valid(result_date):
                return result_date
            else:
                raise ValueError()
        except Exception as err:
            raise err

    @staticmethod
    def __is_date_valid(checked_date):
        if len(checked_date) != 3:
            return False
        return 1 <= checked_date[0] <= 31 and 1 <= checked_date[1] <= 12 and checked_date[2] > 0

    def __str__(self):
        return f'{self.__date[0]:02d}-{self.__date[1]:02d}-{self.__date[2]}'


new_date = Date(input("Type a date (for ex. 01-01-1970): "))
print(new_date)
