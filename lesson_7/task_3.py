class Cell:
    def __init__(self, number=int):
        self.number = number
    def __add__(self, other):
        return self.number + other.number
    def __sub__(self, other):
        return self.number - other.number
    def __mul__(self, other):
        return self.number * other.number
    def __truediv__(self, other):
        return self.number / other.number
    #def make_cell(self):


cell_1 = Cell(8)
cell_2 = Cell(9)

print(cell_1+cell_2)

print(cell_1-cell_2)

print(cell_1 * cell_2)

print(round(cell_1 / cell_2))





