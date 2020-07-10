import os
import csv

#creating a path

path = os.path.join("Resources/budget_data.csv")

#creating empty lists and variables
#this is a variable to store the total number of months
monthcounter = 0
#this is to calculate the total/sum of all profit/losses
totalprofit_losses = 0
#this is a first conditional for the change in profit/losses
rowstatus = False
#an empty list to store the change in profit/losses for each month
profit_losses_list = []
#this is an empty list to store the months (for the greatest increase/decrease in profits)
month_list = []
#this is an empty variable to store Max Profit
max_profit = 0
#this is an empty variable to store Min Profit
min_profit = 0
#this is an empty variable to store the MONTH of Max Profit
#    max_month and min_month



#to access the file in the path, with the csv delimiter

with open(path) as csvfile:
    file = csv.reader(csvfile, delimiter = ",")
    
    #this is to pop/remove the header.
    csv_header = next(file)
    
    for x in file:
    
        #this is to count how many row/months are in the csv file
        monthcounter = monthcounter + 1
    
        #this is to add each row of profit/losses
        totalprofit_losses = totalprofit_losses + (int(x[1]))
        
        #storing data of each profit/losses row into a variable
        currentrow = int(x[1])
        
        #this is storing months into the month_list
        month_list.append(x[0])
        
        #this is storing the change of profit/losses row , as it goes through the loop
        #first if statement will not be run, because there is no value to compare the first row of profit/losses to
        #the second time, it will go through the if statement
        
        if rowstatus is True:
            row2 = currentrow
            rowchange = row2 - row1
            #this will put each change into a list
            profit_losses_list.append(rowchange)
            #row1 now becomes current row. so next if statement, it would work.
            row1 = row2
            
        else:
            #this change the status, so that the if statement will run the second time.
            rowstatus = True
            #this is to store the value of current row - profit/losses
            row1 = currentrow

# to calculate the average change:
averagechange = sum(profit_losses_list) / len(profit_losses_list)
#this is rounding it to 2 decimal points.
averagechange = round(averagechange,2)

# since there are 85 rows of data in the profit_losses_list , and there are 86 rows of data in the month_list
# we have to remove the first row of data on the month_list , because the first row does NOT have any previous value to compare the changes to
month_list.pop(0)

# to calculate the greatest increase and decrease in profits, and for what months
max_profit = max(profit_losses_list)
min_profit = min(profit_losses_list)

max_month = month_list[profit_losses_list.index(max(profit_losses_list))]
min_month = month_list[profit_losses_list.index(min(profit_losses_list))]

# now we are going to print the analysis on the terminal:
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {monthcounter}")
print(f"Average Change: ${averagechange}")
print(f"Greatest Increase in Profits: ${max_profit} for the month of {max_month}")
print(f"Greatest Decrease in Profits: ${min_profit} for the month of {min_month}")

# lets output the analysis into a text file:
output_path = os.path.join("Analysis/Analysis.txt")
# mode = "w"  for write, instead of "r" the default
# use outfile.write for outputing to text file. NOTE:  \n is used to return to the next line. 
with open(output_path, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("---------------------------\n")
    outfile.write(f"Total Months: {monthcounter}\n")
    outfile.write(f"Average Change: ${averagechange}\n")
    outfile.write(f"Greatest Increase in Profits: ${max_profit} for the month of {max_month}\n")
    outfile.write(f"Greatest Decrease in Profits: ${min_profit} for the month of {min_month}\n")

   