import os
TASKS_FILE = "tasks.txt"

# Function for Loading All tasks
def load_task():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                task, status = line.strip().rsplit(":", 1)
                tasks.append((task, status == "complete"))
    return tasks




# Function To save Taks
def save_task(tasks):
    with open(TASKS_FILE, "w") as file:
        for task, completed in tasks:
            status = "complete" if completed else "incomplete"
            file.write(f" {task}: {status}\n")


# Fucntion for adding Tasks
def add_task(tasks):
    new_task = input(" Enter Your New Task: ")
    tasks.append((new_task, False))
    print(f" Your New Task '{new_task}' has been added Successfully!\n")

# Function for View Tasks
def view_task(tasks):
    if tasks:
        print("\nYour Tasks")
        for i, (task, completed) in enumerate(tasks, 1):
            status = "✔️" if completed else "❌"
            print(f"{i}. {task}: {status} ")
    else:
        print("No Task Available!")
def complete_task(tasks):
    try:
        complete_task_num = int(input("Enter the Task Number to Mark it As Complete: ")) - 1
        if 0 <= complete_task_num < len(tasks):
            task, _ = tasks[complete_task_num]
            tasks[complete_task_num] = (task, True)
            print(f"Task {complete_task_num}: {task} Marked as Complete.")
        else:
            print(f"{complete_task_num} does not exist.")
    except ValueError:
        print(f" {complete_task_num} is not task number: Please enter task number. ")

def delete_task(tasks):
    try:
        task_num = int(input("Enter Tssk Number that you want to delete: ")) -1

        if 0 <= task_num < len(tasks):
            remove_task = tasks.pop(task_num)
            print(f" Your Task {task_num}: {remove_task[0]} has been removed." )

        else:
            print("Enter Your Correct Task Number.")
    except ValueError:
        print("It is Not Task Number.")

# TO Do List Application
def to_do_app():
    tasks = load_task()

    print("\nTO DO APPLICATION\n")
    print("\nSelect Your Operation")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Mark Task As Complete ")
    print("4. Delete Task")
    print("5. Exit")
    
       
    while True:

        choice = input("Enter option from 1-5:  ")
        if choice in ["1", "2", "3", "4", "5"]:
            if choice == "1":
                add_task(tasks)
                save_task(tasks)
            elif choice == "2":
                view_task(tasks)
            elif choice == "3":
                complete_task(tasks)
                save_task(tasks)
            elif choice == "4":
                delete_task(tasks)
                save_task(tasks)
            elif choice == "5":
                print("Goodbye.")
                break
        else: 
            print("You choose a wrong Number.")

if __name__ == "__main__":
    to_do_app()