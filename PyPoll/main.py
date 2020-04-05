#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won -cand_won/total
#The total number of votes each candidate won -.count
#The winner of the election based on popular vote. -max

import csv
import os

#Set the path for both input and output file
input_file = os.path.join('Resources','election_data.csv')
output_file = os.path.join('poll_analysis.txt')

vote_count = 0

candidates_list = []
votes = []
number_votes=[]
percent_vote=[]

#open csv file
with open(input_file,'r',newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #Set the first row as the header
    csvheader=next(csvreader)
    
    #Loop through each rows in csvreader
    for row in csvreader:
        #count the total numbers of votes
        vote_count += 1
        
        if row[2] not in candidates_list:
            #Add the candidates' names to the list without overlapping
            candidates_list.append(row[2])
            #Add the candidates names to the votes list 
            votes.append(row[2])
        else:
            votes.append(row[2])

    for candidate in candidates_list:
        #count the names of each candidate to count the vote
        number_votes.append(votes.count(candidate))
        #percentage of votes each candidate won
        #Format the number to three decimal points
        percent_won= format((int(votes.count(candidate))/len(votes)*100),'.3f')
        #Add the percentages each candidate won to the percent_vote list
        percent_vote.append(percent_won)

#Find who is the winner with the maximum vote
winner = candidates_list[number_votes.index(max(number_votes))]

#Print out the results
print("Election Results")
print("-------------------------")
print(f"Total Votes : {vote_count}")
print("-------------------------")

#Print the vote results for each candidate
for i in range(len(candidates_list)):
    print(f"{candidates_list[i]} {percent_vote[i]}% ({number_votes[i]})")

print("-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

#Write the results to an output file
with open(output_file,'w', newline='') as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes : {vote_count}\n")
    textfile.write("-------------------------\n")
    for i in range(len(candidates_list)):
        textfile.write(f"{candidates_list[i]} {percent_vote[i]}% ({number_votes[i]})\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("-------------------------")
