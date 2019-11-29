class Clothes:
    pass


class Coat(Clothes):
    def __init__(self, size=None):
        self.size = size
    def ex_fabric_coat(self, size):
        return size/6.5 + 0.5



class Suit(Clothes):
    def __init__(self, growth=None):
        self.growth = growth
    def ex_fabric_suit(self, growth):
        return 2 * growth + 0.3

a = Coat()
print(a.ex_fabric_coat(4))
b = Suit()
print(b.ex_fabric_suit(4))

print(f'total ex_fabric = {a.ex_fabric_coat(4)+ b.ex_fabric_suit(4)}')



