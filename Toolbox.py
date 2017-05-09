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

	print 'Actual number of vampire families:'
	print 'Shh Classified Intel..'
	print number_of_families
	print '\n'

	return sample_array


def estimation_equation(n, p):
	"""
	According to Equation 1.
	"""

	first_term = (n**2)/2
	second_term = 1/ np.log( 1/(1-p) )

	return int( first_term * second_term )


def mission_proceed(sample_array, time_till_detonation, probability):

	number_of_collisions = 0
	checked = []
	index = 0

	for instances in range(time_till_detonation):

		if sample_array[index] in checked:
			number_of_collisions += 1
		checked.append(sample_array[index])
		index += 1

		estimated_number_of_families = estimation_equation(len(checked), probability)

	return 'Estimated number of vampire families:', estimated_number_of_families


number_of_families = 365
time_till_detonation = 50
size = 50

sample_array = create_sample(size, number_of_families)


for probability in np.arange(0.1,1,0.05):
	print probability
	estimate = mission_proceed(sample_array, time_till_detonation, probability)
	print probability, estimate, number_of_families
