def location(current_location):

	hints = {
	'Apartment': 'Try searching the cupboard.',
	'Curling Street': 'Notice the policeman.',
	'Foreman Ave': 'no hint',
	'Harrington River': 'no hint',
	'March Street': 'The light in the window might mean something.',
	'Junction': 'You need to decide where to go.',
	'Old Building': 'Try getting the lights on somehow.',
	'Old Building (first floor)': 'Dave might have something delicious on him.',
	'Old Building (second floor)': 'Get something good for Charlie, he will return the favor.',
	'22nd Street': 'Sometimes monsters are here, sometimes not.',
	'Wandas House': 'Type OUT to go out.'
	}

	return hints.get(current_location)
