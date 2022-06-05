class ComplexNum:
    def __init__(self, real, imag):
        if not isinstance(real, float) and not isinstance(real, int) and \
                not isinstance(imag, float) and not isinstance(imag, int):
            raise ValueError()
        self.__real = real
        self.__imag = imag

    def __add__(self, other):
        if isinstance(other, ComplexNum):
            return ComplexNum(self.__real + other.__real, self.__imag + other.__imag)
        elif isinstance(other, int) or isinstance(other, float):
            return ComplexNum(self.__real + other, self.__imag)
        else:
            raise ValueError()

    def __mul__(self, other):
        if isinstance(other, ComplexNum):
            return ComplexNum(self.__real * other.__real - self.__imag * other.__imag,
                              self.__real * other.__imag + self.__imag * other.__real)
        elif isinstance(other, int) or isinstance(other, float):
            return ComplexNum(self.__real * other, self.__imag * other)
        else:
            raise ValueError()

    def __str__(self):
        return f'{self.__real} {"-" if self.__imag < 0 else "+"} {abs(self.__imag)}i'


print(ComplexNum(1, 3) + ComplexNum(4, -5))
print(ComplexNum(1, -1) * ComplexNum(3, 6))
print(ComplexNum(1, -1) * 5)
