import random

def play_game():
    rounds = int(input("Enter number of rounds to be played: "))
    total_rounds = rounds
    
    draw_point = 0
    player_point = 0
    cpu_point = 0
    
    while rounds > 0:
        cpu_moves = ["scissors", "paper", "rock"]
        cpu_choice = random.choice(cpu_moves)
        
        while True:
            try:
                print("Enter your move: ")
                print("1. scissors")
                print("2. paper")
                print("3. rock")
                
                player_choice = int(input())
                print()
                
                if player_choice not in [1, 2, 3]:
                    raise ValueError
                break
            except ValueError:
                print("Wrong Input! Please enter 1, 2, or 3.")
        
        if (player_choice == 1):
            print("Your choice: sissors")
        elif(player_choice == 2):
            print("Your choice: paper")
        else: 
            print("Your choice: rock")

        print("CPU's choice: ", cpu_choice)
        print()
        
        if (player_choice == 1 and cpu_choice == "scissors") or \
           (player_choice == 2 and cpu_choice == "paper") or \
           (player_choice == 3 and cpu_choice == "rock"):
            print("******Match Draw! ******\n")
            draw_point += 1
            
        elif (player_choice == 1 and cpu_choice == "paper") or \
             (player_choice == 2 and cpu_choice == "rock") or \
             (player_choice == 3 and cpu_choice == "scissors"):
            print("******You Won!******\n")
            player_point += 1
                        
        else:
            print("******You Lose!******\n")
            cpu_point += 1
            
        rounds -= 1
    
    print("------- TOTAL SCORE AMONG " + str(total_rounds) + " ROUNDS OF THE GAME -------")
    print(f"Total Draws: {draw_point}")
    print(f"Total Wins: {player_point}")
    print(f"Total Losses: {cpu_point}")
    
play_game()
