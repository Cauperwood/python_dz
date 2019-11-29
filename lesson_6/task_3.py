
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
        super().__init__(self, wage=None, bonus=None, workers_income=None)
        s = super().income.values('wage')
        h = super().income.values('bonus')
        self.workers_income = s + h
        return print(f'total income {self.workers_income}')

worker_1 = Position()
worker_1.get_full_name('Ivan', 'Ivanov')


worker_2 = Position()
worker_2.get_total_income(20,30)