# Model solution for exercise 7 of the "Introduction to basic Python workshop"
# Copyright Tim Kinnear & Leon Schoonderwoerd

# This is the debugged version of the file "traceback_to_debug.py"

import random  # random, not rndom
import pickle
import numpy as np
# The pickle module is not treated in this workshop. It provides some useful 
# functionality for reading and writing data from files.


with open('data_file.dat', 'rb') as f:  # data_file, not datafile
	data = pickle.load(f)

data_with_noise = data.copy()

noise_strength = 0.8
just_the_noise = []
for i in range(0, len(data)):  # Removed extra arguments
	# Note: a 1 as third argument is not wrong, but does not add functionality.
	noise = random.random()
	data_with_noise[i] += noise_strength * noise  # "+=" adds in-place.
	just_the_noise.append(noise)  # Removed erroneous indentation


mean_clean = sum(data) / len(data)
median_clean = np.sort(data)[len(data)//2]
mean_noise = sum(data_with_noise) / len(data_with_noise)
median_noise = np.sort(data_with_noise)[len(data_with_noise)//2]

# All print statements need parentheses
print("For clean data: mean = {:.4f}, median = {:.4f}".format(mean_clean, median_clean))
print("For noisy data: mean = {:.4f}, median = {:.4f}".format(mean_noise, median_noise))
print("Mean shift normal dist with uniform noise: {.6f}".format(mean_noise - mean_clean))