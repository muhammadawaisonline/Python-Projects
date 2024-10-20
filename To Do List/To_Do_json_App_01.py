import json

TODO_FILE = 'todo.json'

# Load tasks from file
def load_tasks():
    try:
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks, task_description):
    tasks.append({"description": task_description, "completed": False})
    save_tasks(tasks)
    print(f"Task '{task_description}' added.")

# Mark task as completed
def complete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_index]['description']}' marked as completed.")
    else:
        print("Invalid task index.")

# Delete a task
def delete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{task['description']}' deleted.")
    else:
        print("Invalid task index.")

# Display all tasks
def display_tasks(tasks):
    if tasks:
        print("To-Do List:")
        for idx, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{idx + 1}. {task['description']} - {status}")
    else:
        print("No tasks available.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List")
        print("1. Add task")
        print("2. Mark task as completed")
        print("3. Delete task")
        print("4. View tasks")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            task_description = input("Enter task description: ")
            add_task(tasks, task_description)
        elif choice == "2":
            task_index = int(input("Enter task number to mark as completed: ")) - 1
            complete_task(tasks, task_index)
        elif choice == "3":
            task_index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, task_index)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
