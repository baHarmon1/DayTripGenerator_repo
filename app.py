from math import isinf
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


def pick_options():  # while user is_satisfied == False
    # ask questions
    all_options = []
    pick_destination = random.choice(destinations)
    all_options.append(pick_destination)
    pick_resteraunt = random.choice(resteraunts)
    all_options.append(pick_resteraunt)
    pick_mod_of_transportation = random.choice(mode_of_transportations)
    all_options.append(pick_mod_of_transportation)
    pick_entertainment = random.choice(entertainment_options)
    all_options.append(pick_entertainment)
    # How do i assign a value to use later
    return all_options


def trip_confirmation_input():
    if_user_happy = False
    full_list = pick_options()  # make sure to return
    while if_user_happy == False:
        print(full_list)
        user_trip_confirmation = input(
            "Does this trip sound fun to you? Please reply with yes or no. ")
        if user_trip_confirmation.upper() == "YES":
            return
        elif user_trip_confirmation.upper() == "NO":
            print("Press 1 to re-pick destination ")
            print("Press 2 to re-pick resteraunt ")
            print("Press 3 to re-pick mode of transportation ")
            print("Press 4 to re-pick form of entertainment ")
            user_repick = input("Which option would you like to re-pick ")
            if user_repick == "1":
                full_list[0] = random.choice(destinations)
                print(full_list)
                user_repick_destination_confirmation = input(
                    "Is this the destination you prefer? ")
                if user_repick_destination_confirmation == "yes":
                    return
                else:
                    return
            elif user_repick == "2":
                full_list[1] = random.choice(resteraunts)
                print(full_list)
                user_repick_resteraunt_confirmation = input(
                    "Is this the resteraunt you prefer? ")
                if user_repick_resteraunt_confirmation == "yes":
                    return
                else:
                    return
            elif user_repick == "3":
                full_list[2] = random.choice(mode_of_transportations)
                print(full_list)
                user_repick_transportation_confirmation = input(
                    "Is this the mode of transportation you prefer? ")
                if user_repick_transportation_confirmation == "yes":
                    return
                else:
                    return
            elif user_repick == "4":
                full_list[3] = random.choice(entertainment_options)
                print(full_list)
                user_repick_entertainment_confirmation = input(
                    "Is this the entertainment you prefer? ")
                if user_repick_entertainment_confirmation == "yes":
                    return
                else:
                    return

                    # final_trip_confirmation()

        # else:
        #     print("You did not enter a valid command! ")
        #     trip_confirmation()


def trip_confirmation():  # Maybe condense down into another function
    welcome_message()
    trip_confirmation_input()
    # final_trip_confirmation()


# def final_trip_confirmation():
#     # add the final day trip here when complete
#     final_user_trip_confirmation = input(
#         "Are you sure this is the trip you would like to take? ")
#     if final_user_trip_confirmation.upper() == "YES":
#         print("Have a nice trip!")
#         return
#     elif final_user_trip_confirmation.upper() == "NO":
#         return trip_confirmation()
#     else:
#         print("You did not enter a valid command!")
#         return trip_confirmation()


trip_confirmation()
