import death
import apartment
import curling_street


class Engine(object):

	def __init__(self, the_player, start_map):
		self.the_player = the_player
		self.start_map = start_map

		
	def move(self):
		
		if self.the_player.age >= 100:
			death.type(1)
		elif self.the_player.age <= 3:
			death.type(2)
		else:
			pass

		current_map = Maps.map_dict.get(self.start_map)
		
		while True:
			
			get_next_map = current_map.enter(self.the_player)
			current_map = Maps.map_dict.get(get_next_map)
			

class Maps(object):

	map_dict = {
	'Apartment': apartment,
	'Curling Street': curling_street
	}

	def visited(self):
		visited_maps = map_dict.keys()


	

	





	