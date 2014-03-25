def calculate(the_player, experience):

	experiences = {
	'chocolate bar': 8,
	'out of the house': 5,
	'gun': 10,
	'push up': 10,
	'child zombie': 14,
	'zombie male': 22,
	'zombie overlord': 100,
	'flashlight': 25,
	'brass key': 15,
	'charlie hit': 10,
	'turn on lights': 10
	}

	xp_value = experiences.get(experience)

	age = the_player.age
	sex = the_player.male

	if sex is True:
		sex_multiplier = 4
	else:
		sex_multiplier = 5

	if age < 10:
		age_multiplier = 25
	elif age >= 10 and age < 18:
		age_multiplier = 20
	elif age >= 18 and age < 33:
		age_multiplier = 16
	elif age >= 33 and age < 59:
		age_multiplier = 14
	else:
		age_multiplier = 9

	
	calculated_xp = xp_value * sex_multiplier * age_multiplier

	the_player.score = the_player.score + calculated_xp

	print "\nYou get %d score points! %d total score.\n" % (calculated_xp, the_player.score)


	return calculated_xp