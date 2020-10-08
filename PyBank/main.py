# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    
    # Read each row of data after the header, add index
    index = 0
    for row in csvreader:
        
        #print(row)
        #print(f'[{str(csvreader.index(row))}] {row}')
        # print(f"[{index}] {row}")
        # index += 1
        print(index, row)
        index += 1

#total number of months included in the dataset

