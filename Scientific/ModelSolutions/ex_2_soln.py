# Model solution for exercise 2 of the "Introduction to scientific Python workshop"
# Copyright T.M. Kinnear & Leon Schoonderwoerd

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

with open('weather_data.txt', 'r') as f:
    fdata = f.read().split('\n')

del fdata[-1]  # trailing newline in data file leads to spurious entry.

npoints = len(fdata)

# initialize numpy arrays for our data. We could use append() and empty lists,
# but this method is more efficient.
indices = np.zeros(npoints, dtype=int)
times = np.zeros(npoints, dtype=float)
temps = np.zeros(npoints, dtype = float)
rains = np.zeros(npoints, dtype = float)

# split the rows into the appropriate arrays, line-by-line
for i in range(npoints):
    indices[i], times[i], temps[i], rains[i] = fdata[i].split(',')


# Let's fit the temperature data. We assume it is a single sine wave oscillation with noise.
def temperature(x, a, b):  # x is the variable, a & b are parameters
    return a + b * np.sin(2 * np.pi * x / npoints)  # this argument to get a single wave.

popt, pcov = opt.curve_fit(temperature, indices, temps)

# Make a simple plot
times_plot = times /3600  # to get hours
plt.figure()  # Not necessary, but good to be explicit
plt.plot(times_plot, temps, 'ko', markersize=3, label='data')
plt.plot(times_plot, temperature(indices,*popt), 'r-', label='fit')
plt.xlabel("time (hours)")
plt.ylabel("Temperature")
plt.savefig("Fitted_temperature_data.png")
plt.legend()


# Next, we make a histogram of the rain data. We have to open a new figure!
plt.figure()
n, bins, patches = plt.hist(rains, bins=30, label='data')

# Let's finally try to fit a distribution to our histogram. We here choose a simple gaussian-like
# function with two parameters. This does not give a very good result for two reasons:
# 1. The number of bins is rather small, so we cannot optimize with more parameters.
# 2. The data is not Gaussian.
def rainfall(x, a, b):
    return a * np.exp(-(x/b)**2)

bin_centers = bins[:-1] + np.diff(bins) / 2
popt, pcov = opt.curve_fit(rainfall, bin_centers, n)

xs_to_plot = np.linspace(0, 0.5, 200)
plt.plot(xs_to_plot, rainfall(xs_to_plot, *popt), 'r-', label='fit')
plt.xlabel('Rainfall in 2-minute interval (mm)')
plt.ylabel('Occurence')
plt.legend()
plt.savefig("Fitted_rainfall_data.png")

plt.show()
