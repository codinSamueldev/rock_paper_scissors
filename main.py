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


def combat_time(player, robot):
    player_wins = 0
    robot_wins = 0
    rounds = 0

    while rounds < 3: 
        print(f"""
            ------// ROUND {rounds + 1} //------""")
        
        if (player == 'r' and robot == "s") or (player == 's' and robot == "p") or (player == 'p' and robot == "r"):
            print("""
                Robot won this round.""")

            player_wins +=1
            rounds += 1
        else:
            print("""
                Robot won this round.""")
            
            robot_wins += 1
            rounds += 1

    if player_wins > robot_wins:
        print("""
            You won!""")
    elif player_wins == robot_wins:
        print("""
            OMG it is a draw!""")
    else:
        print("""
            Dude, AI will make us their slaves...""")

    return player_wins, robot_wins


if __name__ == "__main__":
    player = get_player_answer()
    robot = get_robot_answer()
    winner = combat_time(player, robot)

    print(winner)