def compare(player_score, comp_score):

    if player_score == comp_score:
        return f"Draw 🙃. player score: {player_score} and computer score: {comp_score} \n"
    elif comp_score == 0:
        return "Lose, opponent has Blackjack 😱 \n"
    elif player_score == 0:
        return "Win with a Blackjack 😎 \n"
    elif player_score > 21:
        return "You went over. You lose 😭 \n"
    elif comp_score > 21:
        return "Opponent went over. You win 😁 \n"
    elif player_score > comp_score:
        return f"You win 😃. player score: {player_score} and computer score: {comp_score} \n"
    else:
        return f"You lose 😤. player score: {player_score} and computer score: {comp_score} \n"
    
    
    
