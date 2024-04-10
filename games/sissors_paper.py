import random

print("How many rounds do you want to play?")
rounds = int(input())
total_rounds = rounds

draw_point = 0
player_point = 0
cpu_point = 0

while rounds > 0:
    cpu_moves = ["sissors", "paper", "rock"]
    cpu_choice = random.choice(cpu_moves)
    
    print("Enter your move: 1. sissors, 2. paper, 3. rock")
    player_choice = int(input())
    
    if player_choice == 1:
        print("Your input: sissors")
    elif player_choice == 2:
        print("Your input: paper")
    elif player_choice == 3:
        print("Your input: rock")
    else:
        print("Invalid input!")
        continue
    
    print("CPU's choice:", cpu_choice)

    if player_choice == 1:
        if cpu_choice == "sissors":
            print("DRAW")
            draw_point += 1
        elif cpu_choice == "paper":
            print("You WIN!!")
            player_point += 1
        else:
            print("You LOSE!!")
            cpu_point += 1

    elif player_choice == 2:
        if cpu_choice == "sissors":
            print("You LOSE!!")
            cpu_point += 1
        elif cpu_choice == "paper":
            print("DRAW")
            draw_point += 1
        else:
            print("You WIN!!")
            player_point += 1
            
    elif player_choice == 3:
        if cpu_choice == "sissors":
            print("You WIN!!")
            player_point += 1
        elif cpu_choice == "paper":
            print("You LOSE!!")
            cpu_point += 1
        else:
            print("DRAW")
            draw_point += 1
    else:
        print("Invalid input!")
        continue

    rounds -= 1

print("------- TOTAL SCORE OF", total_rounds, "ROUNDS OF THE GAME -------")
print(f"The total draw matches among CPU and player: {draw_point} points")
print(f"The total winning matches among CPU and player: {player_point} points")
print(f"The total lost matches among CPU and player: {cpu_point} points")
input()