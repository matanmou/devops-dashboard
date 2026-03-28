#this module is task manager for devops dashboard
def manage_tasks():
"""
task manager menu
"""
 tasks_list = [] #init the task list
 print("=== TASK MANAGER ===")
 while True: #run till user choose to exit
  try:
   user_choise = int(input("""\n[1] Add a task
[2] View all tasks
[3] Remove a task
[0] Return to main menu
Enter your chiose: """))
   if user_choise == 1:
    tasks_list = add_task(tasks_list)
   elif user_choise == 2:
    view_all_tasks(tasks_list)
   elif user_choise == 3:
    tasks_list = remove_task(tasks_list)
   elif user_choise == 0:
    return
   else:
    print("You picked wrong number! please choose from the list!")
  except ValueError:
   print("Wrong Input! You should enter an number!")

def add_task(task_list):
"""
add user's task to task list

Parameters:
  task_list (list): task list

Return:
  (list): the new task ist with the new task"
"""
  task  = input("Enter new task: ")
  task_list.append(task)
  return task_list

def view_all_tasks(task_list):
"""
view at all the tasks in task list in a list with numbers

Parameters:
  task_list (list): task list

Return:
  (Boolean): if the list is empty or not"
"""
  print("All tasks list:")
  try:
    if len(task_list) > 0: #if the list is not empty
     i = 0
     for task in task_list:
      print(f'[{i+1}] - {task}') #print task
    else: #if the list is empty
      print("The list is empty!")
      return False
  except AttributeError:
    print("The list is empty!")
    return False
  except TypeError:
    print("The list is empty!")
    return False
  return True

def remove_task(task_list):
"""
remove task from task list

Parameters:
  task_list (list): task list

Return:
  (list): the new task list without the task that user choose"
"""
  print("=== Remove Task ===")
  is_not_empty = view_all_tasks(task_list) #show task list
  if is_not_empty: #if the list is not empty proccess to remove 
   try:
     user_choise = int(input("Which task to remove (please enter task number): "))
     task_list.pop(user_choise-1) #the remove
     print("Successfully removed!")
     return task_list
   except ValueError:
     print("Wrong Input! You should enter an number!")
     return task_list
   except IndexError:
     print("You picked wrong number! please choose from the list!")
     return task_list
  else: #if the list is empty, return the empty list
   return task_list
