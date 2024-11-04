import requests
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtCore import Qt, QThread, Signal

class ImageLoader(QThread):
    imageLoaded = Signal(bytes)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.imageLoaded.emit(response.content)

class CoverLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._border_radius = 4 # pc
    
    def setCover(self, cover_url):
        # Start a background thread to fetch the image data from the URL
        self.loader = ImageLoader(cover_url)
        self.loader.imageLoaded.connect(self._setCover)
        self.loader.start()
    
    def _setCover(self, cover_content):
        image = QPixmap()
        image.loadFromData(cover_content)
        # Scale the image to the QLabel size while keeping aspect ratio
        scaled_image = image.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        # Create a mask with rounded corners
        rounded_pixmap = QPixmap(self.size())
        rounded_pixmap.fill(Qt.GlobalColor.transparent)  # Start with a transparent pixmap
        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        # Draw the rounded rectangle mask
        path = QPainterPath()
        path.addRoundedRect(rounded_pixmap.rect(), self._border_radius, self._border_radius)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, scaled_image)
        painter.end()
        # Set the rounded pixmap to the QLabel
        self.setPixmap(rounded_pixmap)