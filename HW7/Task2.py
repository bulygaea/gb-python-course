from abc import ABC, abstractmethod


class Clothes(ABC):
    _total_fabric_consumption = 0

    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def fabric_consumption(self):
        raise NotImplementedError(self.__class__.__name__)

    @staticmethod
    def total_fabric_consumption():
        return Clothes._total_fabric_consumption


class Coat(Clothes):

    def __init__(self, name, v):
        super(Coat, self).__init__(name)
        self.__v = v

    @property
    def v(self):
        return self.__v

    def fabric_consumption(self):
        Clothes._total_fabric_consumption += self.v / 6.5 + 0.5
        return self.v / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, name, h):
        super(Suit, self).__init__(name)
        self.__h = h

    @property
    def h(self):
        return self.__h

    def fabric_consumption(self):
        Clothes._total_fabric_consumption += 2 * self.h + 0.3
        return 2 * self.h + 0.3


suit = Suit('suit', 140)
coat = Coat('coat', 38)
print(suit.fabric_consumption())
print(coat.fabric_consumption())
print(Clothes.total_fabric_consumption())
