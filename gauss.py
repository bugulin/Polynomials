class Matrix:
    def __init__(self):
        self.matrix = []

    def run(self):
        self.vars = len(self.matrix)
        for i in range(self.vars-1):
            a = self.matrix[i][i]
            b = self.matrix[i+1][i]
            for n in range(self.vars+1):
                self.matrix[i+1][n] *= a
            for n in range(self.vars+1):
                self.matrix[i][n] *= b
            for n in range(self.vars+1):
                self.matrix[i+1][n] -= self.matrix[i][n]

        print(self)

        result = [0]*self.vars
        for i in range(0, self.vars)[::-1]:
            a = self.matrix[i]
            print(a)
            for n in range(i+1, self.vars):
                print("-", a[n])
                a[self.vars] -= a[n]*result[n]
                a[n] = 0
            result[i] = a[self.vars]/a[i]

        #result.insert(0, (self.matrix[-2][-1] - self.matrix[-2][-2]*result[0]) / self.matrix[-2][-3])
        return result

    def eliminate(self, i, n):
        pass
        
    def __str__(self):
        output = ""
        
        for b, i in enumerate(self.matrix):
            if b not in [0, len(self.matrix)-1]:
                output += "|"
            elif b == 0:
                output += "/"
            else:
                output += "\\"
            for m in i:
                output += (5 - len(str(m))) * " " + str(m)
            output += "  "
            if b not in [0, len(self.matrix)-1]:
                output += "|"
            elif b == 0:
                output += "\\"
            else:
                output += "/"
            output += "\n"
        return output

a = Matrix()
#a.matrix.append([2, 3, 7, 47])
#a.matrix.append([3, 8, 1, 50])
#a.matrix.append([0, 3, 3, 27])

a.matrix.append([4, 1, 5])
a.matrix.append([12, 3, 15])
