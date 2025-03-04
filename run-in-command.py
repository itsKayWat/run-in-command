import os
import winreg
import sys
import ctypes
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def add_context_menu():
    try:
        # Create the main key for .py files
        key_path = r"Python.File\shell\RunInCommand"
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path)
        winreg.SetValue(key, "", winreg.REG_SZ, "Run in Command")
        
        # Create the command key
        command_key = winreg.CreateKey(key, "command")
        
        # Command to open cmd in the file's directory and run the Python file
        command = 'cmd.exe /K "cd /d "%L" & python "%1""'
        winreg.SetValue(command_key, "", winreg.REG_SZ, command)
        
        # Close the keys
        winreg.CloseKey(command_key)
        winreg.CloseKey(key)
        
        print("Context menu entry added successfully!")
        return True
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def remove_context_menu():
    try:
        # Remove the entire key
        winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r"Python.File\shell\RunInCommand\command")
        winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r"Python.File\shell\RunInCommand")
        print("Context menu entry removed successfully!")
        return True
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    # Check if script has admin rights
    if not is_admin():
        print("Requesting administrator privileges...")
        run_as_admin()
        sys.exit()

    while True:
        print("\n1. Add 'Run in Command' to context menu")
        print("2. Remove 'Run in Command' from context menu")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            add_context_menu()
        elif choice == "2":
            remove_context_menu()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")