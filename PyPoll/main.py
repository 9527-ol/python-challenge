# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = '/Users/ow/Desktop/python-challenge/PyPoll/election_data.csv'
print(csvpath)

# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    data={}

    for row in csvreader:
        voter=row[0]
        candidate=row[2]
        data.update({voter:candidate})


total_votes=len(data)
candidates=set(list(data.values()))
candidate_count={}
for i in candidates:
    count=sum(value == i for value in data.values())
    candidate_count.update({i:count})

sorted_candidate=sorted(candidate_count, key=candidate_count.__getitem__)
print(f'''
    #   Election Results
    #   -------------------------
    #   Total Votes: {total_votes}
    #   -------------------------''')

for i in sorted_candidate:
    print(f'    #   {i}: {candidate_count[i]/total_votes*100}% ({candidate_count[i]})')

print(f'''
    #   -------------------------
    #   Winner: {sorted_candidate[-1]}''')

