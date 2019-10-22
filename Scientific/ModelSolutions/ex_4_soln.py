# Model solution for exercise 4 of the "Introduction to scientific Python workshop"
# Copyright T.M. Kinnear & Leon Schoonderwoerd

import numpy as np
import matplotlib.pyplot as plt

#set up some options for which things to plot at the end
#can have both of these set up; however, `profile_plot' works best for few test alpha particles;
#`hist_plot' works best with lots of test particles
profile_plot = True
hist_plot = False #with enough test particles, can be used to recreate behaviour of observed results

#distances of x-offsets to the gold nucleus to run tests along
from_displacement = 0.0 #bohr radii
to_displacement = 0.01 #bohr radii
interval_displacement = 0.0001#bohr radii
y_starting_displacement = 0.05

initial_velocity = 0.05#fraction of speed of light

if profile_plot:
	prof_fig, prof_ax = plt.subplots()
	#set up the figure and axes instances if plotting profiles
	
if hist_plot:
	hist_fig, hist_ax = plt.subplots()
	#set up the figure and axes instances if plotting histogram

def mag(x,y):
	return np.sqrt(x**2 + y**2)

def get_angle(x,y):
	return np.arctan2(x,y)

#initial conditions of overall simulation - constanst
dt = 1e-5 #atomic unit time (h bar / hartree energy)
c = 137.035999 #bohr radii per atomic unit time
ke = 1.0 #1/(4 pi epsilon_0)
q_Au = 79 #electron charges
q_alpha = 2 #electron charges
m_alpha = 7294.3 #electron masses

#colour cycle; plotted lines will cycle through whichever colour codes are listed here
colours = ['k','r','g']


initial_displacements = np.arange(from_displacement,to_displacement,interval_displacement) #5.45
#empty arrays for storing the angle of deflection for each displacements and the weighting factor to account for 3D scattering
angles = np.zeros(len(initial_displacements))
weights = np.zeros(len(initial_displacements))

#iterate through each x-offset
for i,init_x in enumerate(initial_displacements):
	
	#initial conditions
	r_x = [init_x]
	r_y = [-y_starting_displacement]
	v_x = [0]
	v_y = [initial_velocity*c]
	
	myweight = np.pi*2*init_x #weighting factor for the 3D scattering accommodation
	
	init_r = mag(r_x[-1],r_y[-1]) #initial radial distance
	
	#keep looping as long as alpha particle is within 1.1 times the radial distance of its starting location
	while (mag(r_x[-1],r_y[-1]) < init_r*1.1):
		dist = mag(r_x[-1],r_y[-1]) #this far apart...
		a_mag = (ke/m_alpha) * q_Au * q_alpha / dist**2 #...results in this much acceleration...
		a_x = a_mag * r_x[-1]/dist#
		a_y = a_mag * r_y[-1]/dist#...applied this these directions...
		v_x.append(v_x[-1] + a_x*dt)#
		v_y.append(v_y[-1] + a_y*dt)#...changing velocity components by these amounts, for these new net velocities...
		r_x.append(r_x[-1] + v_x[-1]*dt)#
		r_y.append(r_y[-1] + v_y[-1]*dt)#..and these new positions

	if profile_plot:
		mycol = colours.pop(0)#`pop' (remove) the first colour off of our list
		prof_ax.plot(r_x,r_y,c=mycol) #plot a line in that colour
		colours.append(mycol) #put the colour back on at the back of the list

	angles[i] = get_angle(v_x[-1],v_y[-1]) #update final angle for this offset
	weights[i] = myweight #update the weighting factor for this offset

if hist_plot:
	hist_ax.hist(np.degrees(angles),weights=weights,log=True,bins=np.arange(0,30,5))
	theory_angles = np.linspace(0,np.pi,100)
	hist_ax.plot(np.degrees(theory_angles), np.sin(theory_angles/2)**-4.0)
	#hist_fig.show()

if profile_plot:
	prof_ax.scatter([0.0],[0.0],30,'y','o') #Gold nucleus
	prof_ax.set_aspect('equal') #makes the distance axes isotropic
	prof_ax.set_xlabel('X axis (a$_0$)')
	prof_ax.set_ylabel('X axis (a$_0$)')
	#prof_fig.show()

