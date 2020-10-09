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
    
      #for row in csvreader:
    total_profit = 0
    total_month = 0
    previous = 0
    total_change = 0
    greatest_increase = 0
    greatest_month = ""
    greatest_decrease = 0

    for row in csvreader:                   
        total_month += 1       
        
        total_profit += int(row[1])         
     
        current = int(row[1])        

        if total_month > 1:
            change = current - previous 
            total_change += change
            if change > greatest_increase:
                greatest_increase = change
                greatest_month = row[0]
        previous = current


       
print("Financial Analysis")
print("---------------------------------------------------------------------------------")
print("Total Month: " + str(total_month))
print("Total: " + str(total_profit))
print("Avg Change: " + str(total_change/(total_month-1)))
print("greatest increase in profits: " + greatest_month + " " + str(greatest_increase))
    

        
        
       
        
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
# Sum of all changes divided by # of (total rows -1)
        # def average(profit_loss):
        #     length = len(profit_loss)
        #     total = 0.0
        #     for number in profit_loss:
        #             total += number
        #     return total / length
        
        
#   The greatest increase in profits (date and amount) over the entire period

#   The greatest decrease in losses (date and amount) over the entire period
    
