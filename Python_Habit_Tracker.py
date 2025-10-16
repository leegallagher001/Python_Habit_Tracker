# Python Habit Tracker - Lee Gallagher

# A console application that allows a user to add a habit, mark a habit as completed and view the progress of a particular habit
# Built using Python and JSON

# (0) Imports

import json
import os
import datetime

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
        "name": name,
        "log": []
    }

    habits.append(new_habit)

    with open(database, 'w') as f:
        json.dump(habits, f, indent=4)

def markHabitAsDone():  # Menu Option 2 - Work In Progress

    # Lots of comments on this one as this problem took me a while to understand as I am a beginner to using JSON with Python

    today = datetime.date.today().isoformat() # stores today's date in a variable to be appended later

    habit_to_log = input("Please enter the name of habit to log today: ") # user enters habit name

    with open(database, 'r') as f: # allows Python to read the file and manipulate it
        habits = json.load(f)

    for habit in habits: # accesses individual 'habit' dictionaries from the overall habits JSON file
        if habit_to_log == habit["name"]: # finds the specific habit of the name the user is looking for
            if today in habit["log"]: # checks to make sure the habit hasn't been previously logged today
                print("Already logged today!")
            else:
                habit["log"].append(today) # adds today's date to the 'log' value of the dictionary

    with open(database, 'w') as f: # writes the updated 'habits' dictionary to the JSON file
        json.dump(habits, f, indent=4)

def showHabits():  # Menu Option 3

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
        
        markHabitAsDone()

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