# Samotné počítání polynomů
from .polynomial import Polynomial
from .parse import to_postfix, parse

class Calcurator:
    def compute(self, pol, variables):
        print(pol)
        self.stack = []
        self.variables = variables

        for m in pol:
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

        return self.stack[0]

c = Calcurator()
def new(text, variables):
    print(parse(text))
    return c.compute(to_postfix(parse(text)), variables)
