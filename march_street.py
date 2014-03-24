import prompt
import custom_error
import fight

def enter(the_player):

	the_player.location = 'March Street'
	the_player.directions = ['Junction','Old building','Harrington River']

	print "\nLocation:", the_player.location
	print "-" * 30

	if the_player.location in the_player.visited:

		print "You come back to %s. You've been here before." % the_player.location

	else:
		the_player.visited.append(the_player.location)

		print "You leave junction of Curling Street behind"
		print "and turn right to %s." % the_player.location
		print "You see something moving towards you and feel"
		print "uneasiness and chill in your spine."

	encounter = fight.Encounter(the_player, 'child zombie')
	encounter.start(the_player)

	print "You successfully killed the enemy. Now you can safely"
	print "look around."

	action = prompt.standard(the_player)

	