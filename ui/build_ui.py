import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Command '{command}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e.stderr.decode()}")  

if __name__ == "__main__":
    commands = [
        "pyside6-rcc resources.qrc -o resources_rc.py",
        "pyside6-uic mainwindow.ui -o mainwindow.py"
    ]

    for command in commands:
        run_command(command)