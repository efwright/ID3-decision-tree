# Data.py

import csv
import sys

# Read the data from the file
# Will return the attribute names as strings in a separate list
# Will add a numerical attribute representation as the first
# element of the data list
# Data is in form of 2D array, data[row][col]
# data[0] is the numerical attribute names
# data[*][len(data)-1] is your last column and contains the answers
def readDataFile(path):
	atrs = list()
	data = list() # data[row][col]
	with open(path) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		header = next(csv_reader)
		for atr in header:
			atrs.append(atr)
		for row in csv_reader:
			dataRow = list()
			for d in row:
				dataRow.append(int(d))
			data.append(dataRow)
	atrmap = range(0, len(data[0]))
	data = [atrmap] + data
	return (atrs, data)

# Splits data based on given attribute index (should be a column)
# Two lists will be returned, one list where all rows have the
# given attribute as 1 (Yes)
# And another list where all rows have the given attribute at 0 (No)
# The numerical attribute names are maintained and added to the top
# of each new list
def splitData(data, index):
	if index < 0 or index >= len(data[0]):
		print("Error: splitData")
		print("\tIndex " + str(index) + " is out of range 0->" + str(len(data[0])))
		sys.exit(-1)
	atrmap = data[0]
	data = data[1:]
	dataYes = list(filter(lambda row: row[index] == 1, data))
	dataNo = list(filter(lambda row: row[index] == 0, data))
	dataYes = [atrmap] + dataYes
	dataNo = [atrmap] + dataNo
	return (dataYes, dataNo)

# Remove a column from the data, a new list is generated so the
# input list is not actually edited
# This is used to remove an attribute from the data
def removeColumn(data, index):
	if index < 0 or index >= len(data[0]):
		print("Error: removeColumn")
		print("\tIndex " + str(index) + " is out of range 0->" + str(len(data[0])))
		sys.exit(-1)
	if index == len(data[0])-1:
		return list(map(lambda row: (row[:index]), data))
	else:
		return list(map(lambda row: (row[:index]+row[index+1:]), data ))

