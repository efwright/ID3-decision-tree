# Tree.py

from Data import splitData, removeColumn
from Entropy import entropy, gain, maxGain, checkPure

class Node:
	def __init__(self, name, left=None, right=None, lval=-1, rval=-1):
		self.name = name
		self.left = left
		self.right = right
		self.lval = lval
		self.rval = rval

	def __str__(self):
		return str(name)

def buildTree(data):
	# If we get to a point where have no more non-header rows or
  # non-answer columns, then we made a mistake and asked for
  # a split earlier where we should have had a leaf instead
	if len(data) <= 1 or len(data[0]) <= 1:
		print("Internal Error: buildTree encountered empty data")

	atr = maxGain(data) # Get attribute that gives maximum gain

	node = Node(data[0][atr]) # Grab nurmerical attribute from first row

	dataYes, dataNo = splitData(data, atr)
	leafYes, valYes = checkPure(dataYes, atr)
	leafNo, valNo = checkPure(dataNo, atr)

	if leafNo: # No is the left side of the tree
		node.left = buildTree(removeColumn(dataNo, atr))
	else:
		node.lval = valNo

	if leafYes: # Yes is the right side of the tree
		node.right = buildTree(removeColumn(dataYes, atr))
	else:
		node.rval = valYes

	return node

# Print tree resursive function
# Print | for depth
def _printTree(node, atrmap, depth):
	dstr = ""
	for i in range(0, depth):
		dstr += "| "
	if node.left != None:
		print(dstr + atrmap[node.name] + " 0:")
		_printTree(node.left, atrmap, depth+1)
	else:
		print(dstr + atrmap[node.name] + " 0: " + str(node.lval))
	if node.right != None:
		print(dstr + atrmap[node.name] + " 1:")
		_printTree(node.right, atrmap, depth+1)
	else:
		print(dstr + atrmap[node.name] + " 1: " + str(node.rval))

# Print tree global function
# Start with depth 0
def printTree(node, atrmap):
	_printTree(node, atrmap, 0)

# Test a single row, recursive function to traverse tree
def _testAccuracy(node, row):
	if row[node.name] == 0:
		if node.left != None:
			return _testAccuracy(node.left, row)
		else:
			return node.lval == row[len(row)-1]
	else: # == 1
		if node.right != None:
			return _testAccuracy(node.right, row)
		else:
			return node.rval == row[len(row)-1]

# Check for successes in each row, and compare to total number of rows
def testAccuracy(node, data):
	success = 0
	total   = 0

	for row in data[1:]:
		total += 1
		if _testAccuracy(node, row):
			success += 1

	return float(success) / float(total)

