# -*- coding: utf-8 -*-

import ast
import operator

def intro():
	print """
           _                                    _
          (_'----------------------------------'_)
          (_.==================================._)

"""

def new_game():
	print "Winter has been long in the little town of"
	print "Welton in Kentucky."
	print "Weird stuff has been happening since the summer"
	print "but the full outbreak hasn't happened until October."
	print "Government's been awfully quiet about the whole affair"
	print "and then it was too late to do anything."
	print "Everything happened quickly. Your family is gone now"
	print "and you have been surviving on snow water and ramen"
	print "for past three weeks."
	print "Now it's time to go out..."


def score_board(the_player):
	
	score_file = open('scoreboard.txt', 'r')

	if len(score_file.read()) == 0:
		score_file.close()
		scores = {}
		scores[the_player.name] = the_player.score
		score_file = open('scoreboard.txt', 'w')
		score_file.write(str(scores))
		score_file.close()
		
	else:
		score_file = open('scoreboard.txt', 'r')
		scores = ast.literal_eval(score_file.readline())
		score_file.close()

	scores[the_player.name] = the_player.score
	score_file = open('scoreboard.txt', 'w')
	score_file.write(str(scores))
	score_file.close()

	sorted_scores = sorted(scores.iteritems(), key = operator.itemgetter(1))

	print "*" * 80
	print "*** SCOREBOARD ***"
	print "*" * 80
	print "\n"
	
	for name, score in sorted_scores:
		print name, " ....... ", score





	
