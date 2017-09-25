import json
from Helpers.buildUserEventStream import T

def buildInvoiceAmountList(socialNetwork):
	invoiceAmountList = []
	s = set(socialNetwork)

	i = 0
	with open("sample_dataset/batch_log.json") as json_file:
			for event in json_file:
				if i >= T:
					break
				eventData = json.loads(event)
				if "D" in eventData and "T" in eventData:
					pass
				elif eventData["event_type"] == "befriend" or eventData["event_type"] == "unfriend":
					pass
				elif eventData["id"] in s:
					invoiceAmountList.append(float(eventData["amount"]))
					i+=1

	return invoiceAmountList