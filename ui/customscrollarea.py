from PySide6.QtWidgets import QScrollArea, QGraphicsOpacityEffect
from PySide6.QtCore import QTimer, QPropertyAnimation

class CustomScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Initialize the timer to hide scroll bar
        self.timer = QTimer()
        self.timer.setInterval(750)  # ms
        self.timer.timeout.connect(self.start_fade_out)
        # Create opacity effects for the scrollbars
        self.vertical_opacity_effect = QGraphicsOpacityEffect(self.verticalScrollBar())
        self.verticalScrollBar().setGraphicsEffect(self.vertical_opacity_effect)
        # Create animations for the scrollbars
        # Fade in animation
        self.vertical_fade_in_animation = QPropertyAnimation(self.vertical_opacity_effect, b"opacity")
        self.vertical_fade_in_animation.setDuration(150)  # Duration of the fade effect
        self.vertical_fade_in_animation.setStartValue(0.0)  # Start invisible
        self.vertical_fade_in_animation.setEndValue(1.0)  # End fully visible
        # Fade out animation
        self.vertical_fade_out_animation = QPropertyAnimation(self.vertical_opacity_effect, b"opacity")
        self.vertical_fade_out_animation.setDuration(150)  # Duration of the fade effect
        self.vertical_fade_out_animation.setStartValue(1.0)  # Start fully visible
        self.vertical_fade_out_animation.setEndValue(0.0)  # End invisible

    def enterEvent(self, event):
        self.timer.stop()  # Stop the timer if mouse enters
        # Start the fade-in animation
        if self.vertical_opacity_effect.opacity() < 1.:
            self.vertical_fade_in_animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.timer.start()  # Start the timer when mouse leaves
        super().leaveEvent(event)

    def start_fade_out(self):
        # Start the fade-out animation
        self.vertical_fade_out_animation.start()
        self.timer.stop()  # Stop the timer after starting fade out