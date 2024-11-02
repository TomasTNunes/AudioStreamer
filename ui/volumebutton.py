from roundbutton import RoundButton

class VolumeButton(RoundButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._lastVolume = None
        self._mainwindow = self.parent().parent().parent().parent()
        self.icons = {
            "lowVolume": """QPushButton {
                                            background-color: transparent;
                                            border-radius: 0px;
                                            icon: url(:/assets/buttons/volumeLow.png);
                                        }
                                        QPushButton:hover {
                                            icon: url(:/assets/buttons/volumeLow_hover.png);
                                        }
                                        QPushButton:pressed  {
                                            icon: url(:/assets/buttons/volumeLow_pressed.png);
                                        }
                                        QPushButton:checked  {
                                            icon: url(:/assets/buttons/volumeMute.png);
                                        }
                                        QPushButton:checked:hover  {
                                            icon: url(:/assets/buttons/volumeMute_hover.png);
                                        }
                                        QPushButton:checked:pressed  {
                                            icon: url(:/assets/buttons/volumeMute_pressed.png);
                                        }""",
            "mediumVolume": """QPushButton {
                                            background-color: transparent;
                                            border-radius: 0px;
                                            icon: url(:/assets/buttons/volumeMedium.png);
                                        }
                                        QPushButton:hover {
                                            icon: url(:/assets/buttons/volumeMedium_hover.png);
                                        }
                                        QPushButton:pressed  {
                                            icon: url(:/assets/buttons/volumeMedium_pressed.png);
                                        }
                                        QPushButton:checked  {
                                            icon: url(:/assets/buttons/volumeMute.png);
                                        }
                                        QPushButton:checked:hover  {
                                            icon: url(:/assets/buttons/volumeMute_hover.png);
                                        }
                                        QPushButton:checked:pressed  {
                                            icon: url(:/assets/buttons/volumeMute_pressed.png);
                                        }""",
            "highVolume": """QPushButton {
                                            background-color: transparent;
                                            border-radius: 0px;
                                            icon: url(:/assets/buttons/volumeHigh.png);
                                        }
                                        QPushButton:hover {
                                            icon: url(:/assets/buttons/volumeHigh_hover.png);
                                        }
                                        QPushButton:pressed  {
                                            icon: url(:/assets/buttons/volumeHigh_pressed.png);
                                        }
                                        QPushButton:checked  {
                                            icon: url(:/assets/buttons/volumeMute.png);
                                        }
                                        QPushButton:checked:hover  {
                                            icon: url(:/assets/buttons/volumeMute_hover.png);
                                        }
                                        QPushButton:checked:pressed  {
                                            icon: url(:/assets/buttons/volumeMute_pressed.png);
                                        }""",  
        }

        # Set initial state
        self.setStyleSheet(self.icons["lowVolume"])
    
    @property
    def lastVolume(self):
        return self._lastVolume
    
    def set_lastVolume(self, volume):
        self._lastVolume = volume

    def update_volume_style(self, volume):
        maximum = self._mainwindow.volumeSlider.maximum()
        if volume < maximum/3:
            self.setStyleSheet(self.icons["lowVolume"])
        elif volume < maximum*2/3:
            self.setStyleSheet(self.icons["mediumVolume"])
        else:
            self.setStyleSheet(self.icons["highVolume"])
    
    def enterEvent(self, event):
        self._mainwindow.volumeSlider.set_hover = True
        self._mainwindow.volumeSlider.update_style_based_on_value()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._mainwindow.volumeSlider.set_hover = False
        self._mainwindow.volumeSlider.update_style_based_on_value()
        super().leaveEvent(event)