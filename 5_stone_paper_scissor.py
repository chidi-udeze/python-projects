""" Simulate stone-paper-scissor game"""
import random

user_choice = ''
while user_choice not in ['quit', 'QUIT', 'Q', 'q']:
    user_choice = input("Choose rock, paper or scissor(use q or quit to quit):")
    bot_choice = random.choice(['rock', 'paper', 'scissor'])
    print(f'Bot chose: {bot_choice}')
    if bot_choice == user_choice:
        print("TIE")
    elif user_choice == "rock" and bot_choice == "scissor":
        print("user_win")
    elif user_choice == "paper" and bot_choice == "rock":
        print("user_win")
    elif user_choice == "scissor" and bot_choice == "paper":
        print("user_win")
    else:
        print("bot_wins")
    print()
