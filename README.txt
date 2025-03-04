Run in Command - Python Context Menu Tool
=======================================

Overview:
---------
This utility adds a "Run in Command" option to your Windows context menu for Python files. 
It allows you to execute Python scripts directly in a Command Prompt window while maintaining 
the correct working directory.

Purpose:
--------
- View command-line output that would otherwise disappear instantly
- Interact with scripts that require command-line input
- Debug scripts with proper console output
- Maintain working directory context for scripts that depend on relative paths

Requirements:
------------
- Windows Operating System
- Python 3.x installed
- Administrator privileges (for registry modification)

Installation:
------------
1. Download the repository
2. Run requirements.py (optional, as dependencies are part of standard library)
3. Run run-in-command.py with administrator privileges
4. Select option 1 to add the context menu entry

Usage Example:
-------------
Scenario: You have a data processing script that reads files from its directory and outputs 
results to the console. Without this tool, you'd need to:
1. Open CMD manually
2. Navigate to the script's directory
3. Run the script

With this tool:
1. Right-click the Python file
2. Select "Run in Command"
The script executes immediately in CMD with the correct working directory.

Uninstallation:
--------------
1. Run run-in-command.py with administrator privileges
2. Select option 2 to remove the context menu entry 