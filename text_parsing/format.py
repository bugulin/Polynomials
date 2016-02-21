def form(text):
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
            elif len(result) and result[-1] not in ["+", "-", "*", "/", "^", "("]:
                result.append("*")
            result.append(i)
        else:
            t += i
    if t != "":
        result.append(t)
    return result
