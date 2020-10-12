#Modules
import os
import csv
# define variables
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    
total_vote_count = 0


# create null dictionary to store candidate names
candidatelist = {}
#Open ElectionData.csv
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        total_vote_count += 1
        candidate = row[2]
        if candidate not in candidatelist:
            #candidatelist.update({candidate : 1})
            candidatelist[candidate] = candidatelist.get(candidate,0) +1
        else: 
            candidatelist[candidate] += 1
        
        #Percent_Received = candidatelist[1]/total_vote_count
        
        #list of candidates
        

        #calc % of votes by candidate
        
            # votes_received = (candidatelist.get(candidate,0)) / total_vote_count
            # percent_received = "{:.3%}".format(votes_received)
         
        
        # k = candidatelist.keys() 
        # v = candidatelist.values()
    
    print(total_vote_count)
    print(candidatelist)
    print (candidatelist([0][0]))
    # print(([key for key in candidatelist.keys()], [value for value in candidatelist.values()]))
    # print(candidate)
    # print(votes_received)
    # print(percent_received)
    
    
    