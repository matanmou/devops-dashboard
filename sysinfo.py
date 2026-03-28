import socket
import getpass
import os

def show_sysinfo():
"""
that func show current system info
"""
  print("=== SYSTEM INFORMATION ===")
  print(f'Hostname: {socket.gethostname()}')
  print(f'User: {getpass.getuser()}')
  print(f'Current directory: {os.getcwd()}')
