import Polynomials

def parse(text):
    text = text.split("=")
    return text

rovnice = []
text = " "
while text != "":
    text = input()
    if "=" in text:
        rovnice.append(parse(text))
