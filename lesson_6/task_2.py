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
print(f'load of road {road_mass.mass(4, 5, 3, 2)}')