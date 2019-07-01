# Required Output
#   """ Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#    ----------------"""

# First open ad read the file from the location
# set the file path
import os
import csv
print("--------------------------------")
csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
# """ with open(csvpath, newline="") as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",") """

# create a loop to go through all the rows and pring total number of rows
    totalrows =0
    list_gain =[]
    currentelement = 0
    list_delta=[]
    list_month=[]

# for loop to to read through the csvreader row by row
    for row in csvreader:
        totalrows += 1
        list_gain.append(float(row[1])) # Creates a list of profit/loss data (second column in the data set)
        list_month.append(str(row[0])) # creates a list of months (first column in the dataset)
        
    totalgain = sum(list_gain) # calculates total profit/loss from the list
    
    print (f'Total Months = {totalrows}') 
    print(f'Total Profit/(Loss) = ${totalgain}')
    # Following loop is to calculate delta/change of profit/loss between the consicutive months 
for x in range(len(list_gain)):
    if x < len(list_gain)-1:
        #print(list_gain[x]) # to check if the list is created correctly
        currentelement = list_gain[x]
        nextelement = list_gain[x+1]
        delta = nextelement - currentelement
        list_delta.append(delta) # list to capture all the consicutive month delta/change

maxgain = max(list_delta) # calculates max change
mingain = min(list_delta) # calculates min change
avg_change = round ((sum(list_delta)/len(list_delta)),0) # calculates average change
print(f'Average Gain: $ {avg_change}')

# find the index for the max and min from the delta/change list
# pass the index into the list of months to get associated month for max and min value of the change

maxgainindex = list_delta.index(max(list_delta))
mingainindex = list_delta.index(min(list_delta))

print(f'Greatest increase in profits: {list_month[maxgainindex]}  $({maxgain})')
print(f'Greatest decrease in profits: {list_month[mingainindex]}  $({mingain})')
print("--------------------------------")

