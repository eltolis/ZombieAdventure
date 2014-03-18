import sys
import custom_error
import player
import handler
import prompt
import splashscreen
import game
import death

def splash_screen():
	print chr(27) + "[2J"
	splashscreen.intro()
	print "*" * 80
	print "***** Welcome to ZOMBIE ADVENTURE *****"
	print "*" * 80
	print "\nSelect option:"
	print "1. Start a new game"
	print "2. Load existing game"
	print "3. Quit"

	while True:
		action = prompt.menu()

		if action == 1:
			create_player = player.CreateNewPlayer()
			create_player_args = create_player.generate()
			the_player = player.Player(*create_player_args)

			print "\nYour name is %s and you're %d old." % (the_player.name, the_player.age)
			print "It is %s that you're a man." % str(the_player.male).lower()
			print "Your maximum health is %d hitpoints." % the_player.hitpoints

			print "\n1. Continue to game"
			print "2. Back to main menu"
			action = prompt.menu()

			
			if action == 1:

				if the_player.age <= 3:
					death.type(2, the_player)
				elif the_player.age >= 141:
					death.type(1, the_player)
				else:
					pass

				prompt.game_help()
				custom_error.errortype(4)
				print chr(27) + "[2J"

				a_game = game.Engine(the_player, 'Apartment')
				a_game.move()

			elif action == 2:
				handler.load()
			else:
				custom_error.errortype(3)
				custom_error.errortype(2)
				splash_screen()
				# a_game = game.Engine()
				# a_game.launch_game(the_player)
		elif action == 2:
			handler.load()
		elif action == 3:
			exit(1)
		else:
			custom_error.errortype(0)


splash_screen()

