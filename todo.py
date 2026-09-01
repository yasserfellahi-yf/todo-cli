def main():
    print("=== Todo CLI ===")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")
    print()
    choice = input("Enter your choice: ")
    print(f"You selected: {choice}")

if __name__ == "__main__":
    main()