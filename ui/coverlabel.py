from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtCore import Qt

class CoverLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._border_radius = 4 # pc
    
    def setCover(self, cover_content):
        image = QPixmap()
        image.loadFromData(cover_content)
        # Scale the image to the QLabel size while keeping aspect ratio
        scaled_image = image.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        # Create a mask with rounded corners
        rounded_pixmap = QPixmap(self.size())
        rounded_pixmap.fill(Qt.GlobalColor.transparent)  # Start with a transparent pixmap
        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        path = QPainterPath()
        path.addRoundedRect(rounded_pixmap.rect(), self._border_radius, self._border_radius)  # Set the radius to 4px
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, scaled_image)
        painter.end()
        # Set the rounded pixmap to the QLabel
        self.setPixmap(rounded_pixmap)