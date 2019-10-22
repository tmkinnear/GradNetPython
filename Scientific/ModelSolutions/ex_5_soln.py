# Model solution for exercise 5 of the "Introduction to scientific Python workshop"
# Copyright T.M. Kinnear & Leon Schoonderwoerd

import numpy as np


def approximate_pi(N):
    N_in = 0
    xs = np.random.rand(N)
    ys = np.random.rand(N)
    N_in = sum(xs**2 + ys**2 <= 1)
    return 4*N_in/N


pi_exact = np.pi
print("Pi = {}".format(pi_exact))
print("Approximating for different numbers of trials:")
for N in [1e2, 1e3, 1e4, 1e5, 1e6, 1e7]:
    pi_approx = approximate_pi(100)
    print("N = {}, pi = {}, delta = {}".format(N, pi_approx, np.abs(pi_approx - pi_exact)))
