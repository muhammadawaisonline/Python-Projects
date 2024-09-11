import os
TASKS_FILE = "tasks.txt"

# Function for View Task
def load_task():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                task, status = line.strip().rsplit(":", 1)
                tasks.append((task,status))
    return tasks



# Fuction to save task
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task, completed in tasks:
            status = "complete" if completed else "incomplete"
            file.write(f"{task}: {status}\n")

# Function to add tasks
def add_task(tasks):
    new_task = input("Enter your new task: ")

    tasks.append((new_task, False))
    print(f"\n your new task '{new_task}' has been added successfully! ")

def view_task(tasks):
    if tasks:
        print("\n Your Tasks ")
        for i, (task, completed) in enumerate(tasks, 1):
            status = "✔️" if completed else "❌"
            print(f"{i}. {task}: {status}")
    else:
        print("You haven't Enter any Task: Please add Your Task First ")

# Function to nark as complete task
def complete_task(tasks):
    try:
        task_num = int(input("Enter your task number that you have been completed: ")) -1
        if 0 <= task_num < len(tasks):
            task, _ = tasks[task_num]
            tasks[task_num] = (task, True)
            print(f"{task_num}. {task} marked as completed.")
        else:
            print(f"{task_num} is not exist.")
    except ValueError:
        print(f"{task_num} is not task number.")
def delete_task(tasks):
    view_task(tasks)
    try:
        task_num = int(input("Enter Your Task Number that you want to delete: ")) - 1

        if 0 <= task_num < len(tasks):
            remove_task = tasks.pop(task_num)
            print(f"your task '{remove_task[0]}' has been removedb successfully.")
            view_task(tasks)
        else:
            print("You Choose wrong task Number: Please select correct task number>")
    except ValueError:
        print(f"{task_num} is not task number: Please Choose task right number.")

# TO DO Application
def to_do_app():
    tasks = load_task()
    print("\nTo Do Application\n")
    print("\n Select option")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Mark as Complete")
    print("4. Delete Task")
    print("5. Exit")

    while True:
        choice = input("Enter option from 1 to 5 (1-5): ")
        if choice in ["1", "2", "3", "4", "5"]:
            if choice == "1":
                add_task(tasks)
                save_tasks(tasks)
            elif choice == "2":
                view_task(tasks)
            elif choice == "3":
                complete_task(tasks)
                save_tasks(tasks)
            elif choice == "4":
                delete_task(tasks)
                save_tasks(tasks)
            elif choice == "5":
                print("Goodbye.")
                break
            else:
                print("Please Choose Right Option.")
        else:
            print("Invalid Selction: Choose 1-5:")

if __name__ == "__main__":
    to_do_app()