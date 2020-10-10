import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r') as csvfile:

    total_vote = 0

    for row in csv.DictReader(csvfile):
        total_vote += 1

print ("Total Vote: " + str(total_vote))
print(f'{len(row[2]}')
