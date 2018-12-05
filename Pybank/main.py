import os
import csv
import sys

pybank_csv = os.path.join("C:/Users/Teresa Barajas/SMDA201811DATA2/02-Homework/03-Python/Instructions/PyBank/Resources","budget_data.csv")

months_list = []
net = 0 
profit_lossList = []
net_change = 0
biggest_inc_profit =[]
biggest_profit_loss =[]
change = 0
changeList =[]

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
		change = (profit_lossList[index+1] - profit_lossList[index])
		changeList.append(change)
		net_change= net_change + (profit_lossList[index + 1] - profit_lossList[index])/(len(months_list)-1)
	
	#if statement to split up the list into negatives and positives
	for index in range(len(changeList)):
		if changeList[index]> 0: 
			biggest_inc_profit.append(changeList[index])
		else: 
			biggest_profit_loss.append(changeList[index])

	
#going to use a function to separate profits and losses and find max
def find_profit_gain(array):
    max = 0
    for number in biggest_inc_profit:
    	if number > max:
    		max = number
    return max
GIIP = find_profit_gain(biggest_inc_profit)
 
def find_profit_loss(array):
    min = 0
    for number in biggest_profit_loss:
    	if number < min:
    		min = number
    return min

GDIP = find_profit_loss(biggest_profit_loss)

#finding the index of the month so we can print it with our findings. 

month1 = changeList.index(GIIP)
month2 = changeList.index(GDIP)


#remember to string out the integers since we have total months stored as an integer.
#an F string would also work here

print("Total Months: " + str(len(months_list)))
print("Total $: "+ str(net))
print("Average Change: $ " + str(net_change))
print("Greatest Increase in Profits: " + str(months_list[(month1+1)]) + "($" + str(GIIP)+ ")")
print("Greatest Decrease in Profits: " + str(months_list[(month2+1)]) + "($" + str(GDIP)+ ")")

#push to text file
with open("C:/Users/Teresa Barajas/pybank_results.txt", "w") as f:
	

	f.write("Total Months: " + str(len(months_list)))
	f.write("\nTotal $: "+ str(net))
	f.write("\nAverage Change: $ " + str(net_change))
	f.write("\nGreatest Increase in Profits: " + str(months_list[(month1+1)]) + "($" + str(GIIP)+ ")")
	f.write("\nGreatest Decrease in Profits: " + str(months_list[(month2+1)]) + "($" + str(GDIP)+ ")")