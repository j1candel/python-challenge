import os 
import csv

#Assigning a path to file 
budget_csv = os.path.join(".","Resources","budget_data.csv")

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
        
        #Every Row greater than zero 
        if i > 0:
            profit_difference_added += (profit - prev_profit)
            profit_difference = profit - prev_profit
        prev_profit = profit

        average_change=profit_difference_added/total_months
   
        if max_difference < profit_difference:   
            max_difference = profit_difference
            max_name = str((row[0])) 
       
        if min_difference > profit_difference:
            min_difference = profit_difference
            min_name = str((row[0])) 

    print("Financial Analysis")
    print("-------------------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: ${net_profit}')
    print(f'Avergae Change: ${average_change}')
    print(f'Greatest Increase in Profits: {max_name} (${max_difference})')
    print(f'Greatest Decrease in Profits: {min_name} (${min_difference})')




