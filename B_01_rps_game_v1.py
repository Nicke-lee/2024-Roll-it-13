# Check that users have entered a valid
# option based on a list

def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a work in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

            # print error if user does not enter something that is valid
            print(error)
            print()


# Displays instructions
def instructions():
    print('''

**** Instructions ****

To begin, choose the number of rounds ( or press enter for
infinite mode).

Then play against the computer. You need to choose R (rock),
P (paper) or S (scissors).

The rules are as follows:
o Paper beats rock
o Rock beats scissors
o Scissors beats paper 

Good luck!
    ''')


# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"


        try:
            response = int(to_check)

            # check that the number is more than / equal to 1
            if response < 1:
                return "invalid"
            else:
                return response


        except ValueError:
            print(error)

# Main Routine Starts here

# Intialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]


print("💎🧾✂ Rock / Paper / Scissors Game 💎🧾✂ ")
print()

# ask user if they want to see the instructions
# show them if requested
want_instructions = string_checker("Do you want to read the instructions? ").lower()

# check users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5


# Game loops starts here
while rounds_played <= num_rounds:

    # Rounds heading (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n 💿💿💿Rounds {rounds_played +1} (Infinite mode) 💿💿💿 "
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played +1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("you chose", user_choice)

    # If user choice is exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if user are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


# Game loop ends here


# Game history / statistics area
