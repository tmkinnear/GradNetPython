# Model solution for exercise 3 of the "Introduction to scientific Python workshop"
# Copyright T.M. Kinnear & Leon Schoonderwoerd

import copy
import numpy as np
import matplotlib.pyplot as plt


# This model solution comes in two parts. The first part is a very basic simulation of just two
# point masses. The second part is a generalization to multiple masses. To make this latter
# simulation easier to follow in the code, some python structure that has not been explained
# in the workshop notes has been used: classes.

# A class in python is a way to describe a custom 'object'. In python, essentially everything is
# an object: variables, types, functions, etc. Consider how, for floats, some operations are
# implemented by default (e.g., addition, multiplication, printing out), but some do not make sense
# (e.g., indexing, adding an element as you would to a list). Classes allow us to define a new
# object that can behave in custom ways. In the case described below, we will create a 'particle'
# class to describe everything a particle can do.

# ==============================
# Part 1: simple 2-body problem.
# ==============================

# Constant
# newtonG = 6.6743015e-11
newtonG = 1
dt = 0.1
tmax = 50
m1, m2 = 1, 20

# Initial conditions
r1 = np.array([10, 0], dtype=float)   # we will be using numpy array operations for vector calculus.
r2 = np.array([0, 0], dtype=float)
v1 = np.array([0, np.sqrt(2)])  # should give a circular orbit?
v2 = np.array([0,0], dtype=float)

x1_list = [r1[0]]  # Want to track positions over time
y1_list = [r1[1]]
x2_list = [r2[0]]
y2_list = [r2[1]]


def force_on_particle(pos1, pos2, mass1, mass2):
    r_relative = pos2 - pos1  # Check sign
    norm = np.linalg.norm(r_relative)
    mag = newtonG * mass1 * mass2 / (norm**2)
    return mag * r_relative / norm


# Now for the actual simulation
for t in np.arange(0, tmax, dt):
    force_on_1 = force_on_particle(r1, r2, m1, m2)
    a1 = force_on_1 / m1
    a2 = - force_on_1 / m2
    v1 += a1 * dt
    v2 += a2 * dt
    r1 += v1 * dt
    r2 += v2 * dt

    x1_list.append(r1[0])
    y1_list.append(r1[1])
    x2_list.append(r2[0])
    y2_list.append(r2[1])

# Make a plot
plt.plot(x1_list, y1_list, label='1')
plt.plot(x2_list, y2_list, label='2')
plt.plot(x1_list[0], y1_list[0], 'kx', label='1 Start')
plt.plot(x2_list[0], y2_list[0], 'rx', label='2 Start')
plt.legend()
# plt.show()  # Uncomment to make the plot.
plt.clf()


# ===================================================
# Part 2: advanced many-body simulation using classes
# ===================================================


class particle():
    def __init__(self, r, v, a, m):
        self.r = np.array(r, dtype=float)
        self.v = np.array(v, dtype=float)
        self.a = np.array(a, dtype=float)
        self.m = m
        self.all_x = []
        self.all_y = []

    def update_a(self, force):
        self.a += force / self.m

    def reset_a(self):
        self.a = 0

    def update(self, dt):
        self.v += self.a * dt
        self.r += self.v * dt
        self.all_x.append(self.r[0])
        self.all_y.append(self.r[1])


# Initialize our particles. The first two give the exact same simulation as before
particles = [particle([0, 0], [0,0], [0,0], 20),
             particle([10, 0], [0, np.sqrt(2)-0.5], [0,0], 1),
             particle([-20, 0], [0, -1], [0, 0], 0.05)
             ]
n_particles = len(particles)

# The code below this line is general for any number of particles
for t in np.arange(0, tmax, dt):
    for particle in particles:
        particle.reset_a()

    # Loop over all particles pairwise to find the forces between them:
    for i in range(n_particles):
        print("i = {}".format(i))
        for j in range(i + 1, n_particles):  # Avoid double counting
            print("j= {}".format(j))
            particle1 = particles[i]
            particle2 = particles[j]
            force = force_on_particle(particle1.r, particle2.r, particle1.m, particle2.m)
            particle1.update_a(force)
            particle2.update_a(-force)

    # Then another loop to update velocities and positions
    for particle in particles:  # No need for indexing
        particle.update(dt)

# plot results
for particle in particles:
    plt.plot(particle.all_x, particle.all_y)
plt.show()
