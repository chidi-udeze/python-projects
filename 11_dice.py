import random


def roll_dice():
    dice1 = random.randint(1 ,6)
    dice2 = random.randint(1 ,6)
    return dice1 + dice2

def main():
    player1 = input("name of player1 :")
    player2 = input("name of player2 :")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(f"{player1} rolled :{roll1}")
    print(f"{player2} rolled :{roll2}")

    if roll1 > roll2:
        print(f"{player1} won")
    elif roll1 == roll2:
        print("Draw")
    else:
        print(f"{player2} won")

main()
