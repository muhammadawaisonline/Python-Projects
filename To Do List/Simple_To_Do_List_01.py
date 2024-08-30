
# fuction to display the manue 
def display_manue():
    print("\n .....Simple To Do List..... ")
    print("1. View To Do List ")
    print("2. Add Task")
    print("3. Remove task")
    print("4. Exit")

# Function to View the To Do List
def view_task(to_do_list):
# Check if the list is empty
    if not to_do_list:
        print("Your To do list is Empty")
    else:
        print("\n To Do List")
#        Enumerate syart from 1
        for indx, task in enumerate(to_do_list, 1):
            print(f" {indx}. {task}")

#   Function to add task in the list
def add_task(to_do_list):
    new_task = input("Add New task: ")
#   append task to the list
    to_do_list.append(new_task)
    print(f" {new_task}     (task has been added to your new list)")

# Function to remove task from the list
def remove_task(to_do_list):
#   First Show the Current Task
    view_task(to_do_list)
    try:    
        task_num: int = int(input("\nEnter the number of task that you want to remove:  ")) 
        if 1 <= task_num <= len(to_do_list):
#   Remove Task at specified index
            remove_task = to_do_list.pop(task_num - 1)
            print(f" {task_num}. {remove_task} has been removed from your list")

        else:
            print("Invalid Task Number")
    except ValueError:
        print("Please Enter Valid Number.")
#   Main Function to run To Do List Application
def to_do_list_application():
#   Initialize an empty To Do list to hold task
    to_do_list = []
#   Infinite Loop For the manue
    while True:
        display_manue()
        choice = input(" Choose an Option (1-4): ")
        if choice == "1":
            #view task
            view_task(to_do_list)
        elif choice == "2":
            #Add task
            add_task(to_do_list)
        elif choice == "3":
         # Remove Task
            remove_task(to_do_list)
        # Exit the Application
        elif choice == "4":
            print("Exiting the To Do List App. Goodbye")
            break
        else:
            print("Invalid Choice: Please Choose a valid Number (1-4): ")
to_do_list_application()