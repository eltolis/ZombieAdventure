import random
import prompt
import custom_error
import death
import score

def enter(the_player):

	the_player.location = 'Old Building (second floor)'
	the_player.directions = ['Old Building (first floor)']

	print "\nLocation:", the_player.location
	print "-" * 30

	if the_player.location in the_player.visited:

		charlie_greets = [
		'looking good','missed you',"haven't seen you for a while",
		'nice ass','nice outside?']

		print "You come back to %s." % the_player.location
		print "'Hey there %s, %s!' Charlie screams." % (the_player.name, random.choice(charlie_greets))

	else:
		the_player.visited.append(the_player.location)

		print "You slowly and carefully climb to second"
		print "floor. You see the source of light now."
		print "It's a small candle under the window."
		print "You see sleeping bag near it and"
		print "empty food cans around."
		print "Someone lives here, evidently."

		custom_error.errortype(4)

		charlie_check = random.randint(0,1)
		if charlie_check == 0:
			print "You feel something hard landing on your head"
			print "and almost lose conscience."
			charlie_hit = random.uniform(0.1,1.0)
			the_player.hitpoints = the_player.hitpoints - charlie_hit

			if the_player.hitpoints <= 0:
				death.type(6)
			else:
				print "You lose %.1f hitpoints." % charlie_hit
				custom_error.errortype(4)

		elif charlie_check == 1:
			print "You see something approaching fast in"
			print "your peripheral vision."
			print "You manage to roll a feet away and stand"
			print "on your feet."

			score.calculate(the_player, 'charlie hit')

		print "You see old grey man in front of you."
		print "He was definitely hiding in the dark corner"
		print "across the candle."
		print "'Howdy there, I'm awfully sorry for that!'"
		print "'I thought it was Dave, he snapped that"
		print "'rope last week and I had to fight him.'"

		end_conversation = False

		while end_conversation == False:
			print "\n'Heard some noise, is he allright?'\n"
			print "1. Yes"
			print "2. No"
			
			answer = prompt.conversation()

			if answer == 1:
				print "'Good, good, he's a good boy.'"
				print "'He used to work for me in my restaurant.'"
				print "'I know he's different now....'"
				print "'But I keep him around, as a warning'"
				print "'and to keep me safe.'"
				print "'I know it's strange, don't judge me.'"
				
				break

			elif answer == 2:

				while end_conversation == False:
	
					print "'No? What did you do to him?!'"
					print "1. The rope snapped, I just defended myself."
					print "2. I killed that fucker!"
				
					answer2 = prompt.conversation()

					if answer2 == 1:
						print "'Oh...' Looks like old man is about to cry."
						print "'I kind of got attached to him, even when'"
						print "'he became different, y'know...'"
						print "'Nevermind...'"
						
						end_conversation = True

					elif answer2 == 2:
						print "'What!!! You... I'm gonna fuckin ~#^@#$...'"
						print "Old man pulls a huge shotgun out of his"
						print "coat."
						death.type(8, the_player)

					else:
						custom_error.errortype(1)

			else:
				custom_error.errortype(1)

		print "'Hey there, my name's Charlie. What's yours?'"

		custom_error.errortype(4)

		print "'%s' you mumble." % the_player.name
		print "\nYou hear Charlie's story, about his pizza place"
		print "and life he had before."
		print "You talked for a while and he offered you to stay"
		print "for the night: 'I saw a pack of 'em from the window.'"
		print "'Wouldn't be safe for you to wander around at night.'\n"
		print "You agree and wake up late next day."

		custom_error.errortype(4)

		hp_to_heal = the_player.max_hitpoints - the_player.hitpoints
		the_player.hitpoints = the_player.hitpoints + hp_to_heal

		print "You gain %.1f hitpoints from good night sleep.\n" % hp_to_heal
		print "'Listen, %s, by the way you wouldn't have some candy'" % the_player.name
		print "'with you or something?'"
		print "'I might have a flashlight to trade...'"


	while True:
		action = prompt.standard(the_player)

		if "first floor" in action:
			return 'Old Building (first floor)'
		elif action == "chocolate" and 'flashlight' in the_player.inventory.keys() or action == "chocolate bar" and 'flashlight' in the_player.inventory.keys():
			print "Sorry, I don't have anything else to trade."
		elif action == "chocolate" or action == "chocolate bar" and the_player.inventory['chocolate bar'] >= 1:
			the_player.inventory['chocolate bar'] = the_player.inventory['chocolate bar'] - 1
			the_player.inventory['flashlight'] = 1
			print "Charlie: 'Great! Here you go, you might have a good use for it!'"
			print "He gives you working flashlight"
			score.calculate(the_player, 'flashlight')
		elif action == "chocolate" or action == "chocolate bar" and the_player.inventory['chocolate bar'] == 0:
			print "You don't have any chocolate bar to give to Charlie."
		else:
			custom_error.errortype(3)