import os

TODO_FILE = "todo.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter the task to add: ").strip()
    if task:
        tasks.append(task)
        print(f'"{task}" has been added.')
    else:
        print("No task was added.")

def remove_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f'"{removed}" has been removed.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def edit_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the task number to edit: ")) - 1
            if 0 <= index < len(tasks):
                new_task = input("Enter the new task: ").strip()
                if new_task:
                    old_task = tasks[index]
                    tasks[index] = new_task
                    print(f'"{old_task}" updated to "{new_task}".')
                else:
                    print("No change made.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nMenu:")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Edit Task")
        print("5. Save and Exit")
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            edit_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()
