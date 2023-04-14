import os

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("\n" + "------------------------------------" + "\n")


def remove_task(task):
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    with open("tasks.txt", "w") as file:
        for line in tasks:
            if line.strip("\n") != task:
                file.write(line)
    print("\n" + "------------------------------------" + "\n")


def show_tasks():
    if not os.path.exists("tasks.txt"):
        print("\n" + "No tasks found")
        print("\n"+"------------------------------------"+"\n")

        return
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    for task in tasks:
        print("\n" + task.strip("\n"))
    print("\n"+"------------------------------------"+"\n")

def main():
    while True:
        print("\t" + "1. Add task")
        print("\t" + "2. Remove task")
        print("\t" + "3. Show tasks")
        print("\t" + "4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter task: ")
            remove_task(task)
        elif choice == "3":
            show_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice")
            print("\n" + "------------------------------------" + "\n")


if __name__ == "__main__":
    main()