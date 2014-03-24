def location(current_location):

	hints = {
	'Apartment': 'Try searching the cupboard.',
	'Curling Street': 'See if you can take anything.'
	}

	print hints.get(current_location)
