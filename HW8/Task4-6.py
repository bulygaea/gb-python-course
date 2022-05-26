from abc import ABC, abstractmethod


class Storage:
    pass


class OfficeEquipment(ABC):
    pass


class Print(OfficeEquipment):
    pass


class Scanner(OfficeEquipment):
    pass


class Xerox(OfficeEquipment):
    pass
