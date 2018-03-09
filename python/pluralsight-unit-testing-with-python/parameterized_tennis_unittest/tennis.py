
score_names = ["Love", "Fifteen", "Thirty", "Forty"]

def tennis_score(player1_points, player2_points):
    max_points = max(player1_points, player2_points)
    min_points = min(player1_points, player2_points)
    leading_player = 1 if max_points == player1_points else 2
    
    if max_points >= 4:
        if max_points == min_points:
            return "Deuce"
        elif max_points == min_points + 1:
            return "Advantage Player {}".format(leading_player)
        else:
            return "Win for Player {}".format(leading_player)
    elif max_points == 3 and min_points == 3:
        return "Deuce"
    else:
        if player1_points == player2_points:
            return "{0}-All".format(score_names[player1_points])
        else:
            return "{0}-{1}".format(score_names[player1_points],
                                    score_names[player2_points])
