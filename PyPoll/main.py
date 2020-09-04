import os 
import csv

#Assigning a path to open file
election_csv=os.path.join("Resources","election_data.csv")

#Define the function so 'election_csv' is the sole parameter 
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

        #Setting Votes equal to the 3rd row 
        votes = str(row[2])

        #Counting the amount of Khan Votes 
        if votes == khan_votes:
            counted_khan +=1
        
        #Divide votes for Khan by total_votes to get vote share 
        khan_percentage = counted_khan/total_votes
        
        #Convert into a percentage 
        percentage_khan = "{:.0%}".format(khan_percentage)

        #Counting the amount of Correy Votes 
        if votes == correy_votes:
            counted_correy +=1
        
        #Divide votes for Correy by total_votes to get vote share 
        correy_percentage = counted_correy/total_votes
        
        #Convert into a percentage 
        percentage_correy = "{:.0%}".format(correy_percentage)

        #Counting the amount of Li Votes 
        if votes == li_votes:
            counted_li +=1

        #Divide votes for Li by total_votes to get vote share 
        li_percentage = counted_li/total_votes
        
        #Convert into a percentage 
        percentage_li = "{:.0%}".format(li_percentage)
        
        #Counting the amount of O'Tooley Votes 
        if votes == otooley_votes:
            counted_otooley +=1
        
        #Divide votes for O'Tooley by total_votes to get vote share 
        otooley_percentage = counted_otooley/total_votes
        
        #Convert into a percentage 
        percentage_otooley = "{:.0%}".format(otooley_percentage)

        Khan=percentage_khan
        Correy=percentage_correy
        Li=percentage_li
        OTooley=percentage_otooley

        if Khan > Correy and Khan > Li and Khan > OTooley:
            winner = 'Khan'
        elif Correy > Khan and Correy > Li and Correy > OTooley:
            winner = 'Correy'
        elif Li > Khan and Li > Correy and Li > OTooley:
            winner = 'Li'
        elif OTooley > Khan and OTooley > Correy and OTooley > Li:
            winner = 'OTooley'

print(counted_otooley)
print(f'Election Results')
print(f'--------------------------')
print(f'Total Votes: {total_votes}')
print(f'--------------------------')
print(f'Khan: {percentage_khan} ({counted_khan})')
print(f'Correy: {percentage_correy} ({counted_correy})')
print(f'Li: {percentage_li} ({counted_li})')
print(f"OTooley: {percentage_otooley} ({counted_otooley})")
print(f'--------------------------')
print(f'Winner: {winner}')
print(f'--------------------------')

