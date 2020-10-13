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
        

      
    print("Election Results")     
    print("-----------------------------------------")
    print("Total Votes: " + str(total_vote_count))
    print("-----------------------------------------")

    top_votes = 0
    winner = ""

    for key in candidatelist:
        share_of_votes_received = candidatelist[key] / total_vote_count
        percent_received = "{:.3%}".format(share_of_votes_received)
        
        print(key, ' :', percent_received, candidatelist[key])
    
        if candidatelist[key] > top_votes:
            top_votes = candidatelist[key]
            winner = key

    print("-----------------------------------------")
    print("Winner: " + str(winner))
    
output_path = os.path.join("Analysis", "PyPoll_HW_Output.csv")

with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ',')
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['----------------------------------------------------------------------'])
    csvwriter.writerow(['Total Votes: ' + str(total_vote_count)])
    csvwriter.writerow(['----------------------------------------------------------------------'])
    for key in candidatelist:
        #csvwriter.writerow([key, ' :', percent_received, candidatelist[key]])
        csvfile.write(f"{key}: {(candidatelist[key]/total_vote_count)*100:.3f}% ({candidatelist[key]})\n")
    csvwriter.writerow(['----------------------------------------------------------------------'])
    csvwriter.writerow(['Winner: ', str(winner)])
    
    
   