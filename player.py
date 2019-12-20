class Player():
    def __init__(self, name):
        self.last_roll = ""
        self.name = name
        self.num_wins = 0

    def roll(self):
        hand = input("Rock, Paper, or Scissors?")
        hand = hand.lower()

        while hand != "rock" and hand != "paper" and hand != "scissors":
            hand = input("Rock, Paper, or Scissors?")
            hand = hand.lower()
        self.last_roll = hand
        return self.last_roll
