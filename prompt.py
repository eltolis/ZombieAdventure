import handler
import sys
import hint
import custom_error
import screen


def standard(the_player):

	while True:
		
		user_input = str(raw_input("> ")).lower()

		if user_input == "save":
			handler.save(the_player)
		elif user_input == "inventory" or user_input == "inv":
			print the_player.inventory.keys()
		elif user_input == "char":
			print "\n---", the_player.name, "---"
			print "Age:", the_player.age
			print "Is male:", the_player.male
			print "Hitpoints:", the_player.hitpoints
			print "Current location:", the_player.location
			print "Score:", the_player.score, "\n"
		elif user_input == "help":
			game_help()
		elif user_input == "look":
			print the_player.directions
		elif user_input == "hint":
			hint.location(the_player.location)
		elif user_input == "quit":

			print "Are you sure? Y/N"

			while True:
				to_quit = str(raw_input("> ")).lower()

				if to_quit == "y":
					break
				elif to_quit == "n":
					return ''
				else:
					custom_error.errortype(3)

			print "Do you want to save? Y/N"
				
			while True:
				save_input = str(raw_input("> ")).lower()

				if save_input == "y":
					handler.save(the_player)
					break
				elif save_input == "n":
					break
				else:
					custom_error.errortype(3)
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
				print "Please type in 'Y' or 'N' only."
		except ValueError:
			custom_error.errortype(3)

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

