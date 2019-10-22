# Model solution for exercise 5 of the "Introduction to basic Python workshop"
# Copyright T.M. Kinnear & Leon Schoonderwoerd

list_of_integers = range(50)  # Just all integers 0-49 in this case

mean = sum(list_of_integers) / len(list_of_integers)
median = list_of_integers[int(len(list_of_integers)/2)]

print(mean, median)


# For a slightly more tricky example with 50 random integers between 0-100:
import random
random_integers = [random.randint(0,100) for i in range(50)]
mean = sum(random_integers) / len(random_integers)
median = random_integers[int(len(random_integers)/2)]

print(mean, median)  # This median is wrong. Why?

sorted_integers = sorted(random_integers)  # Because the list needs to be sorted.
mean = sum(sorted_integers) / len(sorted_integers)
median = sorted_integers[int(len(sorted_integers)/2)]

print(mean, median)