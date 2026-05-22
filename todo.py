# todo.py
# Simple GitHub-ready To-Do App in Python

import os

FILE_NAME = "tasks.txt"


def load_tasks():
    """Load tasks from file."""
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        tasks = [line.strip() for line in file.readlines()]

    return tasks


def save_tasks(tasks):
    """Save tasks to file."""
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\n===== YOUR TASKS =====")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    print()


def add_task(tasks):
    """Add a new task."""
    task = input("Enter new task: ")

    if task.strip() == "":
        print("Task cannot be empty.\n")
        return

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!\n")


def delete_task(tasks):
    """Delete a task."""
    show_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed_task = tasks.pop(number - 1)
            save_tasks(tasks)

            print(f"Deleted task: {removed_task}\n")

        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def main():
    tasks = load_tasks()

    while True:
        print("===== TO-DO APP =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
