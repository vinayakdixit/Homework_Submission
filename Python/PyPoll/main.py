# """ Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------
#  """
 # import necesssary Libraries and or modules
import os
import csv
 # Set file path 
csvpath = os.path.join("Resources","election_data.csv")
output_text = os.path.join("Results", "election_results.txt")
 #open csv
with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader)
     # create three lists for the Voters, County and Votes. Also create a counter to count total votes by counting total rows
    totalvotes = 0
    list_voters = []
    list_county = []
    list_votes = []

# with open(output_text, "w") as txt_file:
    for row in csvreader:
         totalvotes += 1 # counts total votes by counting toatl rows
         #list_voters.append(str(row[0]))
         #list_county.append(str(row[1]))
         list_votes.append(str(row[2]))

    print("Election Results")
    print("-----------------------")
    print(f'Total Votes ={totalvotes}')
    print("-----------------------")
with open(output_text, "w") as txt_file:
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {totalvotes}\n"
        f"-------------------------\n")

    txt_file.write(election_results)
# count the votes for individual candidates by sending ....
# the candidate one by one using a list into a function 
# function definition

    def getvotestat(candidatename):
        votes = list_votes.count(candidatename)
        #print(f'Votes for {candidatename}: {votes}')
        percent = format(round((votes/totalvotes),1), '%')
        #percent_1 = format ((votes/totalvotes),%)
        print(f'{candidatename}: {percent}   ({votes})')
        votes_stats =(f'\n{candidatename}: {percent}   ({votes})\n')
        txt_file.write(votes_stats)
        #print(percent_1)
        return votes

# end of defining function

    # Create a list of all the candidates
    list_candidate = ["Khan","Correy","Li","O'Tooley"]
    # Calling the getvotestat function and collectiong results in a list of vote counts
    list_votecount = []
    for i in range (len(list_candidate)):
        list_votecount.append(getvotestat(list_candidate[i]))

    print("-----------------------")
    #print(list_votecount)
    winner = list_candidate[list_votecount.index(max(list_votecount))]
    print(f'Winner: {winner}')
    print("-----------------------")



    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {totalvotes}\n"
        f"-------------------------\n")


    winner_result = (f"------------------\n"
        f'\n\nWinner: {winner}\n'
                 f"------------------\n")
    txt_file.write(winner_result)

# end of the code
