from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Property
import yt_dlp
from AudioStreamer.audiostreamertrack import AudioStreamerTrack
from searchtrackwidget_ui import Ui_SearchTrackWidgetBase

# Search Track Widget
class SearchTrackWidget(QWidget, Ui_SearchTrackWidgetBase):
    # Class Variables (Global)
    selected_widget = None  # Class variable to track the currently selected widget
    AS = None  # Class variable for the AudioStreamer instance
    
    def __init__(self, track, parent=None):
        super(SearchTrackWidget, self).__init__(parent)
        self.setupUi(self)
        self._track = track
        # Set Widget UI
        self.artistLabel.setText(track.artists)
        self.musicLabel.setText(track.name)
        self.iconLabel.setCover(track.cover)
        # Custom Properties for Widget
        self._checked = False
        self.updateStylesheet()
    
    @classmethod
    def setAudioStreamer(cls, audio_streamer):
        """Set the shared AudioStreamer instance for all SearchTrackWidget instances."""
        cls.AS = audio_streamer

    def getChecked(self):
        return self._checked

    def setChecked(self, value):
        self._checked = value
        self.updateStylesheet()
        if value:   
            SearchTrackWidget.selected_widget = self  # Set this widget as the selected one
        else:
            SearchTrackWidget.selected_widget = None  # Deselect if unchecked

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
        if not self.getChecked():
            # If there's a currently selected widget and it's not this one, deselect it
            if SearchTrackWidget.selected_widget and SearchTrackWidget.selected_widget != self:
                SearchTrackWidget.selected_widget.setChecked(False)  # Deselect the currently selected widget
            # Check this widget
            self.setChecked(True)
        super().mousePressEvent(event)
    
    def mouseDoubleClickEvent(self, event):
        if self.AS.active:
            self.AS.stop()
        if not self._track.url:
            self._track.getYoutubeAudio()
        if self._track.url:
            self.AS.play(self._track)
        super().mouseDoubleClickEvent(event)
    