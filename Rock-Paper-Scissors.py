import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def choose_move(self):
        move = input('Enter move(rock, paper or scissors): ')
        if move in ('rock', 'paper', 'scissors'):
            return move
        else:
            print('Invalid Input')
            return self.choose_move()


class Computer(Player):
    def choose_move(self):
        return random.choice(('rock', 'paper', 'scissors'))


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'It\'s a tie.'
    elif ((player_choice == 'rock' and computer_choice == 'scissors') |
             (player_choice == 'scissors' and computer_choice == 'paper') |
             (player_choice == 'paper' and computer_choice == 'rock')):
        return 'Player wins'

    else:
        return 'Computer wins'


class Game:
    def __init__(self):
        self.player = Player('Player')
        self.computer = Computer('AI')
        self.player_score = 0
        self.computer_score = 0

    def play_round(self):
        player_choice = self.player.choose_move()
        computer_choice = self.computer.choose_move()
        print(f'Computer chose: {computer_choice}')        
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        if "Player wins" in result:
            self.player_score += 1
        elif "Computer wins" in result:
            self.computer_score += 1

        print(f"Score - You: {self.player_score}, Computer: {self.computer_score}\n") 

    def play_game(self):
        print("Welcome to Rock-Paper-Scissors! Best of 3 rounds.")
        while self.player_score < 2 and self.computer_score < 2:
            self.play_round()

        if self.player_score > self.computer_score:
            print("Congratulations! You won the game!")
        else:
            print("Computer wins the game! Better luck next time!")
            
        self.play_again()
    
    def play_again(self):
        choice = input("Do you want to play again? (yes/no): ").lower()
        while choice not in ["yes", "no"]:
            choice = input("Invalid input. Please enter 'yes' or 'no': ").lower()

        if choice == "yes":
            self.player_score = 0
            self.computer_score = 0
            self.play_game()
        else:
            print("Thanks for playing! Goodbye!")


# Test Case
# Run the game manually
game = Game()
game.play_game()
