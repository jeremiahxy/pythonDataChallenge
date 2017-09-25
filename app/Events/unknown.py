from Helpers.addToLog import addToLog

def unknown(event):
	#print information to console
	print("\n\nunknown event type!!\n\n")

	#add item to log
	addToLog(event)

	return;