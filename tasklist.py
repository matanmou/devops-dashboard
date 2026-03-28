def manage_tasks():
 tasks_list = []
 print("=== TASK MANAGER ===")
 while True:
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
  task  = input("Enter new task: ")
  task_list.append(task)
  return task_list

def view_all_tasks(task_list):
  print("All tasks list:")
  try:
    if len(task_list) > 0:
     i = 0
     for task in task_list:
      print(f'[{i+1}] - {task}')
    else:
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
  print("=== Remove Task ===")
  is_not_empty = view_all_tasks(task_list)
  if is_not_empty:
   try:
     user_choise = int(input("Which task to remove (please enter task number): "))
     task_list.pop(user_choise-1)
     print("Successfully removed!")
     return task_list
   except ValueError:
     print("Wrong Input! You should enter an number!")
     return task_list
   except IndexError:
     print("You picked wrong number! please choose from the list!")
     return task_list
  else:
   return task_list
