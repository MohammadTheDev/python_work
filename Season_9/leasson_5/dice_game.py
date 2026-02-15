# اشتباه کد خودم

# from random import randint


# def roll_dice(num_dice=1, sides=6):
#     """Roll dice and return results."""
#     results = []
#     for _ in range(num_dice):
#         results.append(randint(1, sides))
#         return results


# def play_dice_game():
#     """A simple dice game."""
#     print("Welcome to the Dice Game!")
#     print("-" * 30)

#     player_rolls = roll_dice(2)
#     player_total = sum(player_rolls)
#     print(f"You rolled: {player_rolls} = {player_total}")

#     computer_rolls = roll_dice(2)
#     computer_total = sum(computer_rolls)
#     print(f"Computer rolled: {computer_rolls} = {computer_total}")

#     print("-" * 30)
#     if player_total > computer_total:
#         print("You win!")
#     elif player_total < computer_total:
#         print("Computer wins!")
#     else:
#         print("It's a tie!")

# play_dice_game

# درست کد کد اموز

from random import randint


def roll_dice(num_dice=1, sides=6):
    """Roll dice and return results."""
    results = []
    for _ in range(num_dice):
        results.append(randint(1, sides))
    return results


def play_dice_game():
    """A simple dice game."""
    print("Welcome to the Dice Game!")
    print("-" * 30)

    player_rolls = roll_dice(2)
    player_total = sum(player_rolls)
    print(f"You rolled: {player_rolls} = {player_total}")

    computer_rolls = roll_dice(2)
    computer_total = sum(computer_rolls)
    print(f"Computer rolled: {computer_rolls} = {computer_total}")

    print("-" * 30)
    if player_total > computer_total:
        print("🎉 You win!")
    elif player_total < computer_total:
        print("💻 Computer wins!")
    else:
        print("🤝 It's a tie!")


play_dice_game()
