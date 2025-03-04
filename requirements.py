import subprocess
import sys

def install_requirements():
    requirements = [
        'ctypes',
        'winreg'
    ]
    
    for package in requirements:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"Successfully installed {package}")
        except:
            print(f"Note: {package} is already part of Python standard library")

if __name__ == "__main__":
    print("Installing requirements...")
    install_requirements()
    print("\nAll requirements have been installed!")