import os
import csv

#choose 1 or 2
file_num = 1

# We need to find the file and open it
file = os.path.join('election_data' + str(file_num) + '.csv')

#We need to create an emtpty dictionary.
poll = {}


total_votes = 0

#Open the files for reading
with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)

    #Bypass the header line
    next(csvread, None)

    #create the directory
    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
    #Create 2 more empty dictionary
candidates = []
num_votes = []

#Create dictionary and append the data
for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

# Create the percent list
vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 1))

#Zip everything per group
clean_data = list(zip(candidates, num_votes, vote_percent))

#Adding everything into the winner list
winner_list = []

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

# Making the winnder string 
winner = winner_list[0]


if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

#rrinting the data
output_file = os.path.join('election_results_' + str(file_num) +'.txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#print everythign to screen
with open(output_file, 'r') as readfile:
    print(readfile.read())
