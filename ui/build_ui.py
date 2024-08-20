import subprocess
import os

def run_command(command):
    try:
        result = subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Command '{command}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e.stderr.decode()}")  

def delete_file_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted file: {file_path}")
    else:
        print(f"File does not exist: {file_path}")

if __name__ == "__main__":
    files_to_delete = ["resources_rc.py", "mainwindow_ui.py", "searchtrackwidget_ui.py"]
    
    for file in files_to_delete:
        delete_file_if_exists(file)

    commands = [
        "pyside6-rcc resources.qrc -o resources_rc.py",
        "pyside6-uic searchtrackwidget.ui -o searchtrackwidget_ui.py",
        "pyside6-uic mainwindow.ui -o mainwindow_ui.py"
    ]

    for command in commands:
        run_command(command)
