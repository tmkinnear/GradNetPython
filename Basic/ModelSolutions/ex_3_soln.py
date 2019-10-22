# Model solution for exercise 3 of the "Introduction to basic Python workshop"
# Copyright T.M. Kinnear & Leon Schoonderwoerd

from math import sqrt

a = 1
b = 4
c = 2

sol_plus = (-b + sqrt(b**2 - 4 * a * c)) / (2*a)
sol_minus = (-b - sqrt(b**2 - 4 * a * c)) / (2*a)

print("The equation {} x^2 + {} x + {} = 0 has two solutions:".format(a, b, c))
print("x1 = {}".format(sol_plus))
print("x2 = {}".format(sol_minus))
