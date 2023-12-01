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

if __name__ == "__main__":
    player = get_player_answer()
    robot = get_robot_answer()

    print(f"""
    Your answer is {player}
    Robot answer's {robot}
    """)