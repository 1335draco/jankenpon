import player
import computer
import math

def match(player, computer):
    if player.last_roll == computer.last_roll:
        print("Rematch!\n")
        return "rematch"
    elif player.last_roll == "rock" and computer.last_roll == "scissors":
        return player
    elif player.last_roll == "rock" and computer.last_roll == "paper":
        return computer
    elif player.last_roll == "paper" and computer.last_roll == "rock":
        return player
    elif player.last_roll == "paper" and computer.last_roll == "scissors":
        return computer
    elif player.last_roll == "scissors" and computer.last_roll == "paper":
        return player
    elif player.last_roll == "scissors" and computer.last_roll == "rock":
        return computer
    else:
        print("Error!")
        print("Player's Roll: " + player.last_roll + " Computer's Roll: " + computer.last_roll)

def roll(player, computer):
    player.roll()
    computer.roll()

def game(player, computer):
    roll(player, computer)
    result = match(player, computer)
    while result == "rematch":
        roll(player, computer)
        result = match(player, computer)
    if result.name:
        print("Winner is: " + result.name)
        result.num_wins += 1

if __name__ == '__main__':
    print("Welcome to Rock, Paper Scissors")
    name = input("Choose your name:")
    new_player = player.Player(name)
    computer = computer.Computer()
    total_num_games = input("How many games do you want to play?")
    while(type(total_num_games) != int):
        try:
            total_num_games = int(total_num_games)
        except:
            print("Please use integers.")
            total_num_games = input("How many games do you want to play?")

    num_games_played = 0
    while num_games_played < math.ceil(total_num_games/2) or new_player.num_wins == computer.num_wins:
        game(new_player, computer)
        num_games_played += 1
        print(f"{new_player.name} wins: {new_player.num_wins} | {computer.name} wins: {computer.num_wins}")

    if new_player.num_wins > computer.num_wins:
        print(f"{new_player.name} wins with {new_player.num_wins} wins and {computer.name} loses with {computer.num_wins} wins")

    elif new_player.num_wins < computer.num_wins:
        print(f"{computer.name} wins with {computer.num_wins} wins and {new_player.name} loses with {new_player.num_wins} wins")

