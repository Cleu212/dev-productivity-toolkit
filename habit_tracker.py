import json
import os
from datetime import datetime

FILE_NAME = "habits.json"

def load_habits():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_habits(habits):
    with open(FILE_NAME, "w") as file:
        json.dump(habits, file, indent=4)

def show_habits(habits):
    if not habits:
        print("No habits found.")
        return

    print("\nYour Habits:")
    for habit, dates in habits.items():
        print(f"- {habit} (Completed {len(dates)} times)")

def add_habit(habits):
    habit = input("Enter new habit name: ").strip()
    if habit in habits:
        print("Habit already exists.")
    else:
        habits[habit] = []
        save_habits(habits)
        print("Habit added successfully!")

def complete_habit(habits):
    habit = input("Enter habit name to mark as completed: ").strip()
    if habit not in habits:
        print("Habit not found.")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    if today in habits[habit]:
        print("Habit already completed today.")
    else:
        habits[habit].append(today)
        save_habits(habits)
        print("Habit marked as completed!")

def main():
    habits = load_habits()

    while True:
        print("\nHabit Tracker")
        print("1 - Show habits")
        print("2 - Add habit")
        print("3 - Complete habit")
        print("4 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_habits(habits)
        elif choice == "2":
            add_habit(habits)
        elif choice == "3":
            complete_habit(habits)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
  def show_habits(habits):
    if not habits:
        print("No habits found.")
        return

    print("\nYour Habits:")
    for habit, dates in habits.items():
        print(f"\n- {habit} (Completed {len(dates)} times)")
        if dates:
            print("  Completed on:")
            for date in dates:
                print(f"    • {date}")
        else:
            print("  Not completed yet.")

