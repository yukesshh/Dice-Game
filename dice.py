import random
import time
def roll_dice():
    return random.randint(1, 6)
def print_dice(number):
    dice_faces = {
        1: "⚀", 2: "⚁", 3: "⚂",
        4: "⚃", 5: "⚄", 6: "⚅"
    }
    return dice_faces[number]
def play_game():
    print("🎲 Welcome to the Dice Game!")
    player1 = input("Enter name for Player 1: ")
    player2 = input("Enter name for Player 2: ")
    play_again = "y"
    while play_again.lower() == "y":
        input(f"\n{player1}, press Enter to roll the dice...")
        roll1 = roll_dice()
        print(f"{player1} rolled: {print_dice(roll1)} ({roll1})")
        time.sleep(1)
        if player2.lower() == "cpu":
            print(f"{player2} is rolling...")
            time.sleep(1)
        else:
            input(f"{player2}, press Enter to roll the dice...")
        roll2 = roll_dice()
        print(f"{player2} rolled: {print_dice(roll2)} ({roll2})")
        # Determine winner
        if roll1 > roll2:
            print(f"\n🏆 {player1} wins this round!")
        elif roll2 > roll1:
            print(f"\n🏆 {player2} wins this round!")
        else:
            print("\nIt's a tie!")
        play_again = input("\nDo you want to play again? (y/n): ")
    print("Thanks for playing! Goodbye 🎉")
if __name__ == "__main__":
    play_game()