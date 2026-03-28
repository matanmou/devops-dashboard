def check_log():
"""
that func check logs from user input file name and check if there is logs with errors
"""
  print("=== CHECK LOGS ===")
  file_name = input("Please enter file name: ") #get from user file name
  try: 
    with open(file_name, 'r') as file: #open file
      i = 0 #init counter to count errors
      for line in file: #run all lines in the file
        if "ERROR" in line: 
          print(line)
          i += 1
      if i == 0: #to write there is no errors after all
        print("There is no Error in the file")
  except FileNotFoundError: #if user type file name that doesnwt exsist
    print('File not found!')
