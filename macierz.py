# Napisać klasę macierz. Jej instancjami będą... macierze m na n. Metody jakie musi implementować to:
# inicjalizacja (tworzy instancję klasy macierz) oraz reset (zeruje elementy macierzy) [0.5 p.]
# tworzenie macierzy z zerami lub jedynkowej (wszędzie zera, jedynki na diagonali) [0.5 p.]
# transponowanie macierzy [1 p.]
# dodawanie i odejmowanie macierzy (wraz ze sprawdzeniem czy operacja może zostać wykonana) [0.5 p.]
# mnożenie i dzielenie macierzy (jw.) [1 p.]
# liczenie wyznacznika macierzy (jw.) [1 p.]

# musi również zawierać dokumentację całej klasy oraz poszczególnych metod [0.5 p.]

class Matrix:
    def __init__(self, rows,columns, value = 0):
        self.rows = rows
        self.columns = columns
        self.a = []

        for row in range(0, rows):
            b = []
            for col in range(0, columns):
                b.append(value)
            self.a.append(b)
            rows -= 1

    def __str__(self):
        return str(self.a)

    def collect_values(self):
        container = []
        for x in self.a:
            for y in x:
                container.append(y)
        return container

    def deploy_values(self, container):
        self.a = []
        x = len(container)
        for row in range(0, self.rows):
            b = []
            for col in range(0, int(x / self.rows)):
                b.append(container[col])
            container = container[self.rows:]
            self.a.append(b)
        return self

    def add(self, matrix):
        if matrix.rows == self.rows and matrix.columns == self.columns:

            container1 = self.collect_values()
            container2 = matrix.collect_values()
            container3 = []

            for i in range(0, len(container1)):
                container3.append(container1[i] + container2[i])
            self.a = []
            for row in range(0, self.rows):
                b = []
                for col in range(0, int((len(container3) / self.rows))):
                    b.append(container3[col])
                self.a.append(b)
            return self
        else:
            print('Error. Matrix have different dimensions.')

    def sub(self, matrix):
        if matrix.rows == self.rows and matrix.columns == self.columns:
            container1 = self.collect_values()
            container2 = matrix.collect_values()
            container3 = []

            for i in range(0,len(container1)):
                container3.append(container1[i] - container2[i])
            self.a = []
            for row in range(0, self.rows):
                b = []
                for col in range(0, int((len(container3) / self.rows))):
                    b.append(container3[col])
                self.a.append(b)
            return self
        else:
            print('Error. Matrix have different dimensions.')

    def reset(self):
        rows = self.rows
        columns = self.columns
        self.a = []
        for row in range(0, rows):
            b = []
            for col in range(0, columns):
                b.append(0)
            self.a.append(b)
            rows -= 1
        return self

    def identity(self):
        rows = self.rows
        columns = self.columns
        if rows == columns:
            self.a = []
            i = 0
            for row in range(0, rows):
                b = []

                for col in range(0, columns):
                    if col == i:
                        b.append(1)
                    else:
                        b.append(0)
                i += 1
                self.a.append(b)
                rows -= 1
        else:
            print('Error! Matrix is not square.')

    def transpose(self):
        self.rows, self.columns = self.columns, self.rows
        container = self.collect_values()
        self.deploy_values(container)
        return self

    def mul(self, matrix):
        if self.rows == matrix.columns:
            t = matrix.transpose()

            container = []
            for row in self.a:
                for trow in t.a:
                    y = 0
                    for i in range(0,len(row)):
                        x = row[i] * trow[i]
                        y += x
                    container.append(y)
            return self.deploy_values(container)
        else:
            print('Error! Matrix dimensions dont match.')
            return self

    def determinator(self):
        det = 'Error! Cant make it for this dimension ;('
        if len(self.a) == 2:
            det = (self.a[0][0] * self.a[1][1]) - (self.a[0][1] * self.a[1][0])
        return det

    def revalue(self, *values):
        container=values
        if len(container) == self.rows * self.columns:
            self.deploy_values(container)
        else:
            print('Error! Number of the values doesnt match the matrix dimension!')
        return self

m = Matrix(3,3,1)
n = Matrix(3,3,5)

print(f'macierz m: {m}')
print(f'macierz n: {n}')

print(f'macierz po transpozie: {m.transpose()}')
m.identity()
print(f'm = m^1: {m}')

m.transpose()
print(f'm = m^t: {m}')

m.add(n)
print(f'm = m+n: {m}')

m.sub(n)
print(f'm = m+n-n {m}')

print(f'macierz n: {n}')
m.mul(n)
print(f'm*n {m}')

print(f'wyznacznik: {m.determinator()}')

m.revalue(3,3,3,4,2,6,8,4,5)
print(f'revalued: {m}')
