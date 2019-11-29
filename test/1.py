# class Matrix:
#     def __init__(self, a):
#         List = []
#         for i in a:
#             List.append([j for j in i])
#         self.a = List
#
#     def __str__(self):
#         self.b = '\n'.join(['\t'.join([str(j) for j in i]) for i in self.a])
#         # self.c = str(self.a)
#         return self.b

    # def __add__(self, other):
    #     result = []
    #     numbers = []
    #     for i in range(len(self.a)):
    #         for j in range(len(self.a[0])):
    #             summa = other.a[i][j] + self.a[i][j]
    #             numbers.append(summa)
    #             if len(numbers) == len(self.a):
    #                 result.append(numbers)
    #                 numbers = []
    #     return Matrix(result)
#
#
# m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# # m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
# print(m1)
# print(m1 + m2)
# print(m1 + m2)

class Matrix:
    def __init__(self, a):
        self.b = '\n'.join(['\t'.join([str(j) for j in i]) for i in a])
        List = []
        for i in a:
            List.append([j for j in i])
        self.a = List

    def __str__(self):
        self.c = str(self.a)
        return self.c

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.a)):
            for j in range(len(self.a[0])):
                summa = other.a[i][j] + self.a[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.a):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


# class Matrix:
#     def __init__(self, a):
#         self.b = '\n'.join(['\t'.join([str(j) for j in i]) for i in a])
#         List = []
#         for i in a:
#             List.append([j for j in i])
#         self.a = List
#
#     def __str__(self):
#         self.c = str(self.b)
#         return self.c
#
#     def __add__(self, other):
#         NumStr = len(self.a)
#         NumCol = len(other.a[0])
#         for i in range(NumStr):
#             for j in range(NumCol):
#                 self.a[i][j] = self.a[i][j] + other.a[i][j]
#             Result = self.a
#         return Matrix(Result)
#         seek(0)


m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)
print(m1 + m2)
print(m1 + m2)