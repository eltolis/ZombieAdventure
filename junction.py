import prompt
import custom_error

def enter(the_player):

	the_player.location = 'Junction'
	the_player.directions = ['Curling Street','March Street', '22nd Street', 'Foreman Ave']

	print "\nLocation:", the_player.location
	print "-" * 30

	if the_player.location in the_player.visited:

		print "You're back at %s of Curling Street again." % the_player.location
		print "You've been here before."

	else:
		the_player.visited.append(the_player.location)

		print "You pass few building in Curling Street"
		print "carefully. Thankfully no zombies are present here."
		print "Behind you is Curling Street, on your right"
		print "you can go to March Street, on your left"
		print "there's 22nd Street."
		print "If you continue to go forward you will enter Foreman Ave."

	action = prompt.standard(the_player)

	if action == "curling street":
		return 'Curling Street'
	elif action == "march street":
		return 'March Street'
	elif action == "22nd street":
		return '22nd Street'
	elif action == 'foreman ave' or action == "foreman avenue":
		return 'Foreman Ave'

	else:
		custom_error.errortype(3)