
tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks available!")
        return

    print("\n====== YOUR TASKS ======")

    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['name']} - {status}")


def add_task():
    name = input("Enter your task: ")

    if name.strip():
        tasks.append({
            "name": name,
            "completed": False
        })
        print("Task added successfully!")
    else:
        print("Task cannot be empty!")


def complete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task completed!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Deleted: {removed['name']}")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


while True:
    print("\n====== TO-DO LIST MANAGER ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye! Keep being productive.")
        break
    else:
        print("Invalid choice! Try again.")
