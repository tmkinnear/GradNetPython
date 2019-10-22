# Example of a bugged script for the "Introduction to basic Python workshop"
# Copyright T.M. Kinnear & Leon Schoonderwoerd

import rndom
import pickle
import numpy as npy
# The pickle module is not treated in this workshop. It provides some useful 
# functionality for reading and writing data from files.


with open('datafile.dat', 'rb') as f:
	data = pickle.load(f)

data_with_noise = data.copy()  # Use copy to create a separate object.

noise_strength = 0.8
just_the_noise = []
for i in range(0, len(data), 1, 1):  # Simply iterate over all indices
	noise = random.random()
	data_with_noise[i] += noise_strength * noise  # "+=" adds in-place.
		just_the_noise.append(noise)


mean_clean = sum(data) / len(data)
median_clean = np.sort(data)[len(data)//2]
mean_noise = sum(data_with_noise) / len(data_with_noise)
median_noise = np.sort(data_with_noise)[len(data_with_noise)//2]
print "For clean data: mean = {:.4f}, median = {:.4f}".format(mean_clean, median_clean)
print "For noisy data: mean = {:.4f}, median = {:.4f}".format(mean_noise, median_nois)e
print "Mean shift normal dist with uniform noise: {.6f}".format(mean_noise - mean_clean)