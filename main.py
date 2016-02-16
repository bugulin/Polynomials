import polynomial

def parse(text):
    text = text.split("=")
    text = [polynomial.new(text[0]), polynomial.new(text[1])]
    return text

rovnice = []
text = " "
while text != "":
    text = input()
    if "=" in text:
        rovnice.append(text)

vars = []
t = "".join(rovnice)
for i in t:
    if i.isalpha() and i not in vars:
        vars.append(i)

print(vars)