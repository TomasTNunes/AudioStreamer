from roundbutton import RoundButton

class LoopButton(RoundButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.icons = {
            "unchecked": """QPushButton {
                                            background-color: trasnparent;
                                            border-radius: 0px;
                                        }
                                        QPushButton:hover {
                                            icon: url(:/assets/buttons/loop_hover.png);
                                        }
                                        QPushButton:pressed  {
                                            icon: url(:/assets/buttons/loop_pressed.png);
                                        }
                                        QPushButton:checked  {
                                            icon: url(:/assets/buttons/loop_checked.png);
                                        }""",
            "checked": """QPushButton {
                                            background-color: trasnparent;
                                            border-radius: 0px;
                                        }
                                        QPushButton:hover {
                                            icon: url(:/assets/buttons/loop_hover.png);
                                        }
                                        QPushButton:pressed  {
                                            icon: url(:/assets/buttons/loop_pressed.png);
                                        }
                                        QPushButton:checked  {
                                            icon: url(:/assets/buttons/loop_checked.png);
                                        }""",   
            "checked2": """QPushButton {
                                            background-color: trasnparent;
                                            border-radius: 0px;
                                        }
                                        QPushButton:hover {
                                            icon: url(:/assets/buttons/loop_hover.png);
                                        }
                                        QPushButton:pressed  {
                                            icon: url(:/assets/buttons/loop_pressed.png);
                                        }
                                        QPushButton:checked  {
                                            icon: url(:/assets/buttons/loop_checked2.png);
                                        }""",  
        }

        # Set initial state
        self.setProperty("state", "unchecked")
        self.setStyleSheet(self.icons["unchecked"])

        # Connect button click signal to method
        self.clicked.connect(self.update_icon)

    def update_icon(self):
        if self.isChecked():
            self.setProperty("state", "checked")
            self.setStyleSheet(self.icons["checked"])
        else:
            if self.getState() == "checked":
                self.setChecked(True)
                self.setProperty("state", "checked2")
                self.setStyleSheet(self.icons["checked2"])
            else:
                self.setProperty("state", "unchecked")
                self.setStyleSheet(self.icons["unchecked"])
    
    def getState(self):
        return self.property("state")