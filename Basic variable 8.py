goalscored=int(input("Enter the number of goals scored overall"))
goalconceded = int(input( "Enter the number of goals conceded overall"))
goal_difference = goalscored - goalconceded
games_played =int(input("Enter the number of games played:"))
if games_played > 10 :
    average_goals = goal_difference / games_played
    print("The average goal difference per game is: " + str (average_goals))
else:
    print("The average goal difference cannot be calculated as the number of games played is less than or equal to 10")
    print("The goal difference is: " + str(goal_difference))
