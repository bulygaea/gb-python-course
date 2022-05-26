class Date:
    date = ''

    def __init__(self, date):
        Date.date = date

    @classmethod
    def date_to_int(cls):
        try:
            return tuple(map(int, Date.date.split('-')))
        except Exception as err:
            return err

    @staticmethod
    def is_date_valid():
        checked_date = Date.date_to_int()
        try:
            return 1 <= checked_date[0] <= 31 and 1 <= checked_date[1] <= 12 and checked_date[2] > 0
        except Exception as err:
            return err


date = Date(input("Type a date (for ex. 01-01-1970): "))
print(Date.date_to_int())
print(Date.is_date_valid())
