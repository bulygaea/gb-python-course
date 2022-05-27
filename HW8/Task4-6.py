from abc import ABC


class Storage:
    __office_equipments = dict(name=['printer', 'scanner', 'xerox'],
                               count_in_storage=[0, 0, 0],
                               transfer_company=[{'company': [], 'count': []},
                                                 {'company': [], 'count': []},
                                                 {'company': [], 'count': []}])
    __classes_office_equipments = dict(printer=0, scanner=1, xerox=2)

    @staticmethod
    def append_item(item):
        if isinstance(item, Printer):
            Storage.__office_equipments['count_in_storage'][0] += 1
        elif isinstance(item, Scanner):
            Storage.__office_equipments['count_in_storage'][1] += 1
        elif isinstance(item, Xerox):
            Storage.__office_equipments['count_in_storage'][2] += 1
        else:
            raise ValueError()

    @staticmethod
    def transfer(cls, company, count):
        cls = cls.lower()
        company = company.lower()
        if not isinstance(count, int):
            raise ValueError()
        if cls in Storage.__classes_office_equipments.keys():
            index = Storage.__classes_office_equipments.get(cls)
        else:
            raise ValueError()

        if Storage.__office_equipments['count_in_storage'][index] < count:
            raise OverflowError
        Storage.__office_equipments['count_in_storage'][index] -= count
        if company not in Storage.__office_equipments['company'][index]['company']:
            Storage.__office_equipments['transfer_company'][index]['company'].append(company)
            Storage.__office_equipments['transfer_company'][index]['count'].append(0)
        company_index = Storage.__office_equipments['transfer_company'][index]['company'].index(company)
        Storage.__office_equipments['transfer_company'][index]['count'][company_index] += count

    @staticmethod
    def office_equipments():
        return Storage.__office_equipments


class OfficeEquipment(ABC):
    __MONOCHROME = 0
    __COLOR = 1
    __colors = dict(monochrome=__MONOCHROME, color=__COLOR)

    __A3 = 0
    __A4 = 1
    __A5 = 2
    __paper_sizes = dict(A3=__A3, A4=__A4, A5=__A5)

    def __init__(self, paper_size, color):
        if paper_size not in OfficeEquipment.__paper_sizes.keys() or color not in OfficeEquipment.__colors.keys():
            raise ValueError()
        self._paper_size = paper_size
        self._color = color


class Printer(OfficeEquipment):
    __LASER = 0
    __INKJET = 1
    __types = dict(laser=__LASER, inkjet=__INKJET)

    def __init__(self, paper_size, color, type_of_printer):
        super(Printer, self).__init__(paper_size, color)
        if type_of_printer not in Printer.__types.keys():
            raise ValueError
        self.__type = Printer.__types.get(type_of_printer)


class Scanner(OfficeEquipment):
    __PROJECTION = 0
    __SHEET_FEED = 1
    __types = dict(projection=__PROJECTION, sheet_feed=__SHEET_FEED)

    def __init__(self, paper_size, color, type_of_scanner):
        super(Scanner, self).__init__(paper_size, color)
        if type_of_scanner not in Scanner.__types.keys():
            raise ValueError
        self.__type = Scanner.__types.get(type_of_scanner)


class Xerox(OfficeEquipment):
    pass


printers = [Printer('A4', 'color', 'laser'), Printer('A4', 'monochrome', 'laser'), Printer('A4', 'color', 'inkjet')]
for i in range(3):
    Storage.append_item(printers[i])
print(Storage.office_equipments())
Storage.transfer('Printer', 'Directors', 2)
print(Storage.office_equipments())
