from manager import Manager


def main():
    while True:
        game = Manager()
        game.start_game()

        again = input("\nWould you like to play again? (y/n): ").lower()

        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
