def errortype(error_id):

	if error_id == 0:
		print "I do not understand"
	elif error_id == 1:
		print "Put down numbers only"
	elif error_id == 2:
		raw_input("Press any key to start over")
	elif error_id == 3:
		print "Wrong input"
	elif error_id == 4:
		raw_input("\nPress any key to continue")
	else:
		pass 