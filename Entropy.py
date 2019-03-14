# Entropy.py

import math
import copy
from Data import splitData, removeColumn

# Determine probability that an attribute is 1, and an
# attribute is 0
def probability(data, index):
	numYes = 0
	numNo = 0
	numTot = len(data)-1

	if numTot <= 0:
		return (0.0, 0.0)

	for row in data[1:]:
		if row[index] == 1:
			numYes += 1
		else:
			numNo += 1

	pYes = float(numYes)/numTot
	pNo  = float(numNo) /numTot
	return (pYes, pNo)

# Calculate entropy of attribute
def entropy(data, index):
	pYes, pNo = probability(data, index)
	# Can't call log on value 0, so do a check
	return -pYes * math.log(pYes,2) if pYes > 0 else 0 
	-pNo  * math.log(pNo,2)  if pNo  > 0 else 0

# Calculate gain comparing index1 to index2
# The index2 for this algorithm should always be the answer attribute
def gain(data, index1, index2):
	dataYes, dataNo = splitData(data, index1)
	entropyYes = entropy(dataYes, index2)
	entropyNo = entropy(dataNo, index2)
	entropyBase = entropy(data, index2)
	pYes = float(len(dataYes)-1) / float(len(data)-1)
	pNo  = float(len(dataNo)-1)  / float(len(data)-1)
	return entropyBase - (pYes*entropyYes) - (pNo*entropyNo)

# Check each attribute (except for answer) and calculate gain
# with respect to answer attribute
# Returns index of highest gain attribute
def maxGain(data):
	index = 0
	mg = 0

	for i in range(0, len(data[0])-1):
		g = gain(data, i, len(data[0])-1)
		if g > mg:
			mg = g
			index = i
	return index

# Check if an attribute is pure
# The attribute will be compared against the answer
# If we have nothing in data, then choose a solution arbitarily
# If we only have one column in data, then that is the answer
# column. Choose whichever answer appears most often
# If values in index1 are all the same, and values in answer are all
# the same, then the node is pure and doesn't need to be split
# Else, the next node needs to be generated and split
# return (should_split, val) 0 or 1 for val
def checkPure(data, index1):
	if len(data) <= 0: # Numerical attributes should always be there
		print('Internal Error: data attribute header was lost')
		sys.exit(-1)

	if len(data) <= 1: # This is an empty data table
		return (False, 0)

	if len(data[0]) <= 1: # Only one column left, answer
		print("Internal Error: data only contains answer column")
		sys.exit(-1)

	if len(data[0]) <= 2: # Down to the last attribute, leaves must
                        # finish. Choose most common answer
		zero = 0
		one = 0
		for row in data[1:]:
			if row[1] == 1:
				one += 1
			else:
				zero += 1
		return(False, 1 if one > zero else 0)

	zero1 = 0
	one1  = 0
	zero2 = 0
	one2  = 0
	index2 = len(data[0])-1

	for row in data[1:]: # Count the data
		if row[index1] == 1:
			one1 += 1
		else:
			zero1 += 1
		if row[index2] == 1:
			one2 += 1
		else:
			zero2 += 1

# Since table is split before calling this, the values in index1
# should always be the same. So checking for it here MIGHT be
# redundant, but doesn't affect the accuracy
	if zero1 == 0 or one1 == 0:
		if zero2 == 0:
			return (False, 1)
		elif one2 == 0:
			return (False, 0)

	return (True, -1) # Need to split, val doesn't matter

