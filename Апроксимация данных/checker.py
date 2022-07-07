from math import sqrt

from sympy import symbols

a, x = symbols('a x')
f = a**3*x + 3*a**2*x**2/2 + a*x**3 + x**4/4

print(f.subs(a,1))