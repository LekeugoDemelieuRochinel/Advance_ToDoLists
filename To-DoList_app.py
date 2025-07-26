
import json
import os

TASKS_FILE = 'tasks.json'

tasks = []
next_task_id = 1


def load_tasks():
    global tasks
    global next_task_id
    
    try:
        if os.path.exists(TASKS_FILE) and os.path.getsize(TASKS_FILE) > 0:
         with open(TASKS_FILE, "r") as file: 
            # this line of code will create a file to that will allow us to store each task.
            data = json.load(file)
            tasks = data.get('tasks', [])
            
            if tasks:
                max_id = max(tasks['id'] for task in tasks)
                next_task_id = max_id + 1
            else:
                next_task_id = 1
            next_task_id = data.get("next_id", 1)
            print(f"Loaded {len(tasks)} task from({TASKS_FILE} ")
    except FileExistsError:
        # here is if the file doesn't exist yet.
        print(f" '{TASKS_FILE}' not found. Starting with an empty list. ")
        
        # Ensure tasks is empty if file doen't exist
    except json.JSONDecodeError:
        # If the file content is not valide JSON
        print(f"Error decoding JSON from '{TASKS_FILE}'. Starting with an empty lsits ")
        
    except Exception as e:
        # Catch any other unexpected errors during loading
        print(f"An unexpected error occured while loading tasks: {e}")
        
    finally:
        if 'tasks' not in locals():
            tasks = []
            next_task_id = 1
            

# here now we are going with Save tasks function.
# each tasks that we add is going to be save by using this function.
def save_tasks():
    
    data = {
        'tasks': tasks,
        'next_id': next_task_id
    }
        
    try:
        # this will open the file TASKS_FILE so that we can write
        with open(TASKS_FILE, 'w') as file:
            # Dump python data to JSON file
            json.dump(data, file, indent=4)
            print(f"Tasks saved to '{TASKS_FILE}'")
    except Exception as e:
        print(f"Error savaing tasks to '{TASKS_FILE}': {e}")
        
        

# Advance To-Do List Application with data persitence

'''
here is the concept of the project 
Concept: Building on a basic To-Do list, this project introduces data storage (files or a simple database).
'''
# here is the brianstorming of the project

'''
chose the best data structre to store items (here we will chose a list as a data structure)
list because we can play with item like add, remove, change and all of this are supported by a list
'''
# phase 1: core Functionality(in-memory)

                # Understanding the Problem: here is what to do

# 1- Task Each task needs at least a description, it might also need a status 
# 2- Storage how will we store multiple tasks in our program? A list seems appropriate, and each task can be a dictionary within that list
# 3 - operations (add a new task, View all tasks, mark a task as complete, Delete a task, Exit the application)

                    #    now let start 
                    
# here is the list to hole all the task
# and each item in tis list will be a dictionary just because dictionary allows us to store multiple pieces of information

#  here we have the list that hold all tasks

# now we assign unique IDs to tasks
# this varaable is just to give each task aunique ID

# now the function to  add a  new task and the function is taking one parameter 
def add_task(task_name):
    global next_task_id
    
    
    # this is a dictionary that discrib the each task.
    task = {
        'id': next_task_id,
        'description': task_name,
        'completed': False
    }
    
    tasks.append(task)
    
    next_task_id += 1
    
    # print(f"This is the task add call {task_name} and the id of the task is {task['id']}")

# now that we hav finish to add task let now view each task in the tasks

def view_tasks():
    # ths if stement check if there's no task in the list, and if yes it display the message and return 
    if not tasks:
        print("sorry you have not yet add a new task, the task list is empty! \n")
        return
    
    print("\n Start ....this is we have in the To Do List \n")
        
    for task in tasks:
        # this line hare to be search 
        
        #  in the case of this logic we will change it for the better readability and debuging.
        # status = "/" if task["completed"] else " "
        if task["completed"]:
            status = "/"
        else:
            status = " "
        
        print(f"{status} ID: {task['id']} - {task['description']} \n")
        
        
# here is the function to  Mark Task as complete function
def mark_task_complete(task_id):
    
    # here we create a variable found to track if we successfuly found the task.
    found = False
    # and here we iterate througth our list of tasks
    for task in tasks:
        # an we compare the ID of the current task with the task_id provide by the user
        if task['id'] == task_id:
        #   if a match is found, we modify the completed value within that specific task dictionary
            task['completed'] = True
            print(f"Task ID {task_id} maked as complete.")
            found = True
            # by using break we go out of the for loop
            break 
        
        if not found:
            print(f"Error: Task with ID {task_id} not found!")
             
# okay this two line down will be compaire with the two task 
# and we will have three error messages and one good message


# now let try to delet a task in the list

def delete_task(item_id):
    
    for task in tasks:
        if task['id'] == item_id:
              tasks.remove(task)
              print('\n >> Updated Task List << \n')
              print(f"here are the reste of task that we have {tasks}")
        else:
            print("Sorry that the list doesn't have that task!")
   
   
# here is the main menu that containe all the function call and any choice made by the user. 
# and to interact with afunction you have a choice from 1 to 5 as show in the code below.  
def main_menu():
    
    print("Welcome To Rochinel To Do List!")
    # Load tasks at the start of the application
    load_tasks()

    while True:
        
        print("\n--- To Do List Menu ---")
        print("\n 1. Add Task \n 2. View Tasks \n 3. Mark Task Complete \n 4. Delete Task \n 5. Exit")
        print("____________Start______________-")
        
        
        choice = int(input("Enter you Choice: "))
        
        if choice == 1:
            descrip = input("Enter you task description that you want to store in the list.")
            add_task(descrip)
            
        elif choice == 2:
            view_tasks()
            
        elif choice == 3:
            try:
                task_id = int(input("Enter an ID of the task to mark complete: "))
                mark_task_complete(task_id)
            except ValueError:
                print("Invalid input: the one that you have enter is not a number.")
                
        elif choice == 4:
            try:
                task_id = int(input("Enter the ID of that task to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Please this is not a number. ")
                
        elif choice == 5:
            print("Exiting To-Do List. Goodbye!")
            save_tasks()
            break
        else:
            print("Ivalide choice. Please try again.")

# Call the main menu function to start the application 

if __name__ == "__main__":
    main_menu()


            
   
    
    
    


    

    
    


