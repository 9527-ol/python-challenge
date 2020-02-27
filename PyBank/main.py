# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = '/Users/ow/Desktop/python-challenge/PyBank/budget_data.csv'
print(csvpath)
# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #     Financial Analysis
    #   ----------------------------
    #   Total Months: 86
    #   Total: $38382578
    #   Average  Change: $-2315.12
    #   Greatest Increase in Profits: Feb-2012 ($1926159)
    #   Greatest Decrease in Profits: Sep-2013 ($-2196167)

    total_month=0
    total_profit=0
    counter=0
    prev_month=0
    cur_month=0
    change=0
    greatest_month=''
    greatest_profit=0
    lowest_month=''
    lowest_profit=0

    for row in csvreader:
        counter=counter+1
        month=row[0]
        profit=int(row[1])
        total_month=total_month+1
        total_profit=total_profit+profit
        if profit>greatest_profit:
            greatest_profit=profit
            greatest_month=month
        if profit<lowest_profit:
            lowest_profit=profit
            lowest_month=month
        if counter>1:
            cur_month=profit
            change=change+cur_month-prev_month
        prev_month=profit

    avg_change=change/(total_month-1)

    summary=f'''#     Financial Analysis
    #   ----------------------------
    #   Total Months: {total_month}
    #   Total: ${total_profit}
    #   Average  Change: ${avg_change}
    #   Greatest Increase in Profits: {greatest_month} (${greatest_profit})
    #   Greatest Decrease in Profits: {lowest_month} (${lowest_profit})'''
    print(summary)