import socket
import getpass
import os

def show_sysinfo():
  print("=== SYSTEM INFORMATION ===")
  print(f'Hostname: {socket.hostname()}')
  print(f'User: {getpass.getuser()}')
  print(f'Current directory: {os.getcwd()}')
