import sys
import os
from dotenv import load_dotenv
from PySide6.QtWidgets import QApplication, QMainWindow
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from AudioStreamer.audiostreamerV03 import AudioStreamer
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

        # Set Intial Conditions
        self.homeButton.setChecked(True)
        self.rightStackedWidget.setCurrentWidget(self.RSWhomeWidget)

        # Connect Home and Search buttons to functions
        self.homeButton.clicked.connect(self.homeButtonClick)
        self.searchButton.clicked.connect(self.searchButtonClick)

        # Connect Player Buttons to functions
        self.playButton.clicked.connect(self.playButtonClick)

        # Connect Enter key press in RSWSsearchQLineEdit to a function
        self.RSWSsearchQLineEdit.returnPressed.connect(self.onSearchEnter)

        # Set Utilities
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('SPOTIFYCLIENTID'),
                                               client_secret=os.getenv('SPOTIFYCLIENTSECRET'),
                                               redirect_uri=os.getenv('SPOTIFYREDIRECTURI'),
                                               scope="user-library-read"))
        self.AS = AudioStreamer()
        SearchTrackWidget.set_AudioStreamer(self.AS)
        self.SL = SongLink()
        SearchTrackWidget.set_SongLink(self.SL)


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
    
    def playButtonClick(self):
        if self.AS.active:
            if self.AS.paused:
                self.AS.resume()
            else:
                self.AS.pause()
        else:
            self.playButton.setChecked(False)
        # total_seconds = int(self.AS.current_time)
        # minutes = total_seconds // 60
        # seconds = total_seconds % 60
        # # Format seconds with leading zero if needed
        # print(f"{minutes}:{seconds:02d}")
    
    def clearRSWSscrollVLayout(self):
        SearchTrackWidget.selected_widget = None
        # Loop through and remove each widget from the layout
        while self.RSWSscrollVLayout.count():
            item = self.RSWSscrollVLayout.takeAt(0)
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
            cover_url = item['album']['images'][0]['url']
            spotify_uri = item['uri']
            # Create an instance of SearchTrackWidget
            track_widget = SearchTrackWidget(track, artists_str, cover_url, spotify_uri)
            self.RSWSscrollVLayout.addWidget(track_widget)
    
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
        

if __name__ == "__main__":
    # Run application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
