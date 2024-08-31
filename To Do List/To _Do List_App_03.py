import os

TASK_FILE = "tasks.txt"

def load_task():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:

                task, status = line.rsplit(":",1)
                tasks.append((task, status == "complete"))
    return tasks


def save_task(tasks):
    with open(TASK_FILE, "w") as file:
        for task, completed in tasks:
            status = "complete" if completed else "incompleted"
            file.write(f"{task}: [{status}]")



def add_task(tasks):

    new_task = input("Enter Your New Task: ")

    tasks.append((new_task, False))
    print(f"Task {new_task} has been added successfully. \n")


def view_task(tasks):

    if tasks:
        print("\n Your Tasks")
        for i, (task, completed) in enumerate(tasks, 1):
            status = "✔️" if completed else "❌"
            print(f" {i}. {task} {status}")
    else:
        print("No Task Available!")

def complete_task(tasks):
    view_task(tasks)
    try:
        task_num = int(input("Mark As Complete Task: ")) - 1
        if 0 <= task_num < len(tasks):
            task, _ = tasks[task_num]

            tasks[task_num] = (task, True)
            print(f"Task {task} marked as completed.")
        else:
            print("Please Enter Correct task Number>")
    except ValueError:
        print("Invalid Entry: Please Enter Right Task Number!")




def delete_task(tasks):
    view_task(tasks)
    try:
        task_num = int(input("Enter Task Number taht you want to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            remove_task = tasks.pop(task_num)
            print(f" Task {remove_task[0]} deleted successfully.\n")
        else:
            print("Please choose right task number.")
    except ValueError:
        print("Invalid Task Number")


def to_do_list_app():
    tasks = load_task()
    while True:
        print("\nTo Do List APP")
        print("Select Relevant option")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Mark as Complete")
        print("4. Delete Task")
        print("5. Exit!")


        choice = input("Choice an option from 1-5: ").strip()
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

to_do_list_app()


