# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
import csv

def find_football():

    #load data in football text file
    with open('football.csv', 'r') as f:
        my_football = list(csv.reader(f))

    #list goals differences for everything
    goal_difference = []
    for i in range(1,len(my_football)):
        goal_difference.insert(i, abs(int(my_football[i][5]) - int(my_football[i][6])))

    #find lowest goal difference (+1 because first row omitted)
    team_index = goal_difference.index(min(goal_difference)) + 1

    #find correlated team name
    return my_football[team_index][0]

print(find_football())
