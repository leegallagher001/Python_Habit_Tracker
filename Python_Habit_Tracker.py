# Python Habit Tracker - Lee Gallagher

# A console application that allows a user to add a habit, mark a habit as completed and view the progress of a particular habit
# Built using Python and JSON

# (0) Imports

import json
import os

database = "habits.json" # specifies the .json file that we'll be using to hold our habit data

# (1) Define Functions

def addHabit(habits):  # Menu Option 1
    global database
    with open(database, "a") as f:
        json.dump(habits, f, indent=2)
        f.write('\n')
        f.write('\n')

def showHabits():  # Menu Option 3 (will be a work in progress for a LONG time)
    names = []
    global database
    if os.path.exists(database):
        with open(database, "r") as f:
            for key in f:
                for name in key:
                    names.append(name)
                    print(name)

    else:
        print("No file present")

# (2) Opening Statement

print("Hello, and welcome to the Habit Tracker!")
print("\n")
print("This program allows a user to add, complete and track daily habits.")
print("\n")

# (3) Main Menu

print("--- Habit Tracker ---")
print("  1. Add Habit")
print("  2. Mark Habit as Done")
print("  3. View Progress")
print("  4. Exit")

# (4) Choose Menu Item

print("\n")
menuChoice = int(input("Choose Your Option: "))

# (5) Activate Functionality

while menuChoice != 4:

    if menuChoice == 1:
        name = input("Which habit would you like to add?: ")
        lowername = name.lower()
        key = lowername.replace(" ", "_")

        habits =  { key: {
                "name": name,
                "log": [],
              }}

        addHabit(habits)

        print("Habbit Added: ", name)
        print("\n")
        menuChoice = int(input("Select Another Option: "))
        
    elif menuChoice == 2:
        print("Section In Progress")
        print("\n")
        menuChoice = int(input("Select Another Option: "))

    elif menuChoice == 3:
        showHabits()
        print("\n")
        menuChoice = int(input("Select Another Option: "))

    else:
        print("Invalid Choice. Please Try Again.")
        print("\n")
        menuChoice = int(input("Select Another Option: "))

print("Thank you for using the Habit Tracker!")
print("\n")
print("Keep the good habits up!")
print("\n")
input("Press 'ENTER' to exit the program.")