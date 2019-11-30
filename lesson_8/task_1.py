class Data:
    data = '11.11.2010'

    def __init__(self, data):
        self.data = data

    @classmethod
    def data_i(cls):
        res = map(int, cls.data.split('.'))
        return tuple(res)

    @staticmethod
    def data_val(data):
        return [True if 1 <= data[0] <= 31 and 1 <= data[1] <= 12 else False]


a = Data('11.11.2019')
print(Data.data_val('11.11.2019'))
print(a)