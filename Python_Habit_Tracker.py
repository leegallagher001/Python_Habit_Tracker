# Python Habit Tracker - Lee Gallagher

# A console application that allows a user to add a habit, mark a habit as completed and view the progress of a particular habit
# Built using Python and JSON

# (0) Imports

import json
import os

database = "habits.json" # specifies the .json file that we'll be using to hold our habit data

# (1) Define Functions

def addHabit():  # Menu Option 1

    name = input("Enter the name of the new habit: ")
    try:
        with open(database, 'r') as f:
            habits = json.load(f)
    except json.JSONDecodeError:

        habits = []

    new_habit = {
        "name": name
    }

    habits.append(new_habit)

    with open(database, 'w') as f:
        json.dump(habits, f, indent=4)

def showHabits():  # Menu Option 3 (will be a work in progress for a LONG time)

   try:
       with open(database, 'r') as f:
           habits = json.load(f)
   except (FileNotFoundError, json.JSONDecodeError):
       print("No habits found.")
       return

   if not habits:
       print("No habits found.")
   else:
       print("Your Habits:")
       for i, habit in enumerate(habits, start=1):
           print(f"{i}. {habit['name']}")

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

        addHabit()

        print("Habbit Added: ", )
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