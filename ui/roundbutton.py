from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QRect
from PySide6.QtGui import QRegion

class RoundButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.make_button_circular()

    def make_button_circular(self):
        # Define extra padding for the clickable area
        padding = 1
        # Create a circular region based on the button's size with added padding
        circular_region = QRegion(
            QRect(-padding, -padding, self.width() + 2 * padding, self.height() + 2 * padding), 
            QRegion.Ellipse
        )
        self.setMask(circular_region)

    def resizeEvent(self, event):
        super().resizeEvent(event)  # Call the base class's resizeEvent
        self.make_button_circular()  # Update the circular mask on resize
