import os

# File to store tasks
TASKS_FILE = "tasks.txt"

# Function to load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                if len(parts) == 2:
                    task, status = parts
                    tasks.append((task, status == 'complete'))
    return tasks

# Function to save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task, completed in tasks:
            status = 'complete' if completed else 'incomplete'
            file.write(f"{task}:{status}\n")

# Function to add a task
def add_task(tasks):
    task = input("Enter a new task: ").strip()
    tasks.append((task, False))
    print(f"Task '{task}' added successfully.\n")

# Function to view all tasks
def view_tasks(tasks):
    if tasks:
        print("\nYour tasks:")
        for i, (task, completed) in enumerate(tasks, 1):
            status = "✔" if completed else "✘"
            print(f"{i}. {task} [{status}]")
    else:
        print("No tasks available.\n")

# Function to mark a task as complete
def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= task_num < len(tasks):
            task, _ = tasks[task_num]
            tasks[task_num] = (task, True)
            print(f"Task '{task}' marked as complete.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"Task '{removed_task[0]}' deleted successfully.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Main function for the to-do list application
def todo_list_app():
    tasks = load_tasks()  # Load existing tasks from file

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            add_task(tasks)
            save_tasks(tasks)  # Save after adding
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
            save_tasks(tasks)  # Save after marking as complete
        elif choice == '4':
            delete_task(tasks)
            save_tasks(tasks)  # Save after deleting
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.\n")

# Run the To-Do List application
todo_list_app()
