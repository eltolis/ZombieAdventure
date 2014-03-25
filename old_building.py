# -*- coding: utf-8 -*-

import prompt
import custom_error
import score

def enter(the_player):

	the_player.location = 'Old Building'
	the_player.directions = ['March Street','Old Building (first floor)']

	print "\nLocation:", the_player.location
	print "-" * 30

	if the_player.location in the_player.visited and 'flashlight' in the_player.inventory.keys():
		print "You turn on the flashlight. Suddenly you can see all"
		print "the dead bodies in the room."

		if 'first time flash light' in the_player.visited:
			print "You see the trunk."

		else:
			the_player.visited.append('first time flash light')
			score.calculate(the_player,'turn on lights')

			print "Apart from the horrendous scene you notice a large trunk"
			print "in the back of the room."

	elif the_player.location in the_player.visited and dark:

		print "You are at the lobby of %s again. It's dark here." % the_player.location

	else:
		the_player.visited.append(the_player.location)

		print "It's very dark inside and the smell is horrible."
		print "You can't see anything but you see a little"
		print "light coming from the other side of the lobby."
		print "You see some stairs leading up to first floor."

	while True:
		action = prompt.standard(the_player)

		if action == "march street":
			return 'March Street'
		elif action == "stairs" or action == "first floor":
			return 'Old Building (first floor)'
		else:
			custom_error.errortype(3)
			pass