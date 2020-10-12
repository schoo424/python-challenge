import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)

    total_vote = 0
    candidate_totals = {}
    candidates_name = []
    
    # all_candidate_with_duplicates = []
    # all_candidate_with_duplicates.append = row[2]
    
    # for row in election_data.values():
    #     if row in candidates_list:
    #         continue
    #     else:
    #         candidates_list.append(row)


    for row in csvfile:

        #count the number of rows without the column headers
        total_vote +=1
        candidates_name = row[2]
        #get the list of candidate names
        if candidates_name not in candidate_totals:
            candidate_totals.update({row[2]:1})
        else:
            candidate_totals[row[2]] += 1
        #candidate_totals.append({candidates_name})
        # if candidate_name in candidate_totals: 
            
    
        # if candidate_name in candidate_totals:
        #     candidate_totals[candidate_name] = row
        #     candidate_totals[candidate_name] = candidate_totals
        # if unique_candidates in candidate_totals:
        #     candidate_totals[]
        
            
        # if candidate_totals.get(row[2]):
        #     candidate_totals += 1



print ("Total Vote: " + str(total_vote))
print("candidate name:" + str(candidate_totals))

