import random


# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # check user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


# Displays instructions to user
def instructions():
    print('''

**** Instructions ****

To begin,decide on a score goal (eg: The first one to get a 
score of 50 wins).

For each round of the game, you win points by rolling dice.
The winner of the round is the one who gets 13 (or slightly less)

If you win the round, then your score will increase by the number of
points that you earned. If you first roll of two dice is a double
(eg: both dice show a three), then your score will
be DOUBLE the number of points.

If you lose the round, then you don't get any points.

If you and the computer tie (eg: you both get a score of 11, 
then you will have 11 points added to your score.

Your goal is to try to get to the target score before the
computer.

Good luck.

    ''')


# generates an integer between 0 and 6
# to simulate a roll of a die
def roll_die():
    var_result = random.randint(1, 6)
    return var_result


# rolls two dice and returns total whether we
# had a double roll
def two_rolls(who):
    double_score = "no"

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points (so far)
    user_points = roll_1 + roll_2

    # Show the user the result
    print(f"Die 1: {roll_1} \t Die 2: {roll_2}")

    return user_points, double_score


# check that users enter an integer
# that is more than 13
def int_check(question):
    while True:
        error = "Please enter an integer that is 13 or more."

        try:
            response = int(input(question))

            # check that the number is more than / equal to 13
            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# find the lowest, highest and average
# score from the list
def get_stats(stats_list):
    # sort the lists
    stats_list.sort()

    # find lowest, highest and average scores...
    lowest_score = stats_list[0]
    highest_score = stats_list[-1]
    average_score = sum(user_points) / len(user_points)

    return [lowest_score, highest_score, average_score]


# main Routine goes here

# initialise user score and computer score
user_score = 0
comp_score = 0

num_rounds = 0

# create list to hold user and computer scores ang game history
all_user_points = []
all_comp_points = []
game_history = []

# Program starts here (with heading)
print()
print("🎲🎲 Roll it 13 🎲🎲")
print()

# Displays instructions if user wants to see them
want_instructions = yes_no("Do you want to read the instructions? ").lower()

if want_instructions == "yes":
    instructions()

# Get target score (must be an integer more than 13)
print()
target_score = int_check("Enter a target score: ")
print(target_score)

# Loop game until we have a winner
while user_score < target_score and comp_score < target_score:

    # Add one to the number of rounds (for our heading)
    num_rounds += 1
    print(f"💿💿💿 Round {num_rounds} 💿💿💿")

    # Start of a single round

    # Initialise pass variables
    user_pass = "no"
    computer_pass = "no"

    # Start round...
    print("")

    # Get initial dice rolls for user
    user_first = two_rolls("User")
    user_points = user_first[0]
    double_points = user_first[1]

    # Tell the user if they are eligible for double points
    if double_points == "yes":
        print("If you win this round, you gain double points! ")

    # output initial move results
    print(f"You rolled a total of {user_points}.")
    print()

    # Get initial dice rolls for computer
    computer_first = two_rolls("Computer")
    computer_points = computer_first[0]

    print(f"The computer rolled a total of {computer_points}.")

    # Loop (while both user / computer have <= 13 points)...
    while computer_points <= 13 and user_points <= 13:

        # ask user if they want to roll again, update
        # points / status
        print()

        # If user has 13 points, we can assume they don't want to roll again!
        if user_points == 13:
            user_pass = "yes"

        if user_pass == "no":
            roll_again = yes_no("Do you want to roll the dice (type 'no' to pass): ")
        else:
            roll_again = "no"

        if roll_again == "yes":
            user_move = roll_die()
            user_points += user_move
            print(f"You rolled a {user_move}. You now have {user_points} points. ")

            if user_points > 13:
                print(f"Oops! You rolled a {user_move} so your total is {user_points}. "
                      f"Which is over 13 points . ")

                # reset user points to zero so that when we update their
                # score at the end of round it is correct.
                user_points = 0

                break

            else:
                print(f"You rolled a {user_move} and have a total score of {user_points}. ")

        else:
            user_pass = "yes"

        # Roll die for computer and update computer point
        computer_move = roll_die()
        computer_points += computer_move
        print(f"The computer rolled a {computer_move}. The computer"
              f" now has {computer_points}.  You have {user_points}")

        # if computer has 10 points or more (and is winning) it should pass
        if computer_points >= 10 and computer_points >= user_points:
            computer_pass = "yes"

        # Don't let the computer roll again if the pass condition
        # has been met in a previous iteration through the loop
        elif computer_pass == "yes":
            pass

        else:

            # Roll die for computer and update computer points
            computer_move = roll_die()
            computer_points += computer_move

        # check computer has not gone over...
        if computer_points > 13:
            print(f" The computer rolled a {computer_move}, taking their points"
                  f" to {computer_points}. This is over 13 points so the computer loses! ")
            computer_points = 0
            break

        else:
            print(f"The computer rolled a {computer_move}. The computer"
                  f" now has {computer_points}. ")

        print()
        # Tell user if they are winning, losing or if it's a tie
        if user_points > computer_points:
            result = "😀😀😀 You are ahead. 😀😀😀"
        elif user_points < computer_points:
            result = "🙁🙁🙁 The computer is ahead! 🙁🙁🙁 "
        else:
            result = "👀It's currently a tie. 👀"

        print(f"***Round update****: {result} ")
        print(f"User Score: {user_points} \t | \t Computer Score: {computer_points}")

        if computer_pass == "yes" and user_pass == "yes":
            break

    # Outside loop - double user points if they won and are eligible

    # Show round result
    print()

    if user_points < computer_points:
        print("😢😢😢Sorry you lost this round and no points "
              "have been added to your total score. The computer's score has "
              f"increased by {computer_points} points.😢😢😢 ")

        add_points = computer_points

    # Currently does not include double points!
    elif user_points > computer_points:
        # Double user points if they are eligible
        if double_points == "yes":
            user_points *= 2

            print(f"👍👍👍Yay! You won the round and {user_points} points have "
                  f"been added to your score👍👍👍")

        print("You win!!")

    else:
        print(f"👕👕👕The result for this round is a tie. You and the computer "
              f"both have {user_points}.👕👕👕")

        add_points = user_points

    # Record round result and add it to the game history
    round_result = f"Round {num_rounds} - User: {user_points} \t Computer: {computer_points}"
    game_history.append(round_result)

    # end of a single round

    # if the computer wins, add its points to its score
    if user_points < computer_points:
        comp_score += user_points

    # if it's a tie, add the points to BOTH SCORES
    else:
        comp_score += user_points
        user_score += user_points

    # Add points from round to lists to calculate stats.
    all_user_points.append(user_points)
    all_comp_points.append(computer_points)

    print()
    print(f"🎲🎲🎲 User : {user_score} points | Computer : {comp_score} points")
    print()

print()
print(f"Your final score is {user_score}")

# Display game history if user want to see it
show_history = yes_no("Do you want to see the game history? ")
if show_history == "yes":
    print("\n⌛⌛⌛Game History⌛⌛⌛")

    for item in game_history:
        print(item)

    print()

# calculate the lowest, highest and average
# scores and display them.

user_stats = get_stats(all_user_points)
comp_stats = get_stats(all_comp_points)

print("🌂🌂🌂 Game Statistics 🌂🌂🌂")
print(f"User     - Lowest Score: {user_stats[0]}\t"
      f"Highest Score: {user_stats[1]}\t"
      f"Average scores: {user_stats[2]:.2f}")

print(f"Computer - Lowest Score: {comp_stats[0]}\t"
      f"Highest Score: {comp_stats[1]}\t"
      f"Average scores: {comp_stats[2]:.2f}")
