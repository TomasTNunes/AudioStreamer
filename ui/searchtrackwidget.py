from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Property, Qt, Signal, QObject
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
import requests
import yt_dlp
from AudioStreamer.audiostreamertrack import AudioStreamerTrack
from searchtrackwidget_ui import Ui_SearchTrackWidgetBase

# Search Track Widget
class SearchTrackWidget(QWidget, Ui_SearchTrackWidgetBase):
    # Class Variables (Global)
    selected_widget = None  # Class variable to track the currently selected widget
    AS = None  # Class variable for the AudioStreamer instance
    SL = None  # Class variable for the SongLink instance
    
    def __init__(self, track, artist, cover_content, spotify_uri, parent=None):
        super(SearchTrackWidget, self).__init__(parent)
        self.setupUi(self)
        self.artistLabel.setText(artist)
        self.musicLabel.setText(track)
        self.setCoverImage(cover_content)
        # Audio URL
        self.spotify_uri = spotify_uri
        self.youtube_url = None
        self.AStrack = None
        # Custom Properties for Widget
        self._checked = False
        self.updateStylesheet()
    
    @classmethod
    def set_AudioStreamer(cls, audio_streamer):
        """Set the shared AudioStreamer instance for all SearchTrackWidget instances."""
        cls.AS = audio_streamer
    
    @classmethod
    def set_SongLink(cls, song_link):
        """Set the shared SongLink instance for all SearchTrackWidget instances."""
        cls.SL = song_link
    
    def setCoverImage(self, cover_content):
        image = QPixmap()
        image.loadFromData(cover_content)
        # Scale the image to the QLabel size while keeping aspect ratio
        scaled_image = image.scaled(self.iconLabel.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        # Create a mask with rounded corners
        rounded_pixmap = QPixmap(self.iconLabel.size())
        rounded_pixmap.fill(Qt.GlobalColor.transparent)  # Start with a transparent pixmap
        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        path = QPainterPath()
        path.addRoundedRect(rounded_pixmap.rect(), 4, 4)  # Set the radius to 4px
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, scaled_image)
        painter.end()
        # Set the rounded pixmap to the QLabel
        self.iconLabel.setPixmap(rounded_pixmap)

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

    def get_AStrack(self):
        try:
            self.youtube_url = self.SL.getByUrl(self.spotify_uri).entitiesByProvider['youtube'].linksByPlatform['youtubeMusic']
            ydl_opts = {
                'format': 'bestaudio',
                'noplaylist': True,
                'quiet': True,
                'no_warnings': True,
                'extract_flat': 'in_playlist',
                }
        
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(self.youtube_url, download=False)
                audio_url = info_dict['url']
                duration = int(info_dict['duration'])
            self.AStrack = AudioStreamerTrack(audio_url, duration)
        except Exception as e:
            print(f'Fail to get AS Track: {e}')
            return None

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
        if not self.AStrack:
            self.get_AStrack()
        if self.AStrack:
            self.AS.play(self.AStrack)
        super().mouseDoubleClickEvent(event)
    