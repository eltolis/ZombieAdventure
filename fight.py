def hit(the_player, hp):
	the_player.hitpoints = the_player.hitpoints - hp
	print "You were hit for %.1f hitpoints." % hp
	print "You have %.1f/%.1f hp now." % (the_player.hitpoints, the_player.max_hitpoints)
