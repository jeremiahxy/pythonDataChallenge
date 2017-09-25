import json
from Helpers.buildUserEventStream import D
from Helpers.buildFriendList import buildFriendList

def buildSocialNetwork(user):
	socialNetwork = [user]

	i = 0
	while i < D:
		for user in socialNetwork:
			socialNetwork = list(set(socialNetwork)|set(buildFriendList(user)))
		i += 1

	socialNetwork = sorted(socialNetwork)

	return socialNetwork