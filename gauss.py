class Matrix:
    def __init__(self):
        self.matrix = []

    def run(self):
        self.vars = len(self.matrix)
        self.matrix = sorted(self.matrix)
        
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
            #print(self)

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

        chars = "xyzabcdefghijklmno"
        for i in range(self.vars):
            print(chars[i], "=", result[i], end=", ")
        print()
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
a.matrix.append([2, 3, 7, 47])
a.matrix.append([3, 8, 1, 50])
a.matrix.append([0, 3, 3, 27])

#a.matrix.append([8, 80, 7, 155])
#a.matrix.append([10, 30, 5, 30])
#a.matrix.append([31, 11, 5, 0])
