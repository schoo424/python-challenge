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
    # print(f"CSV Header: {csv_header}")
    
    
    # index = 0
    for row in csvreader:
                
        row_count = len(list(csvreader)) + 1
        
        print("Financial Analysis")
        print("---------------------------------------------------------------------------------")
        print("Total Month: " + str(row_count))

        
        
# get the row count in the CSV 
        # row_count = len(list(csvreader)
        # record_count = row_count -1
        # print(record_count

        # def row_count()
        # print(f"[{index}] {row}")
        # index += 1        
#total number of months included in the dataset
#   The net total amount of "Profit/Losses" over the entire period

#   The average of the changes in "Profit/Losses" over the entire period
        # def average(profit_loss):
        #     length = len(profit_loss)
        #     total = 0.0
        #     for number in profit_loss:
        #             total += number
        #     return total / length
        
        
#   The greatest increase in profits (date and amount) over the entire period

#   The greatest decrease in losses (date and amount) over the entire period
    
