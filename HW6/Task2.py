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
