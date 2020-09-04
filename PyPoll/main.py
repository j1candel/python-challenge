import os 
import csv

election_csv=os.path.join("Resources","election_data.csv")

with open(election_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Starting at the second row 
    next(csvreader)

    #Setting values to strings
    khan_votes = "Khan"
    correy_votes = "Correy"
    li_votes = "Li"
    otooley_votes = "O'Tooley"
   
    #Setting values to integers 
    total_votes = 0
    counted_khan = 0
    counted_correy = 0
    counted_li = 0
    counted_otooley = 0
 
    for row in csvreader:
        total_votes += 1

        votes = str(row[2])

        if votes == khan_votes:
            counted_khan +=1
        
        khan_percentage = counted_khan/total_votes

        if votes == correy_votes:
            counted_correy +=1
        
        correy_percentage = counted_correy/total_votes

        if votes == li_votes:
            counted_li +=1

        li_percentage = counted_li/total_votes
        
        if votes == otooley_votes:
            counted_otooley +=1
        
        otooley_percentage = counted_otooley/total_votes

print(counted_otooley)
print(f'Election Results')
print(f'--------------------------')
print(f'Total Votes: {total_votes}')
print(f'--------------------------')
print(f'Khan: {khan_percentage} ({counted_khan})')
print(f'Correy: {correy_percentage} ({counted_correy})')
print(f'Li: {li_percentage} ({counted_li})')
print(f"OTooley: {otooley_percentage} ({counted_otooley})")
print(f'--------------------------')
#print(f'Winner: {}')
print(f'--------------------------')

