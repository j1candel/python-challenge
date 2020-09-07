#Modules 
import os 
import csv

#Assigning a path to open file
budget_csv = os.path.join("Resources","budget_data.csv")

#Assigning a path to put a text file into the Analysis folder
output_path = os.path.join(".","Analysis","PyBank_analysis.txt")

#Define the function so 'budget_csv' is the sole parameter 
with open(budget_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #beginning at the second row 
    next(csvreader)
    
    #Assigning values to variables 
    total_months = 0
    total_profit = 0
    total_loss = 0
    net_profit = 0
    prev_profit = 0
    profit_difference_added = 0
    profit_difference = 0
    max_difference = 0
    min_difference =0
    name = ""

    #read through each row of data after the header
    #putting a number for each row 
    for i, row in enumerate(csvreader):
        
        #Adding up the total months 
        total_months += 1
        
        #Assigning row 1 as Profit/Loss 
        profit = int((row[1]))

        #If profit is positve then add to total_profit 
        if profit > 0:
            total_profit = total_profit + profit 
        
        #If profit is negative then add to total_loss
        if profit < 0:
            total_loss = total_loss + profit 
        
        #Add total_loss 
        net_profit = total_profit + total_loss
        
        #convert to a dollar amount 
        total =  "${:,.2f}".format(net_profit)

        #if every row is greater than zero add the difference between rows 
        if i > 0:
            profit_difference_added += (profit - prev_profit)
            profit_difference = profit - prev_profit
        
        #Assign profit to previous profit 
        prev_profit = profit

        #Divide profit_difference by total months to get average 
        average_change = profit_difference_added/(total_months)
        
        #convert to a dollar amount 
        average_change_difference =  "${:,.2f}".format(average_change)
        
        #if max difference is smaller assign to max difference 
        if max_difference < profit_difference:  
            max_difference = profit_difference
            
            #Set the name of the max value to the first row 
            max_name = str((row[0])) 

        #convert to a dollar amount 
        greatest_max_difference =  "${:,.2f}".format(max_difference)

        #if max_difference is bigger assign to max difference 
        if min_difference > profit_difference:
            min_difference = profit_difference
            
            #Set the name of the minimum value to the first row 
            min_name = str((row[0])) 
        
        #convert to a dollar amount 
        greatest_min_difference =  "${:,.2f}".format(min_difference)

    #Print out all the outputs 
    print("Financial Analysis")
    print("-------------------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: ${total}')
    print(f'Avergae Change: {average_change_difference}')
    print(f'Greatest Increase in Profits: {max_name} ({greatest_max_difference})')
    print(f'Greatest Decrease in Profits: {min_name} ({greatest_min_difference})')

#Define the function so 'output_path' is the sole parameter 
with open(output_path,"w", newline = '') as textfile:
    
    #Print all the output into a text file in Analysis 
    print("Financial Analysis", file=textfile)
    print("-------------------------------------", file=textfile)
    print(f'Total Months: {total_months}', file=textfile)
    print(f'Total: ${total}', file=textfile)
    print(f'Avergae Change: {average_change_difference}', file=textfile)
    print(f'Greatest Increase in Profits: {max_name} ({greatest_max_difference})', file=textfile)
    print(f'Greatest Decrease in Profits: {min_name} ({greatest_min_difference})', file=textfile)




