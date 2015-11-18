from postfix import to_postfix, parse
from polynomials import p

pol = p.compute

def test(sample, result):
    if sample != result:
        print(result)

# parse
test(parse("2"), ["2"])
test(parse("50 * 2"), ["50", "*", "2"])
test(parse("2 x^2"), ["2", "*", "x", "^", "2"])
test(parse("2*x+3 - 5^2"), ['2', '*', 'x', '+', '3', '-', '5', '^', '2'])
test(parse("2x * (5 + 10 * 2x) / 2"), ['2', '*', 'x', '*', '(', '5', '+', '10', '*', '2', '*', 'x', ')', '/', '2']) 
assert parse('-2 * (-5 * -5) + 2') == ['-2', '*', '(', '-5', '*', '-5', ')', '+', '2'], 'Parse: -'

test(pol("1^3"), "1")
test(pol("2*x^2 + 5x - 12"), "2x^2 + 5x - 12")

assert to_postfix("5 + 1") == "5 1 +", "6"
assert to_postfix("2 * 6 + ( 5 - 2 )") == "2 6 * 5 2 - +", "second one"
assert to_postfix("15 - ( 2 + 9 * 2 ) * 11 - ( 15 + 3 ) / 3") == "15 2 9 2 * + 11 * - 15 3 + 3 / -", "15 2 9 2 * ..."
assert to_postfix("1 + 20 - ( 2 - 5 + 5 )") == "1 20 + 2 5 - 5 + -", "Ach! Jak já ty závorky nenávidím!"
assert to_postfix("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3") == "3 4 2 * 1 5 - 2 ^ 3 ^ / +", "Ty mocniny!"

assert p.compute("( 5 * 10 ) / 2 + ( 11 * 2 / 10 ) - 2") == "25.2", "Without X"

# polynomials + -
assert pol('(x^3 + 2x) + (4x^2 + 5x + 3)') == 'x^3 + 4x^2 + 7x + 3', 'Test n. 4'
test(pol("(7x^3 + 5x^2 + x) + (2x^3 - 3x^2 + 9x)"), "9x^3 + 2x^2 + 10x")
assert p.compute("x ^ 5 + 2") == "x^5 + 2", "First one!"

