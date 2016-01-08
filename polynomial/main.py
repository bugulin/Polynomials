from parse import parse, to_postfix

class Polynomial:
    def __init__(self, n, d=1):
        self.length = len(n[0])
        self.numerator = n
        self.denominator = d

    def invert(self):
        self.numerator, self.denominator = self.denominator, self.numerator

    def plus(self, polynomial):
        self.numerator += polynomial.numerator

    def minus(self, polynomial):
        for i in range(len(polynomial.numerator)):
            polynomial.numerator[i][0] *= -1
        self.plus(polynomial)

    def times(self, polynomial):
        result = []
        for a in self.numerator:
            for b in polynomial.numerator:
                c = [a[0]*b[0]]
                for i in range(1, self.length):
                    c.append(a[i]+b[i])
                result.append(c)
        self.numerator = result

        result = []
        for a in self.denominator:
            for b in polynomial.denominator:
                c = [a[0]*b[0]]
                for i in range(1, self.length):
                    c.append(a[i]+b[i])
                result.append(c)
        self.denominator = result

    def divided(self, polynomial):
        polynomial.invert()
        self.times(polynomial)
        
    def __str__(self):
        return str(self.numerator) + " / " + str(self.denominator)

class Calcurator:
    def compute(self, pol):
        self.stack = []
        self.variables = []
        for p in pol:
            if p.isalpha() and p not in self.variables:
                self.variables.append(p)
        
        for m in pol:
            print(m)
            if m == "+":
                b = self.stack.pop()
                a = self.stack[-1]
                a.plus(b)
                #self.stack.append(self.addition(self.stack.pop(), self.stack.pop()))
            elif m == "-":
                b = self.stack.pop()
                a = self.stack[-1]
                a.minus(b)
                #self.stack.append(self.subtraction(self.stack.pop(), self.stack.pop()))
            elif m == "*":
                b = self.stack.pop()
                a = self.stack[-1]
                a.times(b)
                #self.stack.append(self.multiplication(self.stack.pop(), self.stack.pop()))
            elif m == "/":
                b = self.stack.pop()
                a = self.stack[-1]
                a.divided(b)
                #self.stack.append(self.division(self.stack.pop(), self.stack.pop()))
            elif m == "^":
                pass
                #self.stack.append(self.exponent(self.stack.pop(), self.stack.pop()))
            else:
                try:
                    self.stack.append(Polynomial([[int(m)]+[0]*len(self.variables)], [[1] + [0]*len(self.variables)]))
                except ValueError:
                    a = [1] + [0]*len(self.variables)
                    a[self.variables.index(m)+1] = 1
                    self.stack.append(Polynomial([a], [[1] + [0]*len(self.variables)]))

            #print(self.stack)
        for s in self.stack:
            print(s)
        #return self.stack

    def print(self, polynomial):
        sign = ""
        output = ""
        m = -1 * min([i[1] for i in polynomial])
        l = m + max([i[1] for i in polynomial])
        
        p = [0] * (l+1)
        for x, n in polynomial:
            p[n+m] += x
        for i in range(l+1)[::-1]:
            x = p[i]
            if x == int(x):
                x = int(x)
            if x == 0:
                continue
            elif x < 0:
                sign = "- "
                x *= -1
            else:
                sign = "+ "
            if x == 1 and i-m != 0:
                x = ""
            
            if i-m == 0:
                output += sign + str(x)
            elif i-m == 1:
                output += sign + str(x) + self.variable
            else:
                output += sign + str(x) + self.variable+"^" + str(i-m)
            output += " "
        if output[0] == "+":
            output = output[2:]
        return output[:-1]

    def reduce(self, polynomial):
        m = -1 * min([i[1] for i in polynomial])
        l = m + max([i[1] for i in polynomial])
        powers = [0] * (l+1)
        for x, n in polynomial:
            powers[n+m] += x

        output = []
        for n in range(len(powers))[::-1]:
            x = powers[n]
            if x != 0:
                output.append((x, n-m))
        return output
    
    def addition(self, b, a):
        return self.reduce(a + b)
    def subtraction(self, b, a):
        return self.reduce(a + [(-1 * n[0], n[1]) for n in b])
    def multiplication(self, b, a):
        result = []
        for n1 in a:
            for n2 in b:
                result.append((n1[0]*n2[0], n1[1]+n2[1]))
        return self.reduce(result)
    def division(self, b, a):
        # nefunguje
        result = []
        for n1 in a:
            for n2 in b:
                result.append((n1[0]/n2[0], n1[1]-n2[1]))
        return result
    def exponent(self, b, a):
        if len(a) == 1 and b[0][1] == 0 and a[0][1] == 1:
            return [(a[0][0], a[0][1]-1+b[0][0])]
        elif b[0][1] == 0: # (a+b+c)^n
            result = a[:]
            for i in range(b[0][0]-1):
                result = self.multiplication(a, result)
                #print("-", result)
            return self.reduce(result)
        else:
            print("^ ( ... )")
            raise SyntaxError("To ještě neumím!")

c = Calcurator()
def new(text):
    return c.compute(to_postfix(parse(text)))
