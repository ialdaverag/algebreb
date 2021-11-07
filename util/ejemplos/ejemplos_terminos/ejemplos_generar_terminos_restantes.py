from sympy.abc import a, b, c,x, y, z
from algebreb.util.terminos import generar_terminos_restantes

terms1 = generar_terminos_restantes([x, y], 2)
print(terms1)

terms2 = generar_terminos_restantes([x, y], 1)
print(terms2)

terms3 = generar_terminos_restantes([x, y], 3)
print(terms3)

terms4 = generar_terminos_restantes([x, y, z], 2)
print(terms4)

terms5 = generar_terminos_restantes([a, b, c, x, y, z], 2)
print(terms5)

terms6 = generar_terminos_restantes([a], 2)
print(terms6)

terms7 = generar_terminos_restantes([b, c], 7)
print(terms7)