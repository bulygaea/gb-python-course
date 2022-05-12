class Stationery:
    def __init__(self, title):
        self.__title = title

    def draw(self):
        print('Запуск отрисовки!')

    def get_title(self):
        return self.__title


class Pen(Stationery):
    def draw(self):
        print(f'{self.get_title()}: Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.get_title()}: Запуск отрисовки карандашом!')


class Handle(Stationery):
    def draw(self):
        print(f'{self.get_title()}: Запуск отрисовки маркером!')


stationery = Stationery('Stationery')
pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
