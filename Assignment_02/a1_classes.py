"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class
"""
Wong Jie An
27/08/2019
this program tracks where the user has been and places they hope to visit in future
*https://github.com/b3nwong/Assignment_01/tree/master*
*sorry I couldn't access the classroom repository as I have not verified my student status with github*
"""

import csv
import sys

#load file
def open_file():
    global travel_list
    with open('places.csv', 'r') as file:
        reader = csv.reader(file)
        travel_list = list(reader)

#save file
#inside option "Q" of execute_menu()
#updates to csv file
def save_file():
    with open('places.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(travel_list)




# get users name
def get_name():
    print("Welcome user!")
    user_name = input("What is your name?: ")
    while user_name == "":
        print("Your name cannot be blank!")
        user_name = input("What is your name?: ")
    print("Hello {}!".format(user_name))



# show the menu
def show_menu():
    print("Menu:")
    print("L - List places")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")

#accesses the csv file and formats the display when print
#used in both L and
def list_out_places():
    list_numb = 0
    unvisited_places = 0
    max_length = 0
    for row in travel_list:
        for item in row:
            if len(item)> max_length:
                max_length = len(item)
    for row in travel_list:
        if row[3] == "v":
            list_numb += 1
            print("{:>2}. {:<{}} in {:>{}} priority {}".format(list_numb, row[0],max_length, row[1],max_length, row[2]))
        else:
            list_numb += 1
            print("*{}. {:<{}} in {:>{}} priority {}".format(list_numb, row[0],max_length, row[1],max_length, row[2]))
            unvisited_places += 1
    return unvisited_places

#executes users choice
def execute_menu():
    show_menu()

    menu_choice = input("Please choose one of the above options: ").upper()
    if menu_choice == "L":
        unvisited_places = list_out_places()

        if unvisited_places > 0:
            print("{} places. You still want to visit {} places.".format(unvisited_places, unvisited_places))
        else:
            print("No unvisited places.")

    elif menu_choice == "A":
        place_name = input("What is the place's name?: ")
        while place_name == "":
            print("Please enter a location!")
            place_name = input("What is the place's name?: ")
        addition_list = []
        addition_list.append(place_name)

        place_country = input("What country is this in?: ")
        while place_country == "":
            print("Please enter a location!")
            place_country= input("What country is this in?: ")
        addition_list.append(place_country)

        place_priority = input("What priority would you assign to visiting this location?: ")
        while place_priority != "":
            try:
                val = int(place_priority)
                print("Input number value is: ", val)
                break
            except ValueError:
                print("That's not an number!")
                print("Please key in a number.")
                place_priority = input("What priority would you assign to visiting this location?: ")

        addition_list.append(place_priority)
        addition_list.append("n")
        travel_list.append(addition_list)

    elif menu_choice == "M":
        unvisited_places = list_out_places()
        rows = 0
        if unvisited_places == 0:
            print("There are no more unvisited places.")
        else:
            place_to_edit = input("Which place would you like to mark as visited?: ")
            for item in travel_list:
                rows+=1
                if place_to_edit in item:
                    index_numb = travel_list.index(item)
                    travel_list[index_numb][3] = "v"
                    print("FOUND IT! The list has been updated!")
                    break
                else:
                    print("This is not in row {}.".format(rows))
    elif menu_choice == "Q":
        save_file()
        print("Thank you and goodbye!")
        sys.exit()
    else:
        print("That was an invalid input.")
        execute_menu()

    execute_menu()


def main():
    open_file()
    get_name()
    execute_menu()

main()


from place import Place
