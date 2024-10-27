import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow
# Add the 'ui' directory to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'ui'))
from ui.mainwindow_ui import Ui_MainWindow
from ui.searchtrackwidget import SearchTrackWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Set Intial Conditions
        self.homeButton.setChecked(True)
        self.rightStackedWidget.setCurrentWidget(self.RSWhomeWidget)

        # Connect buttons to functions
        self.homeButton.clicked.connect(self.homeButtonClick)
        self.searchButton.clicked.connect(self.searchButtonClick)


    def homeButtonClick(self):
        # Switch to the home page by specifying the widget
        self.rightStackedWidget.setCurrentWidget(self.RSWhomeWidget)
        self.homeButton.setChecked(True)
        self.searchButton.setChecked(False)

    def searchButtonClick(self):
        # Switch to the search page by specifying the widget
        self.rightStackedWidget.setCurrentWidget(self.RSWsearchWidget)
        self.searchButton.setChecked(True)
        self.homeButton.setChecked(False)


if __name__ == "__main__":
    # Run application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
