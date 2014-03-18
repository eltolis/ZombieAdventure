import glob
import os.path
import time
import ast
import player
import game
import prompt
import custom_error


def save(the_player):
	save_file_name = str(the_player.name) + '.sav'
	save_file = open(save_file_name, 'w')
	save_file.truncate()
	save_file.write(str(the_player.name) + "\n")
	save_file.write(str(the_player.age) + "\n")
	save_file.write(str(the_player.male) + "\n")
	save_file.write(str(the_player.inventory) + "\n")
	save_file.write(str(the_player.hitpoints) + "\n")
	save_file.write(str(the_player.location) + "\n")
	save_file.write(str(the_player.visited) + "\n")
	save_file.write(str(the_player.score) + "\n")
	save_file.write(str(the_player.directions) + "\n")
	save_file.close()
	print "Saved as %s file" % save_file_name

def load():
	print chr(27) + "[2J"
	print "-" * 80
	print "Load game"
	print "-" * 80
	print "These are your previously saved characters:\n"
	
	saved_games = glob.glob('*.sav')

	num_of_saved_games = len(saved_games)+1
	num = 1

	while num < num_of_saved_games:

		for save_game in saved_games:
			print num, save_game.strip(' .sav')
			num = num + 1
	
	while True:
		try:
			action = prompt.load_menu()
			load_file_name = saved_games[action - 1]

			load_file = open(str(load_file_name),'r')
			print "\n--- Your selected character ---"
			print "Name: ", load_file.readline().strip("\n")
			print "Age: ", load_file.readline().strip("\n")
			print "Is male: ", load_file.readline().strip("\n")
			print "Inventory: ", load_file.readline().strip("\n")
			print "Hitpoints: ", load_file.readline().strip("\n")
			print "Location: ", load_file.readline().strip("\n")
			load_file.readline().strip("\n")
			print "Score: ", load_file.readline().strip("\n")
			load_file.readline().strip("\n")
			print "Save file:", load_file_name
			print "Last played on:", time.ctime(os.path.getmtime(load_file_name))

			choose_to_load = prompt.load_game()

			load_file.seek(0)

			load_player_name = load_file.readline().strip("\n")
			load_player_age = load_file.readline().strip("\n")
			load_player_male = load_file.readline().strip("\n")
			load_player_inventory = load_file.readline().strip("\n")
			load_player_hitpoints = load_file.readline().strip("\n")
			load_player_location = load_file.readline().strip("\n")
			load_player_visited = load_file.readline().strip("\n")
			load_player_score = load_file.readline().strip("\n")
			load_player_directions = load_file.readline().strip("\n")

			load_file.close()

			load_player_age = convert_save_file(load_player_age)
			load_player_hitpoints = convert_save_file(load_player_hitpoints)
			load_player_male = convert_save_file(load_player_male)
			load_player_inventory = convert_save_file(load_player_inventory)
			load_player_visited = convert_save_file(load_player_visited)
			load_player_score = convert_save_file(load_player_score)
			load_player_directions = convert_save_file(load_player_directions)

			if choose_to_load == "y":

				load_player = player.Player(load_player_name, 
									load_player_age, load_player_male, 
									load_player_inventory, load_player_hitpoints, 
									load_player_location, load_player_visited,
									load_player_score, load_player_directions)

				load_game = game.Engine(load_player, load_player_location)
				load_game.move()

			elif choose_to_load == "n":
				load_file.close()
				load()

		except IndexError:
			print "This save game does not exit."


def convert_save_file(file_content):
	converted_content = ast.literal_eval(file_content)
	return converted_content
