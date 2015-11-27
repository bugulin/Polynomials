from postfix import to_postfix

class Polynomial:
    def compute(self, text):
        self.stack = []
        text = to_postfix(text)
        text = text.split(" ")
        for t in text:
            if t == "+":
                self.stack.append(self.addition(self.stack.pop(), self.stack.pop()))
            elif t == "-":
                self.stack.append(self.subtraction())
            elif t == "*":
                self.stack.append(self.multiplication())
            elif t == "/":
                self.stack.append(self.division())
            elif t == "^":
                self.stack.append(self.exponent())
            else:
                if "x" not in t:
                    self.stack.append([(int(t), 0)])
                else:
                    self.stack.append([(int(t[:-1] or "1"), 1)])
        return self.print(self.stack[0])

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
                output += sign + str(x) + "x"
            else:
                output += sign + str(x) + "x^" + str(i-m)
            output += " "
        if output[0] == "+":
            output = output[2:]
        return output[:-1]

    def reduce(self, polynomial):
        #print(" + ", polynomial)
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
    def subtraction(self):
        b = self.stack.pop()
        a = self.stack.pop()
        return self.reduce(a + [(-1 * n[0], n[1]) for n in b])
    def multiplication(self):
        b = self.stack.pop()
        a = self.stack.pop()
        result = []
        for n1 in a:
            for n2 in b:
                result.append((n1[0]*n2[0], n1[1]+n2[1]))
        return result
    def division(self):
        # nefunguje
        b = self.stack.pop()
        a = self.stack.pop()
        result = []
        for n1 in a:
            for n2 in b:
                result.append((n1[0]/n2[0], n1[1]-n2[1]))
        return result
    def exponent(self):
        b = self.stack.pop()
        a = self.stack.pop()
        if b[0][1] == 0 and a[0][1] == 1:
            return [(a[0][0], a[0][1]-1+b[0][0])]
        elif b[0][1] == 0: # (a+b+c)^n
            result = a[:]
            for i in range(b[0][0]-1):
                self.stack.append(result)
                self.stack.append(a)
                self.stack.append(self.multiplication())
                result = self.stack.pop()
                #print("-", result)
            return result
        else:
            print("^ ( ... )")
            raise SyntaxError("To ještě neumím!")
            
p = Polynomial()


