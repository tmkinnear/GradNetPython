# Model solution for exercise 9 of the "Introduction to basic Python workshop"
# Copyright T.M. Kinnear & Leon Schoonderwoerd

from math import sqrt

a = 2
b = 3
for c in [-15, -10, 0, 5, 10, 15]:
	# the try: ; except: structur (untreated in the workshop) is to have this
	# script not fail when math.sqrt() encounters a negative argument.
	try:
		sol_plus = (-b + sqrt(b**2 - 4 * a * c)) / (2*a)
		sol_minus = (-b - sqrt(b**2 - 4 * a * c)) / (2*a)

		print("The equation {} x^2 + {} x + {} = 0 has two solutions:".format(a, b, c))
		print("x1 = {}".format(sol_plus))
		print("x2 = {}".format(sol_minus))
	except ValueError:
		print("No (real) solutions for a = {}, b = {}, c = {}".format(a, b, c))


# Alternative, allowing negative square roots using sqrt(x) = x^(1/2):
a = 2
b = 3
for c in [-15, -10, 0, 5, 10, 15]:
	sol_plus = (-b + (b**2 - 4 * a * c) ** (1/2)) / (2*a)
	sol_minus = (-b - (b**2 - 4 * a * c) ** (1/2)) / (2*a)

	print("The equation {} x^2 + {} x + {} = 0 has two solutions:".format(a, b, c))
	print("x1 = {}".format(sol_plus))
	print("x2 = {}".format(sol_minus))
