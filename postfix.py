def to_postfix(text):
    output = []
    operators = []
    for t in parse(text):
        if t in ("+", "-"):
            if len(operators):
                for i in range(len(operators))[::-1]:
                    if operators[i] != "(":
                        output += operators[i]
                        del operators[i]
                    else:
                        break
                        
            operators.append(t)
            #print("+ -", t)
        elif t in ["*", "/"]:
            if len(operators):
                for i in range(len(operators))[::-1]:
                    if operators[i] in ["*", "/", "^"]:
                        output += operators[i]
                        del operators[i]
                    else:
                        break
            operators.append(t)
        elif t == ")":
            while operators[-1] != "(":
                output.append(operators[-1])
                del operators[-1]
            del operators[-1]
        elif t == "(":
            operators.append("(")
        elif t == "^":
            if len(operators):
                if operators[-1] in ["^"]:
                    output += operators[-1]
                    operators[-1] = t
                else:
                    operators.append(t)
            else:
                operators.append("^")
        else:
            output.append(t)
    if len(operators):
        return " ".join(output) + " " + " ".join(operators[::-1])
    else:
        return " ".join(output)

def parse(text):
    result = []
    t = ""
    for i in text.replace(" ", ""):
        if i in ["+", "-", "*", "/", "(", ")", "^"]:
            if t != "":
                result.append(t)
                result.append(i)
                t = ""
            else:
                t += i
        elif i == "x":
            if len(t):
                result.append(t)
                t = ""
                result.append("*")
            result.append(i)
        else:
            t += i
    if t != "":
        result.append(t)
    return result

assert to_postfix("5 + 1") == "5 1 +", "6"
assert to_postfix("2 * 6 + ( 5 - 2 )") == "2 6 * 5 2 - +", "second one"
assert to_postfix("15 - ( 2 + 9 * 2 ) * 11 - ( 15 + 3 ) / 3") == "15 2 9 2 * + 11 * - 15 3 + 3 / -", "15 2 9 2 * ..."
assert to_postfix("1 + 20 - ( 2 - 5 + 5 )") == "1 20 + 2 5 - 5 + -", "Ach! Jak já ty závorky nenávidím!"
assert to_postfix("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3") == "3 4 2 * 1 5 - 2 ^ 3 ^ / +", "Ty mocniny!"
