#!/usr/bin/python3
from parse import to_postfix, parse
from polynomials import Polynomial

p = Polynomial()
def pol(t):
    return p.compute(to_postfix(parse(t)))


# parse
print('PARSE')

assert parse('2') == ['2'], 'Jedno číslo'
assert parse('50 * 2') == ['50', '*', '2'], 'Násobení'
assert parse('(x+2)(3x+2) + 20') == ['(', 'x', '+', '2', ')', '*', '(', '3', '*', 'x', '+', '2', ')', '+', '20'], '(...)(...)'
assert parse('2 x^2') == ['2', '*', 'x', '^', '2'], 'ax^n'
assert parse('2*x+3 - 5^2') == ['2', '*', 'x', '+', '3', '-', '5', '^', '2'], 'Pokročilejší'
assert parse('2x * (5 + 10 * 2x) / 2') == ['2', '*', 'x', '*', '(', '5', '+', '10', '*', '2', '*', 'x', ')', '/', '2'], 'I dělení'
assert parse('-2 * (-5 * -5) + 2') == ['-2', '*', '(', '-5', '*', '-5', ')', '+', '2'], '0-n neboli -n'

print('→ OK')


# postfix
print('POSTFIX')

assert to_postfix(['0']) == ['0'], 'Jedno číslo'
assert to_postfix(['5', '+', '1']) == ['5', '1', '+'], 'Sčítání'
assert to_postfix(['2', '*', '6', '+', '(', '5', '-', '2', ')']) == ['2', '6', '*', '5', '2', '-', '+'], 'Násobení a závorky'
assert to_postfix(['1', '+', '20', '-', '(', '2', '-', '5', '+', '5', ')']) == ['1', '20', '+', '2', '5', '-', '5', '+', '-'], 'Ach! Jak já ty závorky nenávidím!'
assert to_postfix(['15', '-', '(', '2', '+', '9', '*', '2', ')', '*', '11', '-', '(', '15', '+', '3', ')', '/', '3']) == ['15', '2', '9', '2', '*', '+', '11', '*', '-', '15', '3', '+', '3', '/', '-'], 'Trochu složitější'
assert to_postfix(['3', '+', '4', '*', '2', '/', '(', '1', '-', '5', ')', '^', '2', '^', '3']) == ['3', '4', '2', '*', '1', '5', '-', '2', '^', '3', '^', '/', '+'], 'Ty mocniny!'

print('→ OK')


# polynomials
print('POLYNOMIALS')

assert pol('1^3') == '1', 'Bez proměnné 1'
assert pol('2*x^2 + 5x - 12') == '2x^2 + 5x - 12', 'Bez proměnné 2'
assert pol('( 5 * 10 ) / 2 + ( 11 * 2 / 10 ) - 2') == '25.2', 'Bez proměnné 3'

assert pol('3x^2 + 5x^2') == '8x^2', 'Jednoduché sčítání'
assert pol('(x + 5)') == 'x + 5', 'Celé jedna závorka'
assert pol('x ^ 5 + 2') == 'x^5 + 2', 'x^n'
assert pol('(x^3 + 2x) + (4x^2 + 5x + 3)') == 'x^3 + 4x^2 + 7x + 3', 'Závorky 1'
assert pol('(7x^3 + 5x^2 + x) + (2x^3 - 3x^2 + 9x)') == '9x^3 + 2x^2 + 10x', 'Závorky 2'
assert pol('(3x^2 + 6x) + (-2x^2 - 14x)') == 'x^2 - 8x', '... + (-n + ...'

assert pol('x * 5 + 2 * 10') == '5x + 20', 'Základní násobení'
assert pol('x^2 * x^3') == 'x^5', 'x^n * x^m'
assert pol('(3x^2 + 4x) * 5x^2') == '15x^4 + 20x^3', 'Násobení se závorkou'
assert pol('(x^3 + 2x) * (4x^2 + 7x)') == '4x^5 + 7x^4 + 8x^3 + 14x^2', '(...) * (...)'
assert pol('5 ^ 3') == '125', 'Mocniny'
assert pol('(5*2 + x^2) ^ 2') == 'x^4 + 20x^2 + 100', 'Závorka na druhou'

assert pol('(10x^2 + 5x + 20)/5') == '2x^2 + x + 4', 'Dělení 1'
assert pol('(4x^3 + 8x^2 + 7)/(2x^2)') == '2x + 4 + 3.5x^-2', 'Dělení 2'

print('→ OK')
