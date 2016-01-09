def to_postfix(text):
    output = []
    operators = []
    for t in text:
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
        return output + operators[::-1]
    else:
        return output

def parse(text):
    result = []
    t = ""
    for i in text.replace(" ", ""):
        if i in ["+", "-"]:
            if t != "":
                result.append(t)
                result.append(i)
                t = ""
            else:
                if not len(result) or result[-1] in ["*", "/", "(", "^"]:
                    t += i
                else:
                    result.append(i)
        elif i in ["*", "/", "(", ")", "^"]:
            if t != "":
                result.append(t)
                t = ""
            if i == "(" and len(result) and result[-1] not in ["+", "-", "*", "/", "^", "("]:
                result.append("*")
            result.append(i)
        elif i.isalpha():
            if len(t):
                result.append(t)
                t = ""
                result.append("*")
            elif len(result) and result[-1] not in ["+", "-", "*", "/", "^"]:
                result.append("*")
            result.append(i)
        else:
            t += i
    if t != "":
        result.append(t)
    return result
