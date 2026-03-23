import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Show tasks
def show_tasks(tasks):
    print("\n--- Your Tasks ---")
    if not tasks:
        print("No tasks available.")
        return

    for i, t in enumerate(tasks, start=1):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {t['task']} | {t['priority']} | Due: {t['due_date']} [{status}]")


# Add task
def add_task(tasks):
    task = input("Enter task: ")
    priority = input("Priority (High/Medium/Low): ")
    due_date = input("Due date (YYYY-MM-DD): ")

    tasks.append({
        "task": task,
        "priority": priority,
        "due_date": due_date,
        "done": False
    })

    print("Task added!")


# Delete task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        print(f"Deleted: {removed['task']}")
    except:
        print("Invalid input!")


# Mark complete
def mark_done(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number: "))
        tasks[num - 1]["done"] = True
        print("Task completed!")
    except:
        print("Invalid input!")


# Edit task
def edit_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to edit: "))
        t = tasks[num - 1]

        print("Leave blank to keep old value")

        new_task = input(f"Task ({t['task']}): ") or t["task"]
        new_priority = input(f"Priority ({t['priority']}): ") or t["priority"]
        new_due = input(f"Due date ({t['due_date']}): ") or t["due_date"]

        t.update({
            "task": new_task,
            "priority": new_priority,
            "due_date": new_due
        })

        print("Task updated!")

    except:
        print("Invalid input!")


# Search tasks
def search_tasks(tasks):
    keyword = input("Enter keyword: ").lower()
    results = [t for t in tasks if keyword in t["task"].lower()]

    print("\n--- Search Results ---")
    if not results:
        print("No matching tasks.")
    else:
        for t in results:
            status = "✅" if t["done"] else "❌"
            print(f"{t['task']} | {t['priority']} | {t['due_date']} [{status}]")


# Main
tasks = load_tasks()

while True:
    print("\n==== ADVANCED TO-DO LIST ====")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Edit Task")
    print("6. Search Tasks")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_tasks(tasks)

    elif choice == "2":
        add_task(tasks)
        save_tasks(tasks)

    elif choice == "3":
        delete_task(tasks)
        save_tasks(tasks)

    elif choice == "4":
        mark_done(tasks)
        save_tasks(tasks)

    elif choice == "5":
        edit_task(tasks)
        save_tasks(tasks)

    elif choice == "6":
        search_tasks(tasks)

    elif choice == "7":
        save_tasks(tasks)
        print("Saved. Exiting...")
        break

    else:
        print("Invalid choice!")