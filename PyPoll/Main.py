import os
import csv

#creating a path

path = os.path.join("Resources/election_data.csv")

#creating variables and empty list
total_votes = 0

candidate_list = []
all_candidate_votes = []
candidate_votes = []
candidate_votes_percentage = []

with open(path) as csvfile:
    file = csv.reader(csvfile, delimiter = ",")
    
    #popping the header
    csv_header = next(file)
    
    for x in file:
        #counting all the votes
        total_votes = total_votes+1
        
        #putting all the votes to an empty list
        all_candidate_votes.append(x[2])
        
        #putting unique candidates in candidate_list
        if x[2] not in candidate_list:
            candidate_list.append(x[2])
        
    #counting all the votes for EACH candidate, then putting the count in an empty list
    for x in candidate_list:
        candidate_votes.append(all_candidate_votes.count(x))
        candidate_votes_percentage.append(round(all_candidate_votes.count(x)/total_votes * 100,ndigits=3)) 
        # the above rounding of the percentage does NOT work for me. 3 has the same decimals as 4. BUT when I put 5, it works. any thoughts?????
        
#now that all the variables/list have been populated with the right data. it is time to compile the winner, and spit out the analysis.

#to calculate the name of the winning candidate:
candidate_winner = candidate_list[candidate_votes.index(max(candidate_votes))]
   
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

#lets loop through all the candidates, along with their votes percentage, and votes count
for x in range(len(candidate_list)):
    print(f"{candidate_list[x]}: {candidate_votes_percentage[x]}% ({candidate_votes[x]} Votes)")

print("-------------------------")
print(f"Winner: {candidate_winner}")
print("-------------------------")


#to output the txt file:
output = os.path.join("Analysis/Analysis.txt")
with open(output, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-------------------------\n")
    for x in range(len(candidate_list)):
        outfile.write(f"{candidate_list[x]}: {candidate_votes_percentage[x]}% ({candidate_votes[x]} Votes)\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {candidate_winner}\n")
    outfile.write("-------------------------\n")