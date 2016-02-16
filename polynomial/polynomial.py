# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 12:38:22 2016

@author: bugulin
"""

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

    def divided_by(self, polynomial):
        polynomial.invert()
        self.times(polynomial)

    def to_the(self, polynomial):
        if len(polynomial.numerator) == 1:
            if sum(polynomial.numerator[0][1:]) == 0:
                if polynomial.numerator[0][0] == 0:
                    self.numerator = [[0] + [0]*self.length-1]
                else:
                    for i in range(polynomial.numerator[0][0]-1):
                        self.times(self)
        else:
            print("It's very hard!")

    def reduce(self):
        numerator = {}
        for m in self.numerator:
            try:
                numerator[tuple(m[1:])] += m[0]
            except KeyError:
                numerator[tuple(m[1:])] = m[0]

        denominator = {}
        for m in self.denominator:
            try:
                denominator[tuple(m[1:])] += m[0]
            except KeyError:
                denominator[tuple(m[1:])] = m[0]

        # ...
        print(numerator, denominator)
        
    def __str__(self):
        return str(self.numerator) + " / " + str(self.denominator)