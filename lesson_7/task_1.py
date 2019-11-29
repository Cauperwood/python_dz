class Matrix_1:
    def __init__(self, param):
        self.param = param
    def __str__(self):
        return str(self.param)
            #map(str,'\n'.join(self.param))

    def __add__(self, other):
        c = []
        for i in range(self.param):
            for j in range(len(self.param[i])):
                c.append(int(self.param[i][j])+int(other.param[i][j]))
        return str(c)


# class Matrix_2:
#     def __init__(self,*args):
#         self.matrix = []
#     def __add__(self, other):
#         for i in range(len(Matrix_1(self.param_1))):
#             for j in range(len(Matrix_1(self.param_1[i]))):
#                 Matrix_1(self.param_1).append(Matrix_1(self.param_1[i][j]), end=' ')
    # def __add__(self, other):
    #     for i in range(len(self.param_1)):
    #         for j in range(len(self.param_1[i])):
    #             other.res[i][j] = self.param_1[i][j] + other.param_1[i][j]
    #     print()
        #return other.res[i][j]
        # return [self.param_1[i][j]+other.param_1[i][j] for i in self.param_1 for j in self.param_1]




a = Matrix_1([[38, 28, 5], [38, 48, 6], [58, 88, 7]])
b = Matrix_1([[35, 25, 5], [35, 45, 6], [55, 85, 7]])
new_matrix = a + b
print(a)
print(b)
print(new_matrix)



