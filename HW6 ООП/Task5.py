"""5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра. """


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
