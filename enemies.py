import random
import sys

class Enemy(object):

	def __init__(self, enemy_name, enemy_hp, enemy_attack):
		self.enemy_name = enemy_name
		self.enemy_hp = enemy_hp
		self.enemy_attack = enemy_attack

	
class SpawnEnemy(object):

	def __init__(self, the_player, fetch_enemy_name):
		self.the_player = the_player
		self.fetch_enemy_name = fetch_enemy_name

	def player_penalty(self, the_player):

		if self.the_player.age < 3:
			penalty = 1.0
		elif self.the_player.age < 5:
			penalty = 1.3
		elif self.the_player.age < 12:
			penalty = 1.6
		elif self.the_player.age < 17:
			penalty = 2.0
		elif self.the_player.age < 26:
			penalty = 2.4
		elif self.the_player.age < 33:
			penalty = 2.7
		elif self.the_player.age < 48:
			penalty = 2.0
		elif self.the_player.age < 60:
			penalty = 1.6
		else:
			penalty = 1.0

		return penalty


	def enemy_type(self, fetch_enemy_name):

		enemy_table = [
		('child zombie', 5, 3),
		('zombie male', 9, 5),
		('zombie overlord', 100, 20)
		]

		get_index = [i for i in enemy_table if fetch_enemy_name in i]
		return get_index[0] if enemy_table else None				
		


	def generate(self, the_player, fetch_enemy_name):
		penalty = self.player_penalty(the_player)
		created_enemy = self.enemy_type(self.fetch_enemy_name)
		
		fetch_enemy_name = created_enemy[0]
		enemy_hp = created_enemy[1] * penalty
		enemy_attack = created_enemy[2] * penalty

		return fetch_enemy_name, enemy_hp, enemy_attack


	


