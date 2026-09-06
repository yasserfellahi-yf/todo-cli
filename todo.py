import json

FILENAME = "tasks.json"
tasks = []

def load_tasks():
    global tasks
    try:
        with open(FILENAME, "r") as file:
            tasks = json.load(file)
    except:
        tasks = []

def save_tasks():
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=2)

def show_menu():
    print("\n=== Todo CLI ===")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Clear completed tasks")
    print("6. Exit")

def add_task():
    task = input("Enter the task: ").strip()
    if task == "":
        print("Task cannot be empty.")
        return
    tasks.append({"task": task, "done": False})
    save_tasks()
    print("Task added successfully!")

def list_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
        return

    print("\nYour tasks:")
    print("-" * 30)
    for i, item in enumerate(tasks, 1):
        status = "[x]" if item["done"] else "[ ]"
        print(f"{i}. {status} {item['task']}")
    print("-" * 30)

def mark_done():
    list_tasks()
    if len(tasks) == 0:
        return
    try:
        number = int(input("Enter task number to mark as done: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            save_tasks()
            print("Task marked as done!")
        else:
            print("Invalid number.")
    except:
        print("Please enter a valid number.")

def delete_task():
    list_tasks()
    if len(tasks) == 0:
        return
    try:
        number = int(input("Enter task number to delete: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks()
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid number.")
    except:
        print("Please enter a valid number.")

def clear_completed():
    global tasks
    before = len(tasks)
    tasks = [item for item in tasks if not item["done"]]
    after = len(tasks)
    save_tasks()
    print(f"Cleared {before - after} completed task(s).")

def main():
    load_tasks()
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            clear_completed()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()