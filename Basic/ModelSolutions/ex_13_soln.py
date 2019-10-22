# Model solution for exercise 13 of the "Introduction to basic Python workshop"
# Copyright T.M. Kinnear & Leon Schoonderwoerd

def print_if_string(arg):
	if type(arg) == str:
		print(arg)
	else:
		print("That was not a string! Shame on you!")

# Let's see if this works as expected:
print_if_string('a')
print_if_string('')
print_if_string(0)
print_if_string(str)
print_if_string(True)