"""
Vampire Insurgence Pre-emption Toolbox.

How many vampire families are present?

Current Challenge: Given estimates are considerably inaccurate. To tune.

"""

import random, numpy as np


def create_sample(size, number_of_families):
	'''
	Samples a sequence from the given population distribution

	Simulates the sequence of encountered vampires (lebelled with corresponding families) in the crowd.
	'''


	sample_array = []
	families = range(number_of_families)

	for i in range(size):
		sample_array.append(random.choice(families))

	return sample_array


def estimation_equation(n, p):
	"""
	According to Equation 1.
	"""

	first_term = (n**2)/2
	second_term = 1/ np.log( 1/(1-p) )

	return int( first_term * second_term )


def mission_proceed(sample_array, time_till_detonation):

	number_of_collisions = 0
	checked = []
	index = 0

	for instances in range(time_till_detonation):

		if sample_array[index] in checked:
			number_of_collisions += 1
		checked.append(sample_array[index])
		index += 1

		estimated_number_of_families = estimation_equation(len(checked), 0.7)

	return estimated_number_of_families



sample_array = create_sample(100, 300)

print mission_proceed(sample_array, 50)

