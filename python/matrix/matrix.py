class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(n) for n in l.split()] for l in matrix_string.splitlines()]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [r[index - 1] for r in self.matrix]
