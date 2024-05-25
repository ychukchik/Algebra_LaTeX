from sympy import groebner
from sympy.abc import x, y, z

polynomials = [x*y - x, x**2 - y, y**2 - y]                     # yes
# polynomials = [y - x**2, z - x**3]                            # no
# polynomials = [x*(y**2) - x*z + y, x*y - z**2, x - y*(z**4)]  # no
print(polynomials)

G = groebner(polynomials, order='lex')
print(G)

G_polynomials = list(G.args[0])

polynomials = set(polynomials)
G_polynomials = set(G_polynomials)

if (G_polynomials==polynomials): print("Заданное множество ЯВЛЯЕТСЯ базисом Гребнера при лексикографическом упорядочении")
else: print("Заданное множество НЕ ЯВЛЯЕТСЯ базисом Гребнера при лексикографическом упорядочении")