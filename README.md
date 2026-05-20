# python_todo
to do list
# ==========================================
# Simple To-Do List App in Python
# ==========================================

tasks = []


def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")


while True:
    show_menu()

    choice = input("Enter your choice (1-4): ")

    # View Tasks
    if choice == "1":
        if len(tasks) == 0:
            print("\nNo tasks available.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    # Add Task
    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print(f"Task '{task}' added successfully!")

    # Remove Task
    elif choice == "3":
        if len(tasks) == 0:
            print("\nNo tasks to remove.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                task_number = int(input("Enter task number to remove: "))

                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Task '{removed_task}' removed successfully!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    # Exit
    elif choice == "4":
        print("Exiting To-Do List App...")
        break

    # Invalid Input
    else:
        print("Invalid choice. Please try again.")
