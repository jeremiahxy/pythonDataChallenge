from Helpers.addToLog import addToLog

def unfriend(event):
	#print information to console
	user1 = event["id1"]
	user2 = event["id2"]
	print(user1+" unfriended "+ user2)

	#add item to log
	addToLog(event)

	return