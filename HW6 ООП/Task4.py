"""4. Реализуйте базовый класс Car. у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (
куда); опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar; добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля; для классов TownCar и WorkCar переопределите метод
show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат. """


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.__speed = speed
        self.__color = color
        self.__name = name
        self.__is_police = is_police

    def go(self):
        print(f'{self.__name}\'s going!')

    def stop(self):
        print(f'{self.__name}\'s stopped!')

    def turn(self, direction):
        print(f'{self.__name} turns {direction}')

    def show_speed(self):
        return f'{self.__name} speed: {self.__speed}'

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def name(self):
        return self.__name

    def is_police(self):
        return self.__is_police


class TownCar(Car):
    def show_speed(self):
        return Car.show_speed(self) if self.speed <= 60 else f'{self.name} has exceeded the speed limit!'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        return Car.show_speed(self) if self.speed <= 40 else f'{self.name} has exceeded the speed limit!'


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


town_car = TownCar(10, 'black', 'Wolkswagen Polo')
sport_car = SportCar(110, 'red', 'Aston Martin')
work_car = WorkCar(10, 'white', 'Lada Granta')
police_car = PoliceCar(40, 'white', 'Skoda Octavia')
work_car.go()
work_car.turn('left')
print(town_car.show_speed(), sport_car.show_speed(), work_car.show_speed(), police_car.show_speed(), sep='\n')
town_car.speed = 90
work_car.speed = 60
print(town_car.show_speed(), work_car.show_speed(), sep='\n')
