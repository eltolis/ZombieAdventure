import sys
import random
import prompt
import custom_error
import score
import fight
import death

def enter(the_player):
	the_player.location = 'Curling Street'
	the_player.directions = ['Apartment','River']

	print "\nLocation:", the_player.location

	if the_player.location in the_player.visited:

		if 'gun' in the_player.inventory.keys():
			pass		

		else:
			print "There is still a gun lying on the floor."
			pass
	
		print "You're in %s again." % the_player.location
		print "You've been here before."

		pass		
	
	else:

		the_player.visited.append(the_player.location)

		print "This is a large street outside of"
		print "your apartment."
		print "You see a gun on the floor."
	
	while True:
		if the_player.hitpoints <= 0:
			death.type(3, the_player)
		else:
			pass

		action = prompt.standard(the_player)

		if action == "apartment":
			return the_player.directions[0]
			break
		elif action == "gun" and not 'gun' in the_player.inventory.keys():
			bullets = random.randint(5,10)
			the_player.inventory['gun'] = bullets
			get_score = score.calculate(the_player, 'gun')
			print "You take the gun which has %d bullets in it." % bullets
		elif action == "gun":
			print "You already have the gun!"
		elif action == "hit":
			fight.hit(the_player, 8.3)
		else:
			custom_error.errortype(3)

	