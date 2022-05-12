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

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def is_police(self):
        return self.__is_police


class TownCar(Car):
    def show_speed(self):
        return Car.show_speed(self) if self.get_speed() <= 60 else f'{self.get_name()} has exceeded the speed limit!'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        return Car.show_speed(self) if self.get_speed() <= 40 else f'{self.get_name()} has exceeded the speed limit!'


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super(PoliceCar, self).__init__(speed, color, name, True)


town_car = TownCar(10, 'black', 'Wolkswagen Polo')
sport_car = SportCar(110, 'red', 'Aston Martin')
work_car = WorkCar(10, 'white', 'Lada Granta')
police_car = PoliceCar(40, 'white', 'Skoda Octavia')
work_car.go()
work_car.turn('left')
print(town_car.show_speed(), sport_car.show_speed(), work_car.show_speed(), police_car.show_speed(), sep='\n')
town_car.set_speed(90)
work_car.set_speed(60)
print(town_car.show_speed(), work_car.show_speed(), sep='\n')
