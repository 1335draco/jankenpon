import random

class Computer():
    def __init__(self):
        self.last_roll = ""
        self.name = "AI"
        self.num_wins = 0


    def roll(self):
        hand = ["rock", "paper", "scissors"]
        hand_num = random.randint(0,2)
        self.last_roll = hand[hand_num]
        print(self.name + " chose: " + self.last_roll)
        return self.last_roll
