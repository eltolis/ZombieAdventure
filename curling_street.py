import sys
import random
import prompt
import custom_error
import score
import fight
import death

def enter(the_player):
	the_player.location = 'Curling Street'
	the_player.directions = ['Apartment','Junction']

	print "\nLocation:", the_player.location
	print "-" * 30

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

		print "You walk out of your apartment."
		print "You are on %s, it's a large street" % the_player.location
		print "with junction at the end."
		print "There are corpses everywhere, all of them"
		print "are dead and didn't turn."
		print "Most of them probably commited suicide."
		print "You notice a corpse of policeman few meters from you."
		print "You see he has a gun on him."
	
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
		elif action == "junction":
			return 'Junction'
		else:
			custom_error.errortype(3)

	