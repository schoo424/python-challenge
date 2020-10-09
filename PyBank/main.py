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
    previous_month = 0
    total_change = 0
    greatest_increase = 0
    greatest_increase_month = ""
    greatest_decrease = 999999999
    greatest_decrease_month = ""

    for row in csvreader:                   
        total_month += 1       
        
        total_profit += int(row[1])         
     
        current_month = int(row[1])        

        if total_month > 1:
            change = current_month - previous_month
            total_change += change
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = row[0]

            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = row[0]
                
        previous_month = current_month


       
print("Financial Analysis")
print("---------------------------------------------------------------------------------")
print("Total Month: " + str(total_month))
print("Total: " + str(total_profit))
print("Avg Change: " + str(total_change/(total_month-1)))
print("Greatest Increase in Profits: " + greatest_increase_month + " " + str(greatest_increase))
print("greatest decrease in profits: " + greatest_decrease_month + " " + str(greatest_decrease))