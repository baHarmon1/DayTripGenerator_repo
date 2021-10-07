import random
# Maybe add all functions to another document and call for them for cleaner code
# Also clean up function and variable names
destinations = [
    "Destination: Rome",
    "Destination: Japan",
    "Destination: Germany"
]
resteraunts = [
    "Resteraunt: McDonalds",
    "Resteraunt: Panda Express",
    "Resteraunt: Taco Bell"
]
mode_of_transportations = [
    "Transportation: Drive",
    "Transportation: Fly",
    "Transportation: Walk"
]
entertainment_options = [
    "Entertainment Option: Watch a play",
    "Entertainment Option: Find street perfmormer",
    "Entertainment Option: Find a tour"
]


def welcome_message():
    user_name = input("What is your name? ")
    print(f"Hello! {user_name}, lets find you a trip! ")


def pick_options():
    all_options = []
    pick_destination = random.choice(destinations)
    all_options.append(pick_destination)
    pick_resteraunt = random.choice(resteraunts)
    all_options.append(pick_resteraunt)
    pick_mod_of_transportation = random.choice(mode_of_transportations)
    all_options.append(pick_mod_of_transportation)
    pick_entertainment = random.choice(entertainment_options)
    all_options.append(pick_entertainment)
    return all_options


def trip_confirmation_input():
    user_trip_confirmation = input(
        "Does this trip sound fun to you? Please reply with yes or no. ")
    if user_trip_confirmation.upper() == "YES":
        return
    elif user_trip_confirmation.upper() == "NO":
        trip_confirmation()
    else:
        print("You did not enter a valid command! ")
        trip_confirmation()


def trip_confirmation():  # Maybe condense down into another function
    welcome_message()
    final_trip_list = pick_options()
    print(final_trip_list)
    trip_confirmation_input()
    print(final_trip_list)
    final_user_trip_confirmation = input(
        "Are you sure this is the trip you would like to take? ")
    if final_user_trip_confirmation.upper() == "YES":
        print("Have a nice trip!")
        return
    elif final_user_trip_confirmation.upper() == "NO":
        trip_confirmation()
    else:
        print("You did not enter a valid command!")
        trip_confirmation()


trip_confirmation()
