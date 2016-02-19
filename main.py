import polynomial.main as polynomial

class Console:
    def compute(self, text):
        # Zjištění proměnných
        self.find_variables(text)
        print("Máme tu proměnné: %s." % ", ".join(self.vars))

        if type(text) == list:
            # Rovnice
            rovnice = [self.parse_equation(eq) for eq in text]
            result = rovnice

            for r in rovnice:
                print(self.print_polynomial(r[0]), "=", self.print_polynomial(r[1]))
        else:
            # Polynom
            result = polynomial.new(text, self.vars)
            print(self.print_polynomial(result))

        return result

    def parse_equation(self, equation):
        eq = equation.split("=")
        eq = [polynomial.new(eq[0], self.vars), polynomial.new(eq[1], self.vars)]
        return eq

    def find_variables(self, text):
        self.vars = []
        for t in "".join(text):
            if t.isalpha() and t not in self.vars:
                self.vars.append(t)

    def print_polynomial(self, polynomial):
        sign = ""
        output = ""

        if polynomial.denominator == [ [1] + [0]*len(self.vars) ]:
            for m in polynomial.numerator:
                n = m[0]
                if n >= 0:
                    output += "+ "
                else:
                    output += "- "
                    m[0] = abs(m[0])
                output += str(m[0])

                for i, x in enumerate(m[1:]):
                    if x != 0:
                        if x == 1:
                            output += "%s" % ( self.vars[i] )
                        else:
                            output += "(%s^%d)" % ( self.vars[i], x )
                output += " "

        if output[0] == "+":
            output = output[2:]
        return output[:-1]

c = Console()
print()
c.compute("5x + y * (x + 12 - x * (y + 5 - 5y))")
print()
