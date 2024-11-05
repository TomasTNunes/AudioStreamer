import sys
import os
import requests
from dotenv import load_dotenv
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from AudioStreamer.audiostreamerV04 import AudioStreamer
from AudioStreamer.events import TrackStartEvent, TrackEndEvent
from track import Track
# Add the 'SongLink' directory to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'SongLink'))
from SongLink.songlink import SongLink
# Add the 'ui' directory to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'ui'))
from ui.mainwindow_ui import Ui_MainWindow
from ui.searchtrackwidget import SearchTrackWidget

# Load Environment Variables
load_dotenv(os.path.join(os.getcwd(), '.env'))

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect Home and Search buttons to functions
        self.homeButton.clicked.connect(self.homeButtonClick)
        self.searchButton.clicked.connect(self.searchButtonClick)

        # Connect Enter key press in RSWSsearchQLineEdit to a function
        self.RSWSsearchQLineEdit.returnPressed.connect(self.onSearchEnter)

        # Connect Player Buttons to functions
        self.playButton.clicked.connect(self.playButtonClick)

        # Create and Connect track timer to a function for playTimeSlider
        self.trackTimer = QTimer()
        self.trackTimer.setInterval(1000)  # Update every second
        self.trackTimer.timeout.connect(self.trackTimerUpdate)

        # Connect playTimeSlider slider functions
        self.playTimeSlider.sliderPressed.connect(self.trackTimer.stop)
        self.playTimeSlider.sliderReleased.connect(self.playTimeSliderRelease)

        # Connect timeLabel to playTimeSlider
        self.playTimeSlider.valueChanged.connect(self.playTimeSliderValueChange)

        # Connect volumeButton to function
        self.volumeButton.clicked.connect(self.volumeButtonClick)

        # Connect volumeSlider slider functions
        self.volumeSlider.sliderPressed.connect(self.volumeSliderPressed)

        # Connect volumeButton to volumeSlider
        self.volumeSlider.valueChanged.connect(self.volumeSliderValueChange)

        # Initialize and Connect Search Filter Buttons
        self.RSWSallButton.clicked.connect(self.RSWSallButtonClick)
        self.RSWSallButton.click() # Initialize "all" as initial selected Search Filter Button
        self.RSWSsongsButton.clicked.connect(self.RSWSsongsButtonClick)
        self.RSWSplaylistsButton.clicked.connect(self.RSWSplaylistsButtonClick)
        self.RSWSalbumsButton.clicked.connect(self.RSWSalbumsButtonClick)
        self.RSWSartistsButton.clicked.connect(self.RSWSartistsButtonClick)

        # Set Utilities
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('SPOTIFYCLIENTID'),
                                               client_secret=os.getenv('SPOTIFYCLIENTSECRET'),
                                               redirect_uri=os.getenv('SPOTIFYREDIRECTURI'),
                                               scope="user-library-read"))
        self.AS = AudioStreamer()
        SearchTrackWidget.setAudioStreamer(self.AS)
        self.SL = SongLink()
        Track.setSongLink(self.SL)

        # Add AudioStreamer Events
        self.AS.add_event_hook(self.onTrackStartEvent, event=TrackStartEvent)
        self.AS.add_event_hook(self.onTrackEndEvent, event=TrackEndEvent)

        # Additional variables
        self.lastSearch = None

        # Set Intial Conditions
        self.homeButton.setChecked(True)
        self.rightStackedWidget.setCurrentWidget(self.RSWhomeWidget)
        self.disableMediaButtons()
        self.volumeSlider.setRange(0, 50) # max Volume
        self.volumeSlider.setValue(self.AS.volume)
        self.prev_BWleftWidget_width = self.BWleftWidget.width()

    #------------------------ Home&Search Buttons ------------------------#
    def homeButtonClick(self):
        # Switch to the home page by specifying the widget
        self.rightStackedWidget.setCurrentWidget(self.RSWhomeWidget)
        self.homeButton.setChecked(True)
        self.searchButton.setChecked(False)

    def searchButtonClick(self):
        # Switch to the search page by specifying the widget
        self.rightStackedWidget.setCurrentWidget(self.RSWsearchWidget)
        self.searchButton.setChecked(True)
        self.homeButton.setChecked(False)
    
    #------------------------ Search Bar ------------------------#
    def clearRSWsearchWidget(self):
        SearchTrackWidget.selected_widget = None
        # Loop through and remove each widget from the all search layout s
        # except last widget which is the spacer
        # All
        for i in range(self.RSWSSWallScrollVLayout.count() - 2, -1, -1):
            item = self.RSWSSWallScrollVLayout.takeAt(i)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()  # Delete the widget from memory
        # Songs
        for i in range(self.RSWSSWsongsScrollVLayout.count() - 2, -1, -1):
            item = self.RSWSSWsongsScrollVLayout.takeAt(i)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()  # Delete the widget from memory
        # Playlists
        for i in range(self.RSWSSWplaylistsScrollVLayout.count() - 2, -1, -1):
            item = self.RSWSSWplaylistsScrollVLayout.takeAt(i)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()  # Delete the widget from memory
        # Albums
        for i in range(self.RSWSSWalbumsScrollVLayout.count() - 2, -1, -1):
            item = self.RSWSSWalbumsScrollVLayout.takeAt(i)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()  # Delete the widget from memory
        # Artists
        for i in range(self.RSWSSWartistsScrollVLayout.count() - 2, -1, -1):
            item = self.RSWSSWartistsScrollVLayout.takeAt(i)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()  # Delete the widget from memory
    
    def onSearchEnter(self):
        # Clear all existing track widgets before adding new ones
        self.clearRSWsearchWidget()
        # Get text from RSWSsearchQLineEdit when Enter is pressed
        search_text = self.RSWSsearchQLineEdit.text()
        if search_text.strip():
            self.lastSearch = self.sp.search(q=search_text, type='track,playlist,album,artist', limit=20)
            for i,item in enumerate(self.lastSearch['tracks']['items']):
                track = Track(item)
                # Create an instance of SearchTrackWidget
                track_widget = SearchTrackWidget(track)
                self.RSWSSWallScrollVLayout.insertWidget(self.RSWSSWallScrollVLayout.count()-1,track_widget)        
    
    #----------------------- Search Filter Buttons ------------------------#
    def RSWSallButtonClick(self):
        self.RSWSstackedWidget.setCurrentWidget(self.RSWSSWallWidget)
    
    def RSWSsongsButtonClick(self):
        self.RSWSstackedWidget.setCurrentWidget(self.RSWSSWsongsWidget)
    
    def RSWSplaylistsButtonClick(self):
        self.RSWSstackedWidget.setCurrentWidget(self.RSWSSWplaylistsWidget)
    
    def RSWSalbumsButtonClick(self):
        self.RSWSstackedWidget.setCurrentWidget(self.RSWSSWalbumsWidget)
    
    def RSWSartistsButtonClick(self):
        self.RSWSstackedWidget.setCurrentWidget(self.RSWSSWartistsWidget)
    
    # def getActiveSearchLayout(self):
    #     if self.RSWSallButton.isChecked():
    #         return self.RSWSSWallScrollVLayout
    #     elif self.RSWSsongsButton.isChecked():
    #         return self.RSWSSWsongsScrollVLayout
    #     elif self.RSWSplaylistsButton.isChecked():
    #         return self.RSWSSWplaylistsScrollVLayout
    #     elif self.RSWSalbumsButton.isChecked():
    #         return self.RSWSSWalbumsScrollVLayout
    #     elif self.RSWSartistsButton.isChecked():
    #         return self.RSWSSWartistsScrollVLayout

    #------------------------ Media Buttons ------------------------#
    def enableMediaButtons(self):
        track = self.AS.track
        # Enable Media Buttons
        self.playButton.setChecked(True)
        self.playButton.setEnabled(True)
        self.nextTrackButton.setEnabled(True)
        self.previousTrackButton.setEnabled(True)
        self.loopButton.setEnabled(True)
        self.shuffleButton.setEnabled(True)
        self.playTimeSlider.setRange(0, track.duration)
        self.playTimeSlider.setValue(0)
        self.playTimeSlider.setEnabled(True)
        self.timeLabel.setStyleSheet('color: rgb(255, 255, 255);')
        self.timeLabel.setText('0:00')
        self.durationLabel.setStyleSheet('color: rgb(255, 255, 255);')
        self.durationLabel.setText(track.durationFormat)
        # Set UI of playing track
        self.iconLabel.setCover(track.cover)
        self.iconLabel.setEnabled(True)
        self.musicLabel.setText(track.name)
        self.musicLabel.setEnabled(True)
        self.artistLabel.setText(track.artists)
        self.artistLabel.setEnabled(True)
        self.resizeActiveTrackLabels()

    def disableMediaButtons(self):
        # Disable Media Buttons
        self.playButton.setChecked(False)
        self.playButton.setEnabled(False)
        self.nextTrackButton.setEnabled(False)
        self.previousTrackButton.setEnabled(False)
        self.loopButton.setEnabled(False)
        self.shuffleButton.setEnabled(False)
        self.playTimeSlider.setValue(0)
        self.playTimeSlider.setEnabled(False)
        self.timeLabel.setStyleSheet('color: rgb(20, 20, 20);')
        self.timeLabel.setText('--:--')
        self.durationLabel.setStyleSheet('color: rgb(20, 20, 20);')
        self.durationLabel.setText('--:--')
        # Remove UI of playing track
        self.iconLabel.setEnabled(False)
        self.iconLabel.clear()
        self.musicLabel.setEnabled(False)
        self.musicLabel.setText('')
        self.artistLabel.setEnabled(False)
        self.artistLabel.setText('')

    def playButtonClick(self):
        if self.AS.active:
            if self.AS.paused:
                self.AS.resume()
            else:
                self.AS.pause()
        else:
            self.playButton.setChecked(False)
    
    def playTimeSliderRelease(self):
        new_position  = self.playTimeSlider.value()
        self.AS.seek(new_position)
        self.trackTimer.start()
    
    def playTimeSliderValueChange(self):
        slider_time = self.playTimeSlider.value()
        self.timeLabel.setText(Track.getDurationFormat(slider_time))

    def trackTimerUpdate(self):
        currentPosition = int(self.AS.currentPosition)
        self.playTimeSlider.setValue(currentPosition)
    
    def volumeButtonClick(self):
        if self.volumeButton.isChecked():
            self.volumeButton.set_lastVolume(self.AS.volume)
            self.volumeSlider.setValue(0)
        else:
            self.volumeSlider.setValue(self.volumeButton.lastVolume)

    def volumeSliderPressed(self):
        volume = self.volumeSlider.value() 
        if volume != 0:
            self.volumeButton.set_lastVolume(volume)

    def volumeSliderValueChange(self):
        volume = self.volumeSlider.value()
        if volume == 0:
            self.volumeButton.setChecked(True)
        else:
            self.volumeButton.setChecked(False)
        self.AS.set_volume(volume)
        self.volumeButton.update_volume_style(volume)
    
    #------------------------ AudioStreamer Events ------------------------#
    def onTrackStartEvent(self):
        self.enableMediaButtons()
        # Start trackTimer
        self.trackTimer.start()
    
    def onTrackEndEvent(self):
        # Stop trackTimer - Use QMetaObject.invokeMethod to call self.trackTimer.stop on the main thread (it's required) 
        # QMetaObject.invokeMethod(self.trackTimer, "stop", Qt.BlockingQueuedConnection)
        # Disable Media Buttons NOTE: make condition if queue empty?
        self.disableMediaButtons()
        # Remove green text from playing SearchTrackWidget
        if SearchTrackWidget.playing_widget:
                SearchTrackWidget.playing_widget.toggleLabelColor()
                SearchTrackWidget.playing_widget = None

    #------------------------ UI Events ------------------------#
    def mousePressEvent(self, event):
        # Check if the click was outside any SearchTrackWidget
        if SearchTrackWidget.selected_widget:
            widget = SearchTrackWidget.selected_widget
            if not widget.rect().contains(SearchTrackWidget.selected_widget.mapFromGlobal(event.globalPosition().toPoint())):
                widget.setChecked(False)  # Uncheck the currently selected widget
        super().mousePressEvent(event)
    
    def resizeEvent(self, event):
        # Check if the size of BWleftWidget has changed
        if self.BWleftWidget.width() != self.prev_BWleftWidget_width:
            self.resizeActiveTrackLabels()
            self.prev_BWleftWidget_width = self.BWleftWidget.width()
        super().resizeEvent(event)
    
    def resizeActiveTrackLabels(self):
        # Adjust width dynamically
        padding = 76
        available_width = self.BWleftWidget.width() - padding
        # Set the maximum width for the track title
        self.musicLabel.setMaximumWidth(available_width)
        self.artistLabel.setMaximumWidth(available_width)
    
    def closeEvent(self, event):
        self.AS.stop()
        super().closeEvent(event)
    
    #------------------------ Auxiliar Functions ------------------------#



if __name__ == "__main__":
    # Run application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
