from text_parsing import parser
t = parser.parse("5x + y * (a - x(5 + a) * 5a) - x^2")

from polynomials import polynomial
var = ('x', 'y', 'a')
p = polynomial.new(t, var)[0]

print(t)
print(p.to_text(var))

from equations import gaussian_elimination as gauss
gauss.eliminate([5, 5, 5], [7, 2, 8])
