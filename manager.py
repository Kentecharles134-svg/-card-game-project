from deck import Deck
from players import CmpPlayer, HmnPlayer


class Manager:
    def __init__(self):
        self.deck = Deck()
        self.human = None
        self.computer = CmpPlayer()
        self.round_number = 1

    def setup_game(self):
        self.deck.build_deck()
        self.deck.shuffle()

        name = input("Enter your name: ")
        self.human = HmnPlayer(name)

        self.computer = CmpPlayer()
        self.round_number = 1

        # Deal 10 cards to each player
        for _ in range(10):
            self.human.add_card(self.deck.draw_card())
            self.computer.add_card(self.deck.draw_card())

    def play_round(self):
        print(f"\n--- Round {self.round_number} ---")

        human_card = self.human.play_card()
        computer_card = self.computer.play_card()

        print(f"{self.human.name} played: {human_card}")
        print(f"Computer played: {computer_card}")

        if human_card.value > computer_card.value:
            print(f"{self.human.name} wins the round!")
            self.human.add_point()

        elif computer_card.value > human_card.value:
            print("Computer wins the round!")
            self.computer.add_point()

        else:
            print("This round is a tie!")

        print(
            f"Score: {self.human.name} {self.human.score} - "
            f"Computer {self.computer.score}"
        )

        self.round_number += 1

    def game_over(self):
        return len(self.human.hand) == 0

    def show_winner(self):
        print("\n--- Final Score ---")
        print(f"{self.human.name}: {self.human.score}")
        print(f"Computer: {self.computer.score}")

        if self.human.score > self.computer.score:
            print(f"{self.human.name} wins the game!")
        elif self.computer.score > self.human.score:
            print("Computer wins the game!")
        else:
            print("The game is a tie!")

    def start_game(self):
        self.setup_game()

        print("\nWelcome to War!")
        print("The higher card wins each round.")

        while not self.game_over():
            self.play_round()

        self.show_winner()
