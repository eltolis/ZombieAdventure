import random
import copy
import prompt
import score
import custom_error
import death
import enemies

class Encounter(object):


	def __init__(self, the_player, enemy):
		self.the_player = the_player
		self.enemy = enemy

	
	def player_attack(self, the_player, the_enemy):

		weapons = self.player_weapon(the_player)
		bonus = self.attack_bonus(the_player)

		num_of_weapons = len(weapons)
		w_num = 1

		while w_num < num_of_weapons:
			for weapon in weapons:
				print str(w_num) + '.', weapon
				w_num = w_num + 1

		selected_weapon = prompt.select_weapon()

		if selected_weapon == None:
			print "You don't have that weapon"
			pass
		elif selected_weapon == 1: # Fist
			print "You choose %s." % weapons[selected_weapon - 1]
			use_weapon = 'fist'
			attack_points = random.randint(1,6) * bonus
		elif selected_weapon == 2: # Gun
			print "You choose %s." % weapons[selected_weapon - 1]
			use_weapon = 'gun'
			attack_points = random.randint(9,40) * bonus
		elif selected_weapon == 3: # Knife
			print "You choose %s." % weapons[selected_weapon - 1]
			use_weapon = 'knife'
			attack_points = random.randint(7,15) * bonus
		elif selected_weapon == 4: # Baseball bat
			print "You choose %s." % weapons[selected_weapon - 1]
			use_weapon = 'baseball bat'
			attack_points = (random.randint(8,13) + random.randint(1,3)) * bonus
		else:
			print "You hesitate for too long and miss your chance to hit."

		chance_of_missing = random.randint(0,5)	

		if chance_of_missing == 0:
			randomize_attack = 0
		else:
			randomize_attack = attack_points * random.uniform(0.0,1.0)
			the_enemy.enemy_hp = the_enemy.enemy_hp - randomize_attack

		if randomize_attack <= 0:
			print "You miss!"
		else:
			print "You hit %s with %s for %.2f hitpoint damage." % (the_enemy.enemy_name, use_weapon, randomize_attack)

		
		custom_error.errortype(4)

		if the_enemy.enemy_hp <= 0:
			enemy_alive = False
		else:
			enemy_alive = True

		return enemy_alive


	
	def enemy_attack(self, the_player, the_enemy):

		chance_of_missing = random.randint(0,5)

		if chance_of_missing == 0:
			randomize_enemy_attack = 0
		else:
			randomize_enemy_attack = the_enemy.enemy_attack * random.uniform(0.0,1.0)
			the_player.hitpoints = the_player.hitpoints - randomize_enemy_attack

		if randomize_enemy_attack <= 0:
			print "%s misses!" % the_enemy.enemy_name
		else:
			print "%s hits you for %.2f. You have %.2f hitpoints left." % (the_enemy.enemy_name, randomize_enemy_attack, the_player.hitpoints)

		if the_player.hitpoints <= 0:
			death.type(6, the_player)
		else:
			pass


	
	def player_weapon(self, the_player):
		
		available_weapons = ['fists']

		if 'gun' in the_player.inventory.keys():
			available_weapons.append('gun')
		elif 'knife' in the_player.inventory.keys():
			available_weapons.append('knife')
		elif 'baseball bat' in the_player.inventory.keys():
			available_weapons.append('baseball bat')
		else:
			pass

		return available_weapons

	def attack_bonus(self, the_player):

		male = the_player.male
		age = the_player.age
		
		if male == True:
			if age < 4:
				bonus = 0.2
			elif age < 8:
				bonus = 0.6
			elif age < 12:
				bonus = 1
			elif age < 17:
				bonus = 2
			elif age < 26:
				bonus = 2.8
			elif age < 33:
				bonus = 3
			elif age < 48:
				bonus = 2.6
			elif age < 61:
				bonus = 0.9
			elif age < 72:
				bonus = 0.4
			else:
				bonus = 0.1
		else:
			if age < 4:
				bonus = 0.2
			elif age < 8:
				bonus = 0.6
			elif age < 12:
				bonus = 0.9
			elif age < 17:
				bonus = 1.8
			elif age < 26:
				bonus = 2.1
			elif age < 33:
				bonus = 2.7
			elif age < 48:
				bonus = 2
			elif age < 61:
				bonus = 0.6
			elif age < 72:
				bonus = 0.2
			else:
				bonus = 0.1

		return bonus

	
	def start(self, the_player):
		
		create_enemy = enemies.SpawnEnemy(the_player, self.enemy)
		created_enemy = create_enemy.generate(the_player, self.enemy)

		the_enemy = enemies.Enemy(*created_enemy)

		enemy_alive = True

			
		initialize_fight = random.randint(0,1)

		print "\n"
		print "-" * 25
		print "--- FIGHT ---"
		print "-" * 25
		print "You face %s." % (the_enemy.enemy_name)
		print "HP: %.2f, Attack: %.2f" % (the_enemy.enemy_hp, the_enemy.enemy_attack)

		if initialize_fight == 0:
			print "You are quicker than %s, you get to attack first!" % the_enemy.enemy_name
			fight_order = 'player first'
		else:
			print "%s strikes first!" % the_enemy.enemy_name
			fight_order = 'enemy first'


		while enemy_alive:

			if fight_order == 'player first':
				enemy_alive = self.player_attack(the_player, the_enemy)
				if enemy_alive == True:
					self.enemy_attack(the_player, the_enemy)
				else:
					break

			elif fight_order == 'enemy first':
				if enemy_alive == True:
					self.enemy_attack(the_player, the_enemy)
					enemy_alive = self.player_attack(the_player, the_enemy)
				else:
					break
			else:
				pass

		print "Congratulations you kill %s." % the_enemy.enemy_name
		score.calculate(the_player, the_enemy.enemy_name)




