def display_menu():
    # Write Display message at the Top Of the APP
    print("\n ..........Simple To Do List App .......... \n")
    print("\n1. View Task ")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit Application")
    


# Function for Adding New Task
def add_task(to_do_list):
    new_task = input(" Enter Your New task: ")
# Udating list with New Task
    to_do_list.append(new_task)
    return view_tasks(to_do_list)


# Function for Display Tasks
def view_tasks(to_do_list):
# Check User Input is valid
    for index, task in enumerate(to_do_list, 1):
        print(f" {index}.  {task}")

# Function for Removing Task Frtom List
def remove_task(to_do_list):
    task_num = int(input("Enter Your Task Number that You Want to Remove: "))
# Check User Input is Valid
    try:
        if 1 <= task_num <= len(to_do_list):
            to_do_list.pop(task_num -1)
            print(f" Task No.{task_num} has been removed.")
        else:
            print("Your Number is invalid: Choose Existing Task")
    except ValueError:
        print("Your Task Does not Exist: Choose Right Task Number.")


# Function For To Do List Application
def to_do_list_app():
# Initilazing To Do list to hold tasks
    display_menu()
    to_do_list = []
    while True:
        
        user_input = input(" Choose Number from 1 to 4 (1-4): ")
        
        if user_input == "1":
            print(" Your Tasks")
            view_tasks(to_do_list)
        elif user_input == "2":
            add_task(to_do_list)
        elif user_input == "3":
            remove_task(to_do_list)
        elif user_input == "4":
            print("Your Application has been Closed! ")
            break
        else:
            print("You Choose Invalid Number")

if __name__ == "__main__":
    to_do_list_app()