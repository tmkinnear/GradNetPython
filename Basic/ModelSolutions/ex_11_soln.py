# Model solution for exercise 11 of the "Introduction to basic Python workshop"
# Copyright T.M. Kinnear & Leon Schoonderwoerd

import random
import numpy as np


N = 10000
N_in = 0
for i in range(N):
	rand_x = random.random()
	rand_y = random.random()
	if rand_x**2 + rand_y**2 <= 1:
		N_in += 1
print(4*N_in/N)
print(np.pi)