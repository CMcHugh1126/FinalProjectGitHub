import random

# Function to get a shuffled random number
def get_random_number():
    numbers = [1, 2, 3, 4, 5, 6]
    random.shuffle(numbers)
    return numbers[0]
    "Function fetches a random number that will be used to assign the players points later on"

# Test for get_random_number():
# Ensure the function always returns a number between 1 and 6.
# Check randomness by calling it multiple times (e.g., in a loop) and validating the spread of outputs.
# Test with an altered `numbers` list to ensure it handles missing numbers or duplicates correctly.

# Function to evaluate rolls and determine if a player tuples out
def evaluate_rolls(rolls):
    if len(set(rolls)) == 1:  
        print("You rolled {} - Tupled out! You get zero points for this turn.".format(rolls))
        return 0, True
    elif len(set(rolls)) == 2:  
        fixed_value = max(set(rolls), key=rolls.count)
        print("You rolled {} - Pair detected! Fixed dice: {}".format(rolls, fixed_value))
        return sum(rolls), False
    else:  # All dice are different
        print("You rolled {}.".format(rolls))
        return sum(rolls), False
    "Function tests rolls for the function and determines what the outcome will be. This happens automatically and no user input it needed" 
# Test for evaluate_rolls():
# Test tuple-out with rolls like [4, 4, 4].
# Test pair detection with rolls like [2, 2, 5].
# Test no special conditions with rolls like [1, 3, 5].
# Test with invalid inputs like fewer than three dice or non-integer values.

# Function to calculate bonus points
def calculate_bonus(rolls):
    bonus_points = 0
    if 6 in rolls:
        bonus_points += rolls.count(6) * 5 
    if all(d % 2 == 0 for d in rolls):
        bonus_points += 10  
    if sorted(rolls) == [1, 2, 3]:
        bonus_points += 15  
    return bonus_points
    "Function calculates bonus points based on specific conditions: rolling a 6, all even numbers, or the sequence [1, 2, 3]. Adds strategic opportunities for players."
# Test for calculate_bonus():
# Test with rolls containing a 6 (e.g., [6, 3, 6]) to ensure +10 points.
# Test with all even numbers (e.g., [2, 4, 6]) to ensure +10 bonus points.
# Test with sequence [1, 2, 3] to ensure +15 bonus points.
# Test with rolls not meeting any conditions (e.g., [1, 3, 5]) to confirm no bonus point

# Function to play a turn for a player
# Function to play a turn for a player
def play_turn(player_name, current_score):
    rolls = [get_random_number(), get_random_number(), get_random_number()]
    print("{}'s turn. Initial roll: {}".format(player_name, rolls))

    fixed_dice = []
    while True:
        # Check for tuple-out or pair detection
        score, tupled_out = evaluate_rolls(rolls)
        if tupled_out:  
            print("{} tupled out. No points earned.".format(player_name))
            return current_score

        # Calculate bonus points
        bonus = calculate_bonus(rolls)
        if bonus > 0:
            print("Bonus points earned this roll: +{}".format(bonus))
        score += bonus

        # Ask the player if they want to re-roll or stop
        reroll = input("Do you want to roll the remaining die? (yes or no): ").strip().lower()
        if reroll == "no":
            total_score = current_score + score
            print("{} stops with a score of {} for this turn.".format(player_name, total_score))
            return total_score

        # Roll the remaining dice
        rolls = [get_random_number() for _ in rolls]
        print("New roll: {}".format(fixed_dice + rolls))
    "This function does the majority of the work for this game, it takes the inout from the previous functions and puts them together.This evaulates the rolls and asks the user when they want to stop rolling "
# Test for play_turn():
# Stop after the initial roll to ensure the score is correctly added.
# Re-roll the remaining die multiple times and verify score accumulation.
# Test tuple-out scenarios by rolling a matching value for the fixed dice.
# Test invalid inputs like reroll prompts other than "yes" or "no".

# Main game logic for two players and dynamic number of turns
def play_game():
    player1_score = 0
    player2_score = 0

    print("Welcome to the Dice Game! If you roll two of the same number, the pairs will be stuck or Fixed.\nIf you roll three of the same you Tuple out and get no points for that turn. \nAnswer Yes if you want to keep rolling or No if you want to keep your points. ")

    # Get the number of turns from the players
    num_turns = 5

    # Initialize scores
    player1_score = 0
    player2_score = 0

    # Player 1's turns
    for turn in range(num_turns):
        print("\nPlayer 1's Turn {}".format(turn + 1))
        player1_score = play_turn("Player 1", player1_score)

    # Player 2's turns
    for turn in range(num_turns):
        print("\nPlayer 2's Turn {}".format(turn + 1))
        player2_score = play_turn("Player 2", player2_score)

    # Return final scores
    return player1_score, player2_score
    "Function flips players turns after specified attempts. Keeps the data for player1 as well as player2"
# Test for play_game():
# Ensure both players complete exactly 5 turns each.
# Verify scores accumulate correctly across turns.
# Check proper game flow, including transitions between players and turns.
# Simulate games with multiple tuple-outs and verify final scores.

# Function to announce the winner
def announce_winner(player1_score, player2_score):
    print("\nGame Over!")
    print("Player 1's Final Score: {}".format(player1_score))
    print("Player 2's Final Score: {}".format(player2_score))
    if player1_score > player2_score:
        print("Player 1 wins!")
        return "Player 1"
    elif player2_score > player1_score:
        print("Player 2 wins!")
        return "Player 2"
    else:
        print("It's a tie!")
        return "Tie"
    "Function that figures out who wins or if there was a tie. Also prints each final score"
# Test for announce_winner():
# Test scenarios where Player 1 wins, Player 2 wins, or there’s a tie.
# Ensure correct formatting and output of scores and winner.
# Handle edge cases like both scores being zero.

# Run the game and announce winner
player1_score, player2_score = play_game()
announce_winner(player1_score, player2_score)
