import os


def load_tasks():
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
    return tasks


def save_tasks(tasks: list):
    with open("tasks.txt", "w") as file:
        file.writelines(tasks)


def add_task(task: list):
    tasks = load_tasks()
    tasks.append(task + "\n")
    save_tasks(tasks)
    print(f"Task added: {task}")


def remove_task(task_number):
    tasks = load_tasks()
    if len(tasks) >= task_number:
        task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task removed: {task.strip()}")
    else:
        print("Invalid task number.")


def view_tasks():
    tasks = load_tasks()
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i} - {task.strip()}")
    else:
        print("No tasks found.")


def exit_program():
    print("Exiting...")
    exit(0)


def main():
    while True:
        print("\n")
        print("To-Do List")
        print("1 - Add task")
        print("2 - Remove task")
        print("3 - View tasks")
        print("4 - Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            task_number = int(input("Enter task number: "))
            remove_task(task_number)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
