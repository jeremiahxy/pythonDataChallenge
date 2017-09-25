import math

def calculateStandardDeviation(list):
	length = len(list)
	meanTotal = 0
	for num in list: meanTotal = meanTotal + num
	mean = meanTotal/length

	total = 0
	for n in list: total = total + ((n-mean)**2)
	standardDeviation = math.sqrt(total/length)
	return standardDeviation