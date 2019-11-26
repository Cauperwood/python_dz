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
