from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QIcon

class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setClearButtonEnabled(False)  # Disable default clear button

        # Custom clear button
        self.clear_button = QPushButton(self)
        self.clear_button.setIcon(QIcon(":/path/to/your/custom_clear_icon.png"))
        self.clear_button.setCursor(Qt.PointingHandCursor)
        self.clear_button.setVisible(False)
        self.clear_button.setStyleSheet("border: none; background: transparent;")
        self.clear_button.clicked.connect(self.clear)

        self.textChanged.connect(self.update_clear_button)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        button_size = self.clear_button.sizeHint()
        frame_width = self.style().pixelMetric(self.style().PM_DefaultFrameWidth)
        self.clear_button.setGeometry(
            QRect(
                self.rect().right() - button_size.width() - frame_width,
                (self.rect().height() - button_size.height()) / 2,
                button_size.width(),
                button_size.height()
            )
        )

    def update_clear_button(self, text):
        self.clear_button.setVisible(bool(text))

# Main application
app = QApplication([])

# Create a CustomLineEdit
line_edit = CustomLineEdit()
line_edit.show()

app.exec_()
