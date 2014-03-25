import handler
import sys
import hint
import custom_error
import score
import death

def standard(the_player):

	push_ups = 1

	while True:
		
		user_input = str(raw_input("> ")).lower()		

		if user_input == "save":
			handler.save(the_player)
		elif user_input == "inventory" or user_input == "inv":
			print "Inventory:"
			for key, item in the_player.inventory.items():
				if item > 0:
					print "- %s (%d)" % (key, item)
				elif key == 'gun' or key == 'knife' or key == 'baseball bat':
					print "- %s (%d uses left)" % (key, item)					
				elif item <= 0:
					pass

		elif user_input == "char":
			print "\n---", the_player.name, "---"
			print "Age:", the_player.age
			print "Is male?:", the_player.male
			print "Hitpoints: %.1f" % the_player.hitpoints, "/ %.1f" % the_player.max_hitpoints 
			print "Current location:", the_player.location
			print "Score:", the_player.score, "points","\n"
		elif user_input == "help":
			game_help()
		elif user_input == "look":
			print "You can go to:", ", ".join(the_player.directions)
		elif user_input == "hint":
			print "Hint:", hint.location(the_player.location)
		# EASTER EGG
		elif user_input == "push up" and the_player.age > 90:
			death.type(4, the_player)
		elif user_input == "push up" and push_ups > 18:
			death.type(5, the_player)
		elif user_input == "push up":
			push_up = score.calculate(the_player, 'push up')
			print "You've done %d sets of push ups." % push_ups
			push_ups = push_ups + 1
		elif user_input == "visited":
			print the_player.visited
		elif user_input == "quit":

			print "Are you sure? Y/N"

			while True:
				to_quit = str(raw_input("> ")).lower()

				if to_quit == "y":
					break
				elif to_quit == "n":
					return ''
				else:
					custom_error.errortype(5)

			print "Do you want to save? Y/N"
				
			while True:
				save_input = str(raw_input("> ")).lower()

				if save_input == "y":
					handler.save(the_player)
					break
				elif save_input == "n":
					break
				else:
					custom_error.errortype(5)
			exit(1)
		else:
			return user_input


def menu():

	while True:
		try:
			user_input = int(raw_input("\nType a number > "))
			return user_input
		except ValueError:
			custom_error.errortype(1)
			

def load_menu():

		while True:
			try:
				user_input = int(raw_input("\nType a number or type 0 to QUIT > "))

				if user_input == 0:
					exit(1)
				else:
					return user_input
			except ValueError:
				custom_error.errortype(1)


def load_game():

	while True:
		try:
			user_input = str(raw_input("\nLoad this character? Y/N > ")).lower()

			if user_input == "y" or user_input == "n":
				return user_input
			else:
				custom_error.errortype(5)
		except ValueError:
			custom_error.errortype(3)

def select_weapon():

	while True:
		try:
			user_input = int(raw_input("\nSelect weapon (number) > "))
			return user_input
		except ValueError:
			custom_error.errortype(1)
		except IndexError:
			return None


def conversation():

	while True:
		try:
			user_input = int(raw_input("\nSelect answer (number) > "))
			return user_input
		except ValueError:
			custom_error.errortype(1)




def game_help():

	print "\n"
	print "-" * 80
	print "Type HELP anytime to display this message."
	print "-" * 80
	print "Type these commands anytime to perform actions:"
	print " * LOOK: See where you can go."
	print " * HINT: If you're stuck, you can get little help."
	print " * SAVE: Save your progress."
	print " * INV: Will display contents of your inventory."
	print " * CHAR: Shows character stats."
	print " * QUIT: Quit game."
	print "\n Don't use verbs with things, just nouns.\n"


