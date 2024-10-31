from PySide6.QtWidgets import QSlider
from PySide6.QtCore import Qt

class HoverSlider(QSlider):
    def __init__(self, orientation=Qt.Orientation.Horizontal, parent=None):
        super().__init__(orientation, parent)
        self.setStyleSheet(self.default_style())

    def default_style(self):
        return """
                QSlider {
	        background-color: transparent;
                }

                QSlider::groove:horizontal {
                background: rgb(76, 76, 76); /* Grey for the background */
                height: 4px; /* Thickness of the slider */
                border-radius: 2px; /* Rounded edges */
                }

                QSlider::add-page:horizontal  {
                background: rgb(76, 76, 76);
                        height: 4px; /* Thickness of the slider */
                border-radius: 2px; /* Rounded edges */
                }

                QSlider::sub-page:horizontal  {
                background: rgb(255, 255, 255);
                        height: 4px; /* Thickness of the slider */
                border-radius: 2px; /* Rounded edges */
                }

                QSlider::handle:horizontal  {
                background: transparent; 
                width: 12px;
                height: 6px;
                margin: -4px -3;
                border-radius: 6px;
                }

        """

    def hover_style(self):
        return """
                QSlider {
	        background-color: transparent;
                }
                
                QSlider::groove:horizontal {
                background: rgb(76, 76, 76); /* Grey for the background */
                height: 4px; /* Thickness of the slider */
                border-radius: 2px; /* Rounded edges */
                }

                QSlider::add-page:horizontal  {
                background: rgb(76, 76, 76);
                        height: 4px; /* Thickness of the slider */
                border-radius: 2px; /* Rounded edges */
                }

                QSlider::sub-page:horizontal  {
                background: rgb(26, 216, 103);
                        height: 4px; /* Thickness of the slider */
                border-radius: 2px; /* Rounded edges */
                }

                QSlider::handle:horizontal  {
                background: rgb(255, 255, 255); 
                width: 12px;
                height: 6px;
                margin: -4px 0;
                border-radius: 6px;
                }

        """

    def enterEvent(self, event):
        self.setStyleSheet(self.hover_style())
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet(self.default_style())
        super().leaveEvent(event)