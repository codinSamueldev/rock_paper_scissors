"""
You know the drill

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

import random

def get_player_answer():
    #Case validation in order to ensure player choose valid option.  
    while True:
        player = input(f"""
                Type 'R' for rock
                Type 'S' for scissors
                Type 'P' for paper\n
                ->  """).lower()
        
        if player in ['r', 's', 'p']:
            break
        else:
           print("""
                 Type again...""") 
    
    return player
    

def get_robot_answer():
    robot = random.choice(['r', 's', 'p'])
    
    return robot


def combat_time(player, robot, player_wins, robot_wins):

    if (player == 'r' and robot == "s") or (player == 's' and robot == "p") or (player == 'p' and robot == "r"):
        print(f"""
            Your choice is {player}
            Robot choice is {robot}\n
            Player won this round.
            
            CURRENT SCORE:
            Your wins -> {player_wins}
            Robot wins -> {robot_wins}
            """)

        player_wins +=1
    elif player == robot:
        print(f"""
            Your choice {player}
            Robot choice {robot}\n
            Hmm funny, it is a draw.
            
            CURRENT SCORE:
            Your wins -> {player_wins}
            Robot wins -> {robot_wins}
            """)
    else:
        print(f"""
            Your choice {player}
            Robot choice {robot}\n
            Robot won this round.
            
            CURRENT SCORE:
            Your wins -> {player_wins}
            Robot wins -> {robot_wins}
            """)
        
        robot_wins += 1

    return player_wins, robot_wins

def get_winner(player_wins, robot_wins):

    if player_wins > robot_wins:
        return """
            You won!"""
    elif player_wins == robot_wins:
        return """
            OMG it is a draw!"""
    else:
        return """
            Dude, AI will make us their slaves..."""
    
    return winner


if __name__ == "__main__":
    player_win = 0
    robot_win = 0
    
    for rounds in range(3):
        print(f"""
        ------// ROUND {rounds + 1} //------""")
        player = get_player_answer()
        robot = get_robot_answer()
        player_win, robot_win = combat_time(player, robot, player_win, robot_win)

    winner = get_winner(player_win, robot_win)
    print(winner)

    