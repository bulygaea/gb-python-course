"""1. Создать класс TrafficLight (светофор). определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный; в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный; продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение; переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный); проверить работу примера, создав экземпляр и вызвав описанный метод. Задачу можно
усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать
скрипт. """

import time

import pygame


class TrafficLight:
    __RED = (255, 0, 0)
    __YELLOW = (255, 255, 0)
    __GREEN = (0, 255, 0)
    __COLORS = [__RED, __YELLOW, __GREEN, __YELLOW]
    __TIME_TO_COLOR = [7, 2, 10, 2]

    def __init__(self, surface):
        self.__color = TrafficLight.__RED
        self.__i = 0
        self.__time_to_start_color = time.time()
        self.__surface = surface

    def running(self):
        if time.time() - self.__time_to_start_color >= TrafficLight.__TIME_TO_COLOR[self.__i]:
            self.__color = TrafficLight.__COLORS[self.__i + 1 if self.__i < 3 else 0]
            self.__time_to_start_color = time.time()
            self.__i = self.__i + 1 if self.__i < 3 else 0
        pygame.draw.circle(self.__surface, self.__color, (150, 90), 50)


WIDTH = 300
HEIGHT = 180
FPS = 30
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
traffic_light = TrafficLight(screen)

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    traffic_light.running()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
