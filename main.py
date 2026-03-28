import sysinfo
import logcheck
import tasklist

while True:
        user_choise = int(input("""
MAIN MENU
---------------
[1] System Info
[2] Log Checker
[3] Task List
[0] Exit
---------------
Enrer your choise: """))

        if user_choise == 1:
                sysinfo.show_sysinfo()
        elif user_choise == 2:
                logcheck.check_log()
        elif user_choise == 3:
                print("Comming soon...")
        elif user_choise == 0:
                break
        else:
                print("Wrong Input!")
