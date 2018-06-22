def calculateWinner(home, away):
    # Our match starts at 0-0
    HomeGoals = 0
    AwayGoals = 0

    # We have a function within our function
    # This one runs the '.random()' test above for a list
    def testShots(shots):

        # Start goal count at 0
        Goals = 0

        # For each shot, if it goes in, add a goal
        for shot in shots:
            if random.random() <= shot:
                Goals += 1

        # Finally, return the number of goals
        return Goals

    # Run the above formula for home and away lists
    HomeGoals = testShots(home)
    AwayGoals = testShots(away)

    # Return the score
    if HomeGoals > AwayGoals:
        print("Home Wins! {} - {}".format(HomeGoals, AwayGoals))
    elif AwayGoals > HomeGoals:
        print("Away Wins! {} - {}".format(HomeGoals, AwayGoals))
    else:
        print("Share of the points! {} - {}".format(HomeGoals, AwayGoals))

