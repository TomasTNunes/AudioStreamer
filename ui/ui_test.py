import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from mainwindow_ui import Ui_MainWindow  # Import the converted class
from searchtrackwidget import SearchTrackWidget

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Create an instance of SearchTrackWidget
        track_widget = SearchTrackWidget("Artist Name", "Music Title", '', '')
        
        # Add the widget to the vertical layout
        self.RSWSscrollVLayout.addWidget(track_widget)

        for i in range(10):
            track_widget = SearchTrackWidget(f'{i}', f'{i}', '', '')
            self.RSWSscrollVLayout.addWidget(track_widget)


if __name__ == "__main__":
    # Run application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
