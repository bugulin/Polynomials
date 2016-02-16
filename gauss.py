class Matrix:
    def __init__(self):
        self.matrix = []

    def run(self, *matrix):
        self.matrix = matrix
        self.vars = len(matrix[0])-1

        self.reduce()
        print(self)
        print("=======")

        self.sort()
        
        for y in range(len(self.matrix)-1):
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

                    if self.matrix[i] == [0]*(self.vars+1):
                        del self.matrix[i]
        print(self)

        while self.matrix.count([0]*(self.vars+1)):
            print("...")
            self.matrix.remove([0]*(self.vars+1))
        if len(self.matrix) < self.vars:
            print("Žádné řešení!")
            return 0
        
        if len(self.matrix) < self.vars:
            print("Žádné řešení!")
            return 0

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

    def reduce(self):
        new_matrix = []
        for e in range(len(self.matrix)):
            divisors = [{1} for i in range(self.vars+1)]
            for i, n in enumerate(self.matrix[e]):
                for d in range(2, n+1):
                    if n%d == 0:
                        divisors[i].add(d)
            hds = divisors[0].copy()
            for i in divisors[1:]:
                hds = hds.intersection(i)
            hd = max(hds)
            if hd != 1:
                new = []
                for i in range(self.vars+1):
                    new.append(self.matrix[e][i] / hd)
                if not new_matrix.count(new):
                    new_matrix.append(new)
        self.matrix = new_matrix

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

#a.matrix.append([8, 80, 7, 155])
#a.matrix.append([10, 30, 5, 30])
#a.matrix.append([31, 11, 5, 0])
a.run([4, 1, 5],
      [12, 3, 15],
      [1, 4, 10],
      [2, 8, 20])
