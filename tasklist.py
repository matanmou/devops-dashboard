def manage_tasks():
  tasks_list = []
  print("=== TASK MANAGER ===")
  try:
    user_choise = int(input("""[1] Add a task
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
  tasks_list.append(task)
  return task_list

def view_all_tasks(task_list):
  print("All tasks list:")
  i = 0
  for task in task_list:
    print(f'[{i+1} - {task}')
  
def remove_task(task_list):
  print("=== Remove Task ===")
  view_all_tasks(task_list)
  try:
    user_choise = int(input("Which task to remove (please enter task number): "))
    task_list.pop(user_choise-1)
    print("Successfully removed!")
  except ValueError:
    print("Wrong Input! You should enter an number!")
  except IndexError:
    print("You picked wrong number! please choose from the list!")

