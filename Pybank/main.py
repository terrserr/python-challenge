import os
import csv

pybank_csv = os.path.join("C:/Users/Teresa Barajas/SMDA201811DATA2/02-Homework/03-Python/Instructions/PyBank/Resources","budget_data.csv")

months_list = []
net = 0 
profit_lossList = []
net_change = 0

with open(pybank_csv, newline ="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter =",")

#indent your for loop and give another indention for all your commands you want to be in the for loop
#The next command will allow you to skip the headers
#add the values to their respective lists in this loop
#Since we are going to do math with the profit loss list, append it as an integer
	next(csvreader)
	for row in csvreader:
		months_list.append(row[0])
		net = net + int(row[1])
		profit_lossList.append(int(row[1]))

	#in another for loop, we'll calculate the change between the months' profit/loss
	#we're going to make sure our for loop isn't using the values in the list to loop through,
	#It needs to loop through the index of values, not the values themselves. We're doing a - 1 so that we don't go
	#beyond the length of the list since we have a +1 in the loop
	for index in range(len(months_list)-1):
		net_change = net_change + (profit_lossList[index] - profit_lossList[index + 1])


total_months = len(months_list)

#remember to string out the integers since we have total months stored as an integer.
#an F string would also work here

print("Total Months:" + str(total_months))
print("Total $:"+ str(net))

