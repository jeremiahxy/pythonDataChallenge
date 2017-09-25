from Helpers.buildUserEventStream import userEventStream
from Helpers.filterLists import filterLists

def buildFriendList(user):
	befriendList = []
	unfriendList = []

	for event in userEventStream:
		if event["id1"] != user and event["id2"] != user:
			continue
		action = event["event_type"]
		if action == "unfriend":
			if event["id1"] == user:
				unfriendList.append(event["id2"])
			elif event["id2"] == user:
				unfriendList.append(event["id1"])
		elif action == "befriend":
			if event["id1"] == user:
				befriendList.append(event["id2"])
			elif event["id2"] == user:
				befriendList.append(event["id1"])

	friendList = list(filterLists(befriendList,unfriendList))

	# print(friendList)

	return friendList