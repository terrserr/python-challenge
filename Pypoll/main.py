import os
import csv
import sys

pypoll_csv = os.path.join("C:/Users/Teresa Barajas/SMDA201811DATA2/02-Homework/03-Python/Instructions/PyPoll/Resources","election_data.csv")
#creating lists

voterID_list = []
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0

with open(pypoll_csv, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ",")

	next(csvreader)
	for row in csvreader:
		voterID_list.append(row[0])
		if "Khan" in row[2]:
			Khan_votes = Khan_votes + 1
		elif "Correy" in row[2]:
			Correy_votes = Correy_votes + 1
		elif "Li" in row[2]:
			Li_votes = Li_votes +1
		else:
			OTooley_votes = OTooley_votes + 1


#calculate total votes

total_votes = len(voterID_list)
POVK = ("{0:.0%}".format(Khan_votes/total_votes))
POVC = ("{0:.0%}".format(Correy_votes/total_votes))
POVL = ("{0:.0%}".format(Li_votes/total_votes))
POVO = ("{0:.0%}".format(OTooley_votes/total_votes))

if POVK > POVC and POVL and POVO:
	winner = "Khan"
if POVC > POVK and POVL and POVO: 
	winner = "Correy"
if POVL > POVK and POVC and POVO: 
	winner = "Li"
if POVO > POVK and POVC and POVL: 
	winner = "O'Tooley"

#print to terminal and txt fill

print("Election Results")
print("-----------------------------------------")
print("Total Votes: " + str(total_votes))
print("-----------------------------------------")
print("Khan: " + str(POVK) + " (" + str(Khan_votes)+ ")")
print("Correy: " + str(POVC) + " (" + str(Correy_votes)+ ")")
print("Li: " + str(POVL)+ " (" + str(Li_votes)+ ")")
print("O'Tooley: " + str(POVO) + " (" + str(OTooley_votes)+ ")")
print("-----------------------------------------")
print("Winner: " + winner)
print("-----------------------------------------")

with open("C:/Users/Teresa Barajas/pypoll_results.txt", "w") as f:
	f.write("Election Results")
	f.write("\nTotal Votes: " + str(total_votes))
	f.write("\n-----------------------------------------")
	f.write("\nKhan: " + str(POVK) + " (" + str(Khan_votes)+ ")")
	f.write("\nCorrey: " + str(POVC) + " (" + str(Correy_votes)+ ")")
	f.write("\nLi: " + str(POVL)+ " (" + str(Li_votes)+ ")")
	f.write("\nO'Tooley: " + str(POVO) + " (" + str(OTooley_votes)+ ")")
	f.write("\n-----------------------------------------")
	f.write("\nWinner: " + winner)
	f.write("\n-----------------------------------------")