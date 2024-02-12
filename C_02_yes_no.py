def yes_no(question):
    while True:
        want_instructions = input("Do you want to read the instructions? ").lower()

        # check users enter yes (y) or no (n)
        if want_instructions == "yes" or want_instructions == "y":
            print("you chose yes")
        elif want_instructions == "no" or want_instructions == "n":
            print("you chose no")
        else:
            print("You did not choose a valid response")

