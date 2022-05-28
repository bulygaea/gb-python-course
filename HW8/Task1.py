class Date:
    date = ''

    @staticmethod
    def __init__(date):
        Date.date = date

    @classmethod
    def date_to_int(cls):
        try:
            if len(tuple(Date.date.split('-'))) == 3:
                return tuple(map(int, Date.date.split('-')))
            else:
                raise ValueError()
        except Exception as err:
            raise err

    @staticmethod
    def is_date_valid():
        checked_date = Date.date_to_int()
        try:
            return 1 <= checked_date[0] <= 31 and 1 <= checked_date[1] <= 12 and checked_date[2] > 0
        except Exception as err:
            raise err


Date(input("Type a date (for ex. 01-01-1970): "))
print(Date.date_to_int())
print(Date.is_date_valid())
