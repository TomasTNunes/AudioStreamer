from PySide6.QtWidgets import QSlider
from PySide6.QtCore import Qt

class HoverSlider(QSlider):
    def __init__(self, orientation=Qt.Orientation.Horizontal, parent=None):
        super().__init__(orientation, parent)
        self.set_hover = False
        self.setStyleSheet(self.default_style())
        self.valueChanged.connect(self.update_style_based_on_value)

    def update_style_based_on_value(self):
        if self.value() == 0:
            if self.set_hover:
                self.setStyleSheet(self.empty_style_hover())
            else:
                self.setStyleSheet(self.empty_style())
        elif self.value() == self.maximum():
            if self.set_hover:
                self.setStyleSheet(self.full_style_hover())
            else:
                self.setStyleSheet(self.full_style())
        else:
            if self.set_hover:
                self.setStyleSheet(self.hover_style())
            else:
                self.setStyleSheet(self.default_style())

    def default_style(self):
        return """
                QSlider {
                    background-color: transparent;
                }

                QSlider::groove:horizontal {
                    background: rgb(76, 76, 76);
                    height: 4px;
                    border-radius: 2px;
                }

                QSlider::add-page:horizontal  {
                    background: rgb(76, 76, 76);
                    height: 4px;
                    border-radius: 2px;
                }

                QSlider::sub-page:horizontal  {
                    background: rgb(255, 255, 255);
                    height: 4px;
                    border-radius: 2px;
                }

                QSlider::handle:horizontal  {
                    background: transparent;
                    width: 12px;
                    height: 6px;
                    margin: -4px -3px;
                    border-radius: 6px;
                }

                QSlider::groove:horizontal:disabled {
                    background: rgb(20, 20, 20);
                }

                QSlider::add-page:horizontal:disabled  {
                    background: rgb(20, 20, 20);
                }

                QSlider::sub-page:horizontal:disabled  {
                    background: rgb(20, 20, 20);
                }
        """

    def hover_style(self):
        return """
                QSlider {
                    background-color: transparent;
                }
                
                QSlider::groove:horizontal {
                    background: rgb(76, 76, 76);
                    height: 4px;
                    border-radius: 2px;
                }

                QSlider::add-page:horizontal  {
                    background: rgb(76, 76, 76);
                    height: 4px;
                    border-radius: 2px;
                }

                QSlider::sub-page:horizontal  {
                    background: rgb(26, 216, 103);
                    height: 4px;
                    border-radius: 2px;
                }

                QSlider::handle:horizontal  {
                    background: rgb(255, 255, 255);
                    width: 12px;
                    height: 6px;
                    margin: -4px 0;
                    border-radius: 6px;
                }

                QSlider::groove:horizontal:disabled {
                    background: rgb(20, 20, 20);
                }

                QSlider::add-page:horizontal:disabled  {
                    background: rgb(20, 20, 20);
                }

                QSlider::sub-page:horizontal:disabled  {
                    background: rgb(20, 20, 20);
                }

                QSlider::handle:horizontal:disabled  {
                    background: transparent;
                    width: 12px;
                    height: 6px;
                    margin: -4px 0;
                    border-radius: 6px;
                }
        """

    def empty_style(self):
        return """
                QSlider {
                    background-color: transparent;
                }

                QSlider::groove:horizontal {
                    background: rgb(76, 76, 76);
                    height: 4px;
                    border-radius: 2px;
                }

                QSlider::handle:horizontal  {
                    background: transparent;
                    width: 12px;
                    height: 6px;
                    margin: -4px -3px;
                    border-radius: 6px;
                }

                QSlider::groove:horizontal:disabled {
                    background: rgb(20, 20, 20);
                }
        """
    
    def empty_style_hover(self):
        return """
                QSlider {
                    background-color: transparent;
                }
                
                QSlider::groove:horizontal {
                    background: rgb(76, 76, 76);
                    height: 4px;
                    border-radius: 2px;
                }

                QSlider::handle:horizontal  {
                    background: rgb(255, 255, 255);
                    width: 12px;
                    height: 6px;
                    margin: -4px 0;
                    border-radius: 6px;
                }

                QSlider::groove:horizontal:disabled {
                    background: rgb(20, 20, 20);
                }

                QSlider::handle:horizontal:disabled  {
                    background: transparent;
                    width: 12px;
                    height: 6px;
                    margin: -4px 0;
                    border-radius: 6px;
                }
        """
    
    def full_style(self):
        return """
                QSlider {
                    background-color: transparent;
                }

                QSlider::groove:horizontal {
                    background: rgb(255, 255, 255);
                    height: 4px;
                    border-radius: 2px;
                }

                QSlider::handle:horizontal  {
                    background: transparent;
                    width: 12px;
                    height: 6px;
                    margin: -4px -3px;
                    border-radius: 6px;
                }

                QSlider::groove:horizontal:disabled {
                    background: rgb(20, 20, 20);
                }
        """
    
    def full_style_hover(self):
        return """
                QSlider {
                    background-color: transparent;
                }
                
                QSlider::groove:horizontal {
                    background: rgb(26, 216, 103);
                    height: 4px;
                    border-radius: 2px;
                }

                QSlider::handle:horizontal  {
                    background: rgb(255, 255, 255);
                    width: 12px;
                    height: 6px;
                    margin: -4px 0;
                    border-radius: 6px;
                }

                QSlider::groove:horizontal:disabled {
                    background: rgb(20, 20, 20);
                }

                QSlider::handle:horizontal:disabled  {
                    background: transparent;
                    width: 12px;
                    height: 6px;
                    margin: -4px 0;
                    border-radius: 6px;
                }
        """

    def enterEvent(self, event):
        self.set_hover = True
        self.update_style_based_on_value()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.set_hover = False
        self.update_style_based_on_value()
        super().leaveEvent(event)
