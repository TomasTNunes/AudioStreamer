from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Property

from searchtrackwidget_ui import Ui_SearchTrackWidgetBase

# Search Track Widget
class SearchTrackWidget(QWidget, Ui_SearchTrackWidgetBase):
    def __init__(self, artist, music, parent=None):
        super(SearchTrackWidget, self).__init__(parent)
        self.setupUi(self)
        self.artistLabel.setText(artist)
        self.musicLabel.setText(music)

    # Custom Properties for Widget
        self._checked = False
        self.updateStylesheet()

    def getChecked(self):
        return self._checked

    def setChecked(self, value):
        self._checked = value
        self.updateStylesheet()

    def updateStylesheet(self):
        if self._checked:
            self.SearchTrackWidget.setStyleSheet("""
                QWidget {
                    background-color: rgb(80, 80, 80);
                    border-radius: 4px;
                }
            """)
        else:
            self.SearchTrackWidget.setStyleSheet("""
                QWidget{
                    background-color: rgb(18, 18, 18);
                    border-radius: 4px;
                }

                QWidget:hover{
                    background-color: rgb(36, 36, 36);
                }
            """)

    checked = Property(bool, getChecked, setChecked)

    def mousePressEvent(self, event):
        self.setChecked(not self.getChecked())
        super().mousePressEvent(event)