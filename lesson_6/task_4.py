class Car:
    def __init__(self, speed, color, name, is_police=bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        if int(self.speed) > 0:
            return 'go'
    def stop(self):
        if self.speed == 0:
            return 'stop'
    def turn(self, direction):
        return direction
    def show_speed(self):
        return self.speed


class TownCar(Car):
    def go(self, speed):
        self.speed = speed
        if speed > 60:
            return 'you drive too fast'


class SportCar(Car):
    pass


class WorkCar(Car):
    def go(self, speed = None):
        self.speed = speed
        if int(speed) > 40:
            return 'you drive too fast'


class PoliceCar(Car):
    pass

prius = TownCar(80, 'grey', 'toyota', False)
print(prius.go(80))
print(prius.turn('right'))
print(prius.stop())
print(prius.show_speed())

lamba = SportCar(280, 'orange', 'lamba', False)
print(lamba.go())
print(lamba.turn('left'))
print(lamba.stop())
print(lamba.show_speed())


kamaz = WorkCar(280, 'dirty', 'master', False)
print(kamaz.go(30))
print(kamaz.turn('to direct'))
print(kamaz.stop())
print(kamaz.show_speed())


lada = PoliceCar(0, 'blue', 'lada', True)
print(lada.go())
print(lada.turn('to behind'))
print(lada.stop())
print(lada.show_speed())




