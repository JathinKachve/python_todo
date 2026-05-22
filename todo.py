# Simple To-Do App in Python

TASKS_FILE = "tasks.txt"


def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print()


def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")


def delete_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed}\n")
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
