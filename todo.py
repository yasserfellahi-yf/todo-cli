tasks = []

def show_menu():
    print("\n=== Todo CLI ===")
    print("1. Add task")
    print("2. List tasks")
    print("3. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added!")

def list_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()