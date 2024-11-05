from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QFontMetrics
from PySide6.QtCore import Qt

class ElidedLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._full_text = None
        self._max_width = None  # Store the maximum width for the label

    def setText(self, text):
        """Override setText to store the full text."""
        self._full_text = text
        font_metrics = QFontMetrics(self.font())
        # Plus a mrgin to account for ... otherwise we reach maximum width with ...
        self._max_width = font_metrics.horizontalAdvance(self._full_text)+1
        self._applyElidedText()

    def resizeEvent(self, event):
        """Handle resize event to update eliding."""
        super().resizeEvent(event)
        self._applyElidedText()

    def _applyElidedText(self):
        """Apply eliding to the label text based on the current width."""
        if self._max_width and self.width() > self._max_width:
            self.setMaximumWidth(self._max_width)
        if self._full_text:
            font_metrics = QFontMetrics(self.font())
            elided_text = font_metrics.elidedText(self._full_text, Qt.ElideRight, self.width())
            super().setText(elided_text)