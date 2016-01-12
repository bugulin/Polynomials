class Matrix:
    def __init__(self):
        self.matrix = []

    def run(self):
        for i in range(len(self.matrix)-1):
            a = self.matrix[i][i]
            b = self.matrix[i+1][i]
            for n in range(4):
                self.matrix[i+1][n] *= a
            for n in range(4):
                self.matrix[i][n] *= b
            for n in range(4):
                self.matrix[i+1][n] -= self.matrix[i][n]

    def eliminate(self, i, n):
        pass
        
    def __str__(self):
        output = ""
        
        for b, i in enumerate(self.matrix):
            if b not in [0, len(self.matrix)-1]:
                output += "/"
            elif b == 0:
                output += "|"
            else:
                output += "\\"
            for m in i:
                output += (5 - len(str(m))) * " " + str(m)
            output += "  "
            if b not in [0, len(self.matrix)-1]:
                output += "\\"
            elif b == 0:
                output += "|"
            else:
                output += "/"
            output += "\n"
        return output

a = Matrix()
a.matrix.append([2, 3, 7, -5, 47])
a.matrix.append([3, 8, 1, -2, 50])
a.matrix.append([0, 3, 3, 1, 27])
a.matrix.append([0, 0, 10, 10, 31])

