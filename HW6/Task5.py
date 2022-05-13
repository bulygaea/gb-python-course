class Stationery:
    def __init__(self, title):
        self.__title = title

    def draw(self):
        print('Запуск отрисовки!')

    @property
    def title(self):
        return self.__title


class Pen(Stationery):
    def draw(self):
        print(f'{self.title}: Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title}: Запуск отрисовки карандашом!')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title}: Запуск отрисовки маркером!')


stationery = Stationery('Stationery')
pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
