"""2. Реализовать класс Road (дорога). определить атрибуты: length (длина), width (ширина); значения атрибутов должны
передаваться при создании экземпляра класса; атрибуты сделать защищёнными; определить метод расчёта массы асфальта,
необходимого для покрытия всей дороги; использовать формулу: длина*ширина*масса асфальта для покрытия одного кв.
метра дороги асфальтом, толщиной в 1 см*число см толщины полотна; проверить работу метода. Например: 20 м*5000 м*25
кг*5 см = 12500 т. """


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation_of_mass(self, asphalt_mass, asphalt_thickness):
        return self._length * self._width * asphalt_mass * asphalt_thickness / 1000


new_road = Road(int(input("Type the road length (m): ")),
                int(input("Type the road width (m): ")))
print(new_road.calculation_of_mass(int(input("Type the asphalt mass (kg): ")),
                                   int(input("Type the asphalt thickness (sm): "))), 't')
