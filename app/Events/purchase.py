from Helpers.buildSocialNetwork import buildSocialNetwork
from Helpers.buildInvoiceAmountList import buildInvoiceAmountList
from Helpers.calculateMean import calculateMean
from Helpers.calculateStandardDeviation import calculateStandardDeviation
from Helpers.flagPurchase import flagPurchase
from Helpers.addToLog import addToLog


def purchase(event):
	user = event["id"]
	amount = float(event["amount"])

	#----
	#3 get the mean of "T" number of invoices of the users "D"-degree social network
	# subtask 1: figure out what users are in the social network
	socialNetwork = buildSocialNetwork(user)
	# print(socialNetwork)

	# subtask 2: create an array of "T" (ie - 50) most recent invoices values from any user in that network
	invoiceAmountList = buildInvoiceAmountList(socialNetwork)

	# subtask 3: calculate mean
	mean = calculateMean(invoiceAmountList)

	#----
	#4 is the amount of the transaction from 2 greater than mean plus 3 standard deviations
	# subtask 1: figure out standard deviation
	standardDeviation = calculateStandardDeviation(invoiceAmountList)

	# subtask 2: call function conditionally if transaction amount is greater than
		# mean plus 3 standard deviations
	#if amount > (mean + (3 * standardDeviation)): flagPurchase(event, mean, standardDeviation)

	print("Is Amount: ")
	print(amount)
	print("More Than: ")
	print(mean + (3 * standardDeviation))
	print("\n")
	if amount >= (mean + (3 * standardDeviation)):
		print("YES! :)")
	elif amount < (mean + (3 * standardDeviation)):
		print("NO :(")
	print("\n")

	#----
	#add item to log
	addToLog(event)

	return