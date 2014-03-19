import sys
import custom_error
import splashscreen

def type(death_id, the_player):

		death_dict = {
			1: "\nYou're so old you barely survived the first wave of zombie attack. Just as you get out of the bed you feel pain chest. Seconds later you fall to the ground and die",
			2: "\n'Baba.. da-ba'. You're just a baby unable to do anything really. You starve to death and die.",
			3: "\nYou reached zero/negative hitpoints. You die."
			}

		get_death_type = death_dict.get(death_id)
		print get_death_type
		print "Your score is %d." % the_player.score

		custom_error.errortype(4)
		splashscreen.score_board(the_player)
		custom_error.errortype(4)
		exit(1)