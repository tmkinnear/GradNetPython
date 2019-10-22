# Model solution for exercise 8 of the "Introduction to scientific Python workshop"
# Copyright T.M. Kinnear & Leon Schoonderwoerd

import numpy as np
import matplotlib.pyplot as plt


# Get the data
with open("velocities.csv", 'r') as f:
    fdata = f.read().split('\n')
times = []
velocities = []
for line in fdata:
    t, v = line.split(',')
    times.append(float(t))  # Make sure to change str to float
    velocities.append(float(v))

# Integrate to get positions.
dt = times[1] - times[0]
# We start with one element in the list, so we can use positions[-1] in the loop below.
positions = [(velocities[1] + velocities[0]) * dt / 2]
accelerations = []
for i in range(1, len(velocities) - 1):  # To avoid indexing issues, range from [1] to [-2]
    positions.append(positions[-1] + ((velocities[i+1] + velocities[i]) * dt / 2))
    accelerations.append((velocities[i] - velocities[i-1]) / dt)
accelerations.append((velocities[-1] - velocities[-2]) / dt)  # Loop has missed the last one.

# Make a plot
plt.plot(times[:-1], positions, label='position')
plt.plot(times, velocities, label='velocity')
plt.plot(times[:-1], accelerations, label='acceleration')
plt.legend()
plt.xlabel('t')
plt.ylabel('m, m/s, m/s^2')
plt.show()


# Exercise left to the reader: instead of using a loop, this can be done with clever 'slicing' of
# the various array, which should be more efficient. See if you can implement that.
