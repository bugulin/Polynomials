from postfix import to_postfix, parse
from polynomials import p

pol = p.compute

def test(sample, result):
    if sample != result:
        print(result)

# parse()
test(parse("2"), ["2"])
test(parse("5
test(parse("2x^2"), ["2", "*", "x", "^", "2"])

test(pol("2*x^2 + 5x - 12"), "2x^2 + 5x - 12")
test(pol("1^3"), "1")
