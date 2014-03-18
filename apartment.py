import prompt
import score

def enter(the_player):

	the_player.location = 'Apartment'
	the_player.directions = ['Curling Street']

	print "\nLocation: ", the_player.location

	if the_player.location in the_player.visited:
		print "You've been here already. It's your old"
		print "apartment."

	else:
		the_player.visited.append(the_player.location)
		pass

	while True:
		action = prompt.standard(the_player)

		if action == 'curling street' and not the_player.directions[0] in the_player.visited:
			print "You take courage and step out of your apartment."
			score.calculate(the_player, 'out of the house')
			break

		elif action == 'curling street' and the_player.directions[0] in the_player.visited:
			break

		else:
			pass

	return 'Curling Street'


	