import json

userEventStream = []
with open("sample_dataset/batch_log.json") as json_file:
	print("opened file")
	for line in json_file:
		lineData = json.loads(line)
		if "D" in lineData and "T" in lineData:
			D = int(lineData["D"])
			T = int(lineData["T"])
		elif lineData["event_type"] == "befriend" or lineData["event_type"] == "unfriend":
			userEventStream.append(lineData)