class Matrix:
    def __init__(self):
        self.matrix = []

    def run(self, *matrix):
        self.matrix = matrix
        self.vars = len(matrix[0]-1)
        self.sort()
        
        for y in range(self.vars-1):
            for i in range(self.vars-1-y):
                if self.matrix[i][y]:
                    b = self.matrix[i+1].copy()
                    bi, ai = self.n(self.matrix[i][y], b[y])
                    
                    for n in range(self.vars+1):
                        b[n] *= ai
                    for n in range(self.vars+1):
                        self.matrix[i][n] *= bi
                    for n in range(self.vars+1):
                        self.matrix[i][n] -= b[n]
        print(self)

        if self.matrix.count([0]*(self.vars+1)):
            print("...")

        result = [0]*self.vars
        c = self.vars-1
        for i in range(0, self.vars):
            a = self.matrix[i]
            #print(a)
            for n in range(self.vars-i, self.vars):
                #print("-", a[n])
                a[self.vars] -= a[n]*result[c-n]
                a[n] = 0
            result[i] = a[self.vars]/a[c-i]
        print(self)

        output = []
        chars = "xyzabcdefghijklmno"
        for i in range(self.vars):
            r = result[i]
            if r == int(r):
                r = int(r)
            output.append(chars[i] + " = " + str(r))
        print(", ".join(output))
        return result[::-1]

    def n(self, a, b):
        abs_a = abs(a)
        abs_b = abs(b)
        multiple_of_a = abs(a)
        multiple_of_b = abs(b)
        while multiple_of_a != multiple_of_b:
            if multiple_of_a > multiple_of_b:
                multiple_of_b += abs_b
            elif multiple_of_b > multiple_of_a:
                multiple_of_a += abs_a
        return multiple_of_a/a, multiple_of_b/b

    def sort(self):
        new_m = [tuple(map(lambda x: abs(x), m)) + (i,) for i, m in enumerate(self.matrix)]
        new_m.sort()
        result = []
        for m in new_m:
            result.append(self.matrix[m[-1]])
        self.matrix = result
        print(self)
        
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
# x = 4, y = 5, z = 2
"""a.run([2, 3, 7, 47],
      [3, 8, 1, 50],
      [0, 3, 3, 27])"""

a.run([4, 1, 5],
      [12, 3, 15])
