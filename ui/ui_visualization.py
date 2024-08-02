import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from build_ui import run_command

from mainwindow import Ui_MainWindow  # Import the converted class

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    commands = [
        "pyside6-rcc resources.qrc -o resources_rc.py",
        "pyside6-uic mainwindow.ui -o mainwindow.py"
    ]
    for command in commands:
        run_command(command)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
