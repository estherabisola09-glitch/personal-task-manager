from task_manager import (
    load_tasks,
    save_tasks,
    add_task,
    complete_task,
    delete_task,
    format_tasks,
)


def show_menu():
    print("\n=== Task Manager ===")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task complete")
    print("4. Delete a task")
    print("5. Exit")


def ask_for_id(prompt):
    """Ask for a task id. Returns an int, or None if the input is not a number."""
    raw = input(prompt).strip()
    try:
        return int(raw)
    except ValueError:
        print("Please enter a number.")
        return None


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("Task title: ")
            success, message = add_task(tasks, title)
            print(message)
            if success:
                save_tasks(tasks)

        elif choice == "2":
            print(format_tasks(tasks))

        elif choice == "3":
            task_id = ask_for_id("Task id to complete: ")
            if task_id is not None:
                success, message = complete_task(tasks, task_id)
                print(message)
                if success:
                    save_tasks(tasks)

        elif choice == "4":
            task_id = ask_for_id("Task id to delete: ")
            if task_id is not None:
                success, message = delete_task(tasks, task_id)
                print(message)
                if success:
                    save_tasks(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()