import sys
import os
import requests
from dotenv import load_dotenv
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, QMetaObject, Qt
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from AudioStreamer.audiostreamerV04 import AudioStreamer
from AudioStreamer.events import TrackStartEvent, TrackEndEvent
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

        # Set Utilities
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('SPOTIFYCLIENTID'),
                                               client_secret=os.getenv('SPOTIFYCLIENTSECRET'),
                                               redirect_uri=os.getenv('SPOTIFYREDIRECTURI'),
                                               scope="user-library-read"))
        self.AS = AudioStreamer()
        SearchTrackWidget.set_AudioStreamer(self.AS)
        self.SL = SongLink()
        SearchTrackWidget.set_SongLink(self.SL)

        # Add AudioStreamer Events
        self.AS.add_event_hook(self.onTrackStartEvent, event=TrackStartEvent)
        self.AS.add_event_hook(self.onTrackEndEvent, event=TrackEndEvent)

        # Set Intial Conditions
        self.homeButton.setChecked(True)
        self.rightStackedWidget.setCurrentWidget(self.RSWhomeWidget)
        self.disableMediaButtons()
        self.volumeSlider.setRange(0, 50) # max Volume
        self.volumeSlider.setValue(self.AS.volume)


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
    def clearRSWSscrollVLayout(self):
        SearchTrackWidget.selected_widget = None
        # Loop through and remove each widget from the layout 
        # except last widget which is the spacer
        for i in range(self.RSWSscrollVLayout.count() - 2, -1, -1):
            item = self.RSWSscrollVLayout.takeAt(i)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()  # Delete the widget from memory
    
    def onSearchEnter(self):
        # Clear all existing track widgets before adding new ones
        self.clearRSWSscrollVLayout()
        # Get text from RSWSsearchQLineEdit when Enter is pressed
        search_text = self.RSWSsearchQLineEdit.text()
        # Spotify API ### MUDAR REQUESTS TODOS PARA .get('','')
        results = self.sp.search(q=search_text, type='track', limit=10)
        for item in results['tracks']['items']:
            artists_str = ', '.join(artist['name'] for artist in item['artists'])
            track = item['name']
            cover_content = requests.get(item['album']['images'][0]['url']).content
            spotify_uri = item['uri']
            # Create an instance of SearchTrackWidget
            track_widget = SearchTrackWidget(track, artists_str, cover_content, spotify_uri)
            self.RSWSscrollVLayout.insertWidget(self.RSWSscrollVLayout.count()-1,track_widget)

    #------------------------ Media Buttons ------------------------#
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
        self.timeLabel.setText(self.get_formated_time(slider_time))

    def trackTimerUpdate(self):
        current_position = int(self.AS.current_position)
        self.playTimeSlider.setValue(current_position)
    
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
        # Enable Media Buttons
        self.playButton.setChecked(True)
        self.playButton.setEnabled(True)
        self.nextTrackButton.setEnabled(True)
        self.previousTrackButton.setEnabled(True)
        self.loopButton.setEnabled(True)
        self.shuffleButton.setEnabled(True)
        self.playTimeSlider.setRange(0, self.AS.duration)
        self.playTimeSlider.setValue(0)
        self.playTimeSlider.setEnabled(True)
        self.timeLabel.setStyleSheet('color: rgb(255, 255, 255);')
        self.timeLabel.setText('0:00')
        self.durationLabel.setStyleSheet('color: rgb(255, 255, 255);')
        self.durationLabel.setText(self.get_formated_time(self.AS.duration))
        # Start trackTimer
        self.trackTimer.start()
    
    def onTrackEndEvent(self):
        # Stop trackTimer - Use QMetaObject.invokeMethod to call self.trackTimer.stop on the main thread (it's required) 
        # QMetaObject.invokeMethod(self.trackTimer, "stop", Qt.BlockingQueuedConnection)
        # Disable Media Buttons NOTE: make condition if queue empty?
        self.disableMediaButtons()

    #------------------------ UI Events ------------------------#
    def mousePressEvent(self, event):
        # Check if the click was outside any SearchTrackWidget
        if SearchTrackWidget.selected_widget:
            widget = SearchTrackWidget.selected_widget
            if not widget.rect().contains(SearchTrackWidget.selected_widget.mapFromGlobal(event.globalPosition().toPoint())):
                widget.setChecked(False)  # Uncheck the currently selected widget
        super().mousePressEvent(event)
    
    def closeEvent(self, event):
        self.AS.stop()
        super().closeEvent(event)
    
    #------------------------ Auxiliar Functions ------------------------#
    @staticmethod
    def get_formated_time(total_seconds):
        total_seconds = int(total_seconds)
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f'{minutes}:{seconds:02d}'



if __name__ == "__main__":
    # Run application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
