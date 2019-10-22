# Model solution for exercise 14 of the "Introduction to basic Python workshop"
# Copyright T.M. Kinnear & Leon Schoonderwoerd

import math

def quadratic_solver(a, b, c):  # without user input
	print("Solving the quadratic equation {}x^2 + {}x + {} = 0".format(a, b, c))
	solution_plus = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
	solution_minus = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
	print("x = {:.5f} or x = {:.5f}".format(solution_plus, solution_minus))


def user_quadratic_solver():  # with user input
	a, b, c = input("Please input a, b and c, separated by spaces: ").split()
	a = int(a)
	b = int(b)
	c = int(c)
	print("Solving the quadratic equation {}x^2 + {}x + {} = 0".format(a, b, c))
	solution_plus = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
	solution_minus = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
	print("x = {:.5f} or x = {:.5f}".format(solution_plus, solution_minus))


# Let's test:
quadratic_solver(2, 3, -10)
user_quadratic_solver()