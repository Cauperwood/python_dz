task_1

import time

class TrafficLight:
    def __init__(self):
        __color = None

    def running(self):
        TrafficLight.color = 'Red'
        print('Red')
        time.sleep(7)
        TrafficLight.color = 'Yellow'
        print('Yellow')
        time.sleep(2)
        TrafficLight.color = 'Green'
        print('Green')
        time.sleep(3)
    # def set_color(self, value):
    #     if str(value) != "Red":
    #         self.__color = value
    #         print('First color of trafficlight is red')
    #         break
    #       else:
    #         continue



a = TrafficLight()
print(a.running())

task_2

class Road:
    def __init__(self, mass_1m=None, sm=None, lenght=None, width=None ):
        self.mass_1m = mass_1m
        self.sm = sm
        self.lenght = lenght
        self.width = width

    def mass(self, lenght, width, mass_1m, sm):
        return lenght * width * mass_1m * sm

road_mass = Road()
print(f'load of road {road_mass.mass(4, 5, 3, 2)} tons')

# task_3

class Worker:
    name = None
    surname = None
    position = None

    def __init__(self, wage=None, bonus=None):
        self.income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self, name=None, surname=None):
        self.name = name
        self.surname = surname
        return print(f' name of worker {self.name} surname - {self.surname}')


 #  четыре часа, потраченные на эту часть 3-го задания не увенчались успехом
    def get_total_income(self):
        super().__init__()
        s = super().income.values('wage')
        h = super().income.values('bonus')
        self.workers_income = s + h
        return print(f'total income {self.workers_income}')

worker_1 = Position()
worker_1.get_full_name('Ivan', 'Ivanov')


worker_2 = Position()
worker_2.get_total_income(20,30)

# task_4
#
class Car:
    def __init__(self, speed=None, color=None, name=None, is_police=bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'The car {} on road')
    def stop(self):
        print(f'The car {} stop')
    def turn(self):
        print(f'The direction of car {}')

class TownCar(Car):
class SportCar(Car):
class WorkCar(Car):
class PoliceCar(Car):








