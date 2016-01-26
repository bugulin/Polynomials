# Samotné počítání polynomů 
from .polynomial import Polynomial
from .parse import to_postfix, parse

class Calcurator:
    def compute(self, pol):
        self.stack = []
        self.variables = []
        for p in pol:
            if p.isalpha() and p not in self.variables:
                self.variables.append(p)
        
        for m in pol:
            #print(m)
            if m == "+":
                b = self.stack.pop()
                a = self.stack[-1]
                a.plus(b)
                
            elif m == "-":
                b = self.stack.pop()
                a = self.stack[-1]
                a.minus(b)
                
            elif m == "*":
                b = self.stack.pop()
                a = self.stack[-1]
                a.times(b)
                
            elif m == "/":
                b = self.stack.pop()
                a = self.stack[-1]
                a.divided_by(b)
                
            elif m == "^":
                b = self.stack.pop()
                a = self.stack[-1]
                a.to_the(b)
                
            else:
                try:
                    self.stack.append(Polynomial([[int(m)]+[0]*len(self.variables)], [[1] + [0]*len(self.variables)]))
                except ValueError:
                    a = [1] + [0]*len(self.variables)
                    a[self.variables.index(m)+1] = 1
                    self.stack.append(Polynomial([a], [[1] + [0]*len(self.variables)]))

        #for s in self.stack:
        #    print(s)
        #    s.reduce()
        return self.stack[0]

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


c = Calcurator()
def new(text):
    return c.compute(to_postfix(parse(text)))