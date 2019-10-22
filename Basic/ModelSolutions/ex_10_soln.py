# Model solution for exercise 10 of the "Introduction to basic Python workshop"
# Copyright T.M. Kinnear & Leon Schoonderwoerd

import random

my_list = [random.randint(1, 100) for i in range(50)]  # Just a random list of ints

sum_between_20_40 = 0
for i in my_list:
	if i >= 20 and i <= 40:
		sum_between_20_40 += i

bin_1 = 0
bin_2 = 0
bin_3 = 0
bin_4 = 0
for i in my_list:
	if i <= 25:
		bin_1 += i
	elif i <= 50:
		bin_2 += i 
	elif i <= 75:
		bin_3 += i 
	else:  # Or another elif.
		bin_4 += i 