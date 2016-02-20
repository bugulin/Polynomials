import polynomial.main as polynomial

class Console:
    def compute(self, *text):
        text = list(text)
        # Zjištění proměnných
        self.find_variables(text)
        print("Máme tu proměnné: %s." % ", ".join(self.vars))

        if len(text) > 1:
            # Rovnice
            rovnice = [self.parse_equation(eq) for eq in text]
            result = rovnice

            #for r in rovnice:
            #    print(self.print_polynomial(r[0]), "=", self.print_polynomial(r[1]))
        else:
            # Polynom
            result = [polynomial.new(text[0], self.vars)]
            #print(self.print_polynomial(result))

        return result, self.vars

    def parse_equation(self, equation):
        eq = equation.split("=")
        eq = [polynomial.new(eq[0], self.vars), polynomial.new(eq[1], self.vars)]
        return eq

    def find_variables(self, text):
        self.vars = []
        for t in "".join(text):
            if t.isalpha() and t not in self.vars:
                self.vars.append(t)

def pprint(p, v):
    if len(p) > 1:
        output = ""
        for m in p:
            output += print_polynomial(m, v)
            output += " + "
            output += print_polynomial(m, v)
    else:
        output = print_polynomial(p[0], v)

    return output

def print_polynomial(polynomial, variables):
    sign = ""
    output = ""

    if polynomial.denominator == [ [1] + [0]*len(variables) ]:
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
                        output += "%s" % ( variables[i] )
                    else:
                        output += "(%s^%d)" % ( variables[i], x )
            output += " "

    if output[0] == "+":
        output = output[2:]
    return output[:-1]
