# Samotné počítání polynomů
from .monomial import Monomial

def new(text, variables):
    stack = []

    for m in text:
        if m == "+":
            b = stack.pop()
            a = stack[-1]
            a.plus(b)

        elif m == "-":
            b = stack.pop()
            a = stack[-1]
            a.minus(b)

        elif m == "*":
            b = stack.pop()
            a = stack[-1]
            a.times(b)

        elif m == "/":
            b = stack.pop()
            a = stack[-1]
            a.divided_by(b)

        elif m == "^":
            b = stack.pop()
            a = stack[-1]
            a.to_the(b)

        else:
            try:
                stack.append(Monomial([[int(m)]+[0]*len(variables)], [[1] + [0]*len(variables)]))
            except ValueError:
                a = [1] + [0]*len(variables)
                a[variables.index(m)+1] = 1
                stack.append(Monomial([a], [[1] + [0]*len(variables)]))

    return stack
