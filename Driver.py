# Driver.py

import sys
from Data import readDataFile
from Entropy import entropy, gain
from Tree import buildTree, printTree, testAccuracy

def main():
	if len(sys.argv) <= 1:
		print("Need to include dataset")
		return

	print("Starting driver")

	# Read a data file
	atrs, train = readDataFile(sys.argv[1])

	# Build a tree with data
	tree = buildTree(train)

	# Print the tree
	printTree(tree, atrs)

	# Check accuracy (0.0 is 0% accuracy, 1.0 is 100% accuracy
	# I expect the accuracy of using the training set to be 100%
	print(testAccuracy(tree, train))

if __name__ == "__main__":
	main()

