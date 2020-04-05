#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

import csv
import os

input_file = os.path.join("Resources","budget_data.csv")
output_file = os.path.join("financial_report.txt")

months = []
profits = []

monthly_profit_change = []
net_profits = 0
previous_profit = 0
current_profit = 0

#open file
with open(input_file,'r',newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    #Set the first row as the header
    csvheader = next(csvreader)

    #Loop through each row in the csvreader 
    for row in csvreader:

        #Add month to the months list
        months.append(row[0])
        
        #Set the current month's profit as final profit
        current_profit = int(row[1])

        #Add monthly profit to the profits list
        profits.append(current_profit)

        #Add up the net profits or losses
        net_profits = net_profits + current_profit

        #Set the formula for profit change
        profit_change = current_profit - previous_profit

        monthly_profit_change.append(profit_change)
        
        #Set the last month's profit as initial profit
        previous_profit = int(row[1])


#Count the total numbers of months
total_months=len(months)

#Find the average of monthly profits change
#Exclude the first monthly profit change (there's no data for its previous month's profit) and deduct that (first) month as well
average_monthly_change = format(((sum(monthly_profit_change)-monthly_profit_change[0])/(total_months-1)),'.2f')

#Find the maximum increase 
profits_greatest_increase = max(monthly_profit_change)
#Find the month with the greatest increase in profits 
month_greatest_increase = months[monthly_profit_change.index(profits_greatest_increase)]

#Find the maximum decrease 
losses_greatest_decrease = min(monthly_profit_change)
#Find the month with the greatest decrease in losses 
month_greatest_decrease = months[monthly_profit_change.index(losses_greatest_decrease)]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profits}")
print(f"Average Change: ${average_monthly_change}")
print(f"Greatest Increase in Profits: {month_greatest_increase} $({profits_greatest_increase})")
print(f"Greatest Decrease in Profits: {month_greatest_decrease} (${losses_greatest_decrease})")


with open(output_file, 'w',newline='') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_profits}\n")
    textfile.write(f"Average Change: ${average_monthly_change}\n")
    textfile.write(f"Greatest Increase in Profits: {month_greatest_increase} $({profits_greatest_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {month_greatest_decrease} (${losses_greatest_decrease})\n")

