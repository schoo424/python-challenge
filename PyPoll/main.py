import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r') as csvfile:

    total_vote = 0
    candidate_totals = dict()

    # all_candidate_with_duplicates = []
    # all_candidate_with_duplicates.append = row[2]
    
    for row in csv.DictReader(csvfile):
        total_vote += 1

        # if candidate_totals.get(row[2]):
        #     candidate_totals += 1



print ("Total Vote: " + str(total_vote))
print(candidate_totals)


