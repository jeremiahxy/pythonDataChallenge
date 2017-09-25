import json
from Events.befriend import befriend
from Events.unfriend import unfriend
from Events.purchase import purchase
from Events.unknown import unknown

#1 grab item from stream
data = []
with open("sample_dataset/stream_log.json") as json_file:
	for line in json_file:
		data.append(json.loads(line))

# print(data)
# dataSorted = sorted(data, key=lambda event: event["event_type"])

#2 note event_type for each item from stream
for event in data:
	event_type = event["event_type"]

	#3 call function based on event_type
	if event_type == "purchase":
		purchase(event)
	elif event_type == "unfriend":
		# unfriend(event)
		pass
	elif event_type == "befriend":
		# befriend(event)
		pass
	else:
		# unknown(event)
		pass