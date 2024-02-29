import random

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

# main Routine goes here

# initialise user score and computer score
user_score = 0
comp_score = 0

num_rounds = 0

target_score = int_check("Enter a target score: ")
print(target_score)

while user_score < target_score and comp_score < target_score:

    # Add one to the number of rounds (for our heading)
    num_rounds += 1
    print(f"💿💿💿Round {num_rounds} 💿💿💿")

    add_points = int(input("How many points have been won?"))
    user_score += add_points

print()
print(f"Your final score is {user_score}")