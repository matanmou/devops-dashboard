def check_log():
  print("=== CHECK LOGS ===")
  file_name = input("Please enter file name: ")
  try:
    with open(file_name, 'r') as file:
      for line in file:
        if "ERROR" in line:
          print(line)
  except FileNotFoundError:
    print('File not found!')
