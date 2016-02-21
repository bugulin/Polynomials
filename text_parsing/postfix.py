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
