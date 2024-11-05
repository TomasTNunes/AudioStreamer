import sys
import os
import requests
from dotenv import load_dotenv
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, Qt, QPropertyAnimation, QEasingCurve, QRect
from PySide6.QtGui import QColor, QPainter, QBrush

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

        # Disable Default Title Bar
        self.setWindowFlags(Qt.FramelessWindowHint)  # Disable default title bar
        self.setAttribute(Qt.WA_TranslucentBackground)  # Allows transparency

        # Set Custom Title Bar Buttons Functions
        self.closeButton.clicked.connect(self.closeButtonClick)
        #self.minimizeButton.clicked.connect(self.minimizeButtonClick)
        self.maximizeButton.clicked.connect(self.toggleMaximizeButtonClick)
        self._isMaximized = False # window maximized status
        self.saved_geometry = self.geometry()  # Save the initial geometry to restore from maximize

        # Drag Resize Window Variables
        self.setMouseTracking(True)
        self.titleBarHeight = self.tittleBarWidget.height()
        self.edge_margin = 6
        self._resizing = False
        self._resizing_direction = None
        self._start_pos = None
        self._start_geom = None

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
    
    #------------------------- Title Bar Buttons -------------------------#
    def closeButtonClick(self):
        # Fade out animation before closing
        self.close_animation = QPropertyAnimation(self, b"windowOpacity")
        self.close_animation.setDuration(140)
        self.close_animation.setStartValue(1.0)
        self.close_animation.setEndValue(0.0)
        self.close_animation.finished.connect(self.close)
        self.close_animation.start()
    
    # def minimizeButtonClick(self):
    #     # Slide down or fade out animation before minimizing
    #     self.minimize_animation = QPropertyAnimation(self, b"geometry")
    #     self.minimize_animation.setDuration(300)
    #     self.minimize_animation.setStartValue(self.geometry())
    #     self.minimize_animation.setEndValue(QRect(self.x(), self.y() + self.height() // 2, self.width(), 0))
    #     self.minimize_animation.setEasingCurve(QEasingCurve.OutQuint)
    #     self.minimize_animation.finished.connect(self.showMinimized)
    #     self.minimize_animation.start()
    
    def toggleMaximizeButtonClick(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()  # Get available screen geometry
        if self._isMaximized:
            # Add borders radius
            self.centralwidget.setStyleSheet('border-radius: 10px;')
            self.closeButton.setStyleSheet("""  QPushButton {
                                                    background-color: None;  /* Background color */
                                                    border-top-right-radius: 10px;  /* Rounded top-right corner */
                                                    border-top-left-radius: 0px;    /* Square top-left corner */
                                                    border-bottom-right-radius: 0px;  /* Square bottom-right corner */
                                                    border-bottom-left-radius: 0px;   /* Square bottom-left corner */
                                                        }
                                                QPushButton:hover {
                                                    background-color: rgb(255, 0, 0);  /* Background color */
                                                        }
                                                QPushButton:pressed {
                                                    background-color: rgb(139, 0, 0);  /* Background color */
                                                        } 
                                           """)
            # Restore to saved size and position with animation
            self.restore_animation = QPropertyAnimation(self, b"geometry")
            self.restore_animation.setDuration(300)
            self.restore_animation.setStartValue(screen_geometry)  # Start from maximized geometry
            self.restore_animation.setEndValue(self.saved_geometry)  # Restore to saved geometry
            self.restore_animation.setEasingCurve(QEasingCurve.OutQuint)
            self.restore_animation.finished.connect(lambda: setattr(self, "_isMaximized", False))
            self.restore_animation.start()
        else:
            # Save current geometry before maximizing
            self.saved_geometry = self.geometry()
            # Maximize to available screen area with animation
            self.maximize_animation = QPropertyAnimation(self, b"geometry")
            self.maximize_animation.setDuration(300)
            self.maximize_animation.setStartValue(self.geometry())
            self.maximize_animation.setEndValue(screen_geometry)  # Set the animation to expand to available screen geometry
            self.maximize_animation.setEasingCurve(QEasingCurve.OutQuint)
            self.maximize_animation.finished.connect(lambda: setattr(self, "_isMaximized", True))
            self.maximize_animation.start()
            # Remove borders radius
            self.centralwidget.setStyleSheet('border-radius: 0px;')
            self.closeButton.setStyleSheet("""  QPushButton {
                                                    background-color: None;  /* Background color */
                                                    border-radius: 0px;
                                                        }
                                                QPushButton:hover {
                                                    background-color: rgb(255, 0, 0);  /* Background color */
                                                        }
                                                QPushButton:pressed {
                                                    background-color: rgb(139, 0, 0);  /* Background color */}
                                           """)

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
    def onTrackStartEvent(self, event):
        self.enableMediaButtons()
        # Start trackTimer
        self.trackTimer.start()
    
    def onTrackEndEvent(self, event):
        # Stop trackTimer - Use QMetaObject.invokeMethod to call self.trackTimer.stop on the main thread (it's required) 
        # QMetaObject.invokeMethod(self.trackTimer, "stop", Qt.BlockingQueuedConnection)
        # Disable Media Buttons NOTE: make condition if queue empty?
        self.disableMediaButtons()
        # Remove green text from playing SearchTrackWidget
        if SearchTrackWidget.playing_widget:
                SearchTrackWidget.playing_widget.toggleLabelColor()
                SearchTrackWidget.playing_widget = None

    #------------------------ UI Events ------------------------#
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
    
    def mousePressEvent(self, event):
        # Drag/Resize Main Window
        if event.button() == Qt.LeftButton:
            self._resizing_direction = self._detect_edge(event.pos())
            if self._resizing_direction:
                self._start_pos = event.globalPos()
                self._start_geom = self.geometry()
                self._resizing = True
            elif event.pos().y() < self.titleBarHeight:
                # Allow dragging from title bar
                self.oldPos = event.globalPos()
    
        # Check if the click was outside any SearchTrackWidget
        if SearchTrackWidget.selected_widget:
            widget = SearchTrackWidget.selected_widget
            if not widget.rect().contains(SearchTrackWidget.selected_widget.mapFromGlobal(event.globalPosition().toPoint())):
                widget.setChecked(False)  # Uncheck the currently selected widget
        super().mousePressEvent(event)
    
    def mouseMoveEvent(self, event):
        # Drag/Resize Main Window
        if self._resizing:
            self._resize_window(event.globalPos())
        else:
            # If not resizing, check if near edge for resize cursor
            self._set_cursor(self._detect_edge(event.pos()))
            # Handle dragging (only if not resizing)
            if self.oldPos:
                delta = event.globalPos() - self.oldPos
                self.move(self.x() + delta.x(), self.y() + delta.y())
                self.oldPos = event.globalPos()
        super().mouseMoveEvent(event)
    
    def mouseReleaseEvent(self, event):
        # Drag/Resize Main Window
        self._resizing = False
        self._resizing_direction = None
        self.oldPos = None
        super().mouseReleaseEvent(event)
    
    def _resize_window(self, pos):
        delta = pos - self._start_pos
        geom = QRect(self._start_geom)
        # Resizing logic with minimum size checks
        if 'left' in self._resizing_direction:
            geom.setLeft(geom.left() + delta.x())
            # Ensure the width does not go below the minimum width
            if geom.width() < self.minimumWidth():
                geom.setLeft(geom.right() - self.minimumWidth())
        elif 'right' in self._resizing_direction:
            geom.setRight(geom.right() + delta.x())
            # Ensure the width does not go below the minimum width
            if geom.width() < self.minimumWidth():
                geom.setRight(geom.left() + self.minimumWidth())
        if 'top' in self._resizing_direction:
            geom.setTop(geom.top() + delta.y())
            # Ensure the height does not go below the minimum height
            if geom.height() < self.minimumHeight():
                geom.setTop(geom.bottom() - self.minimumHeight())
        elif 'bottom' in self._resizing_direction:
            geom.setBottom(geom.bottom() + delta.y())
            # Ensure the height does not go below the minimum height
            if geom.height() < self.minimumHeight():
                geom.setBottom(geom.top() + self.minimumHeight())
        # Finally, set the geometry
        self.setGeometry(geom)

    def _detect_edge(self, pos):
        """Detect if the mouse is near the window edge, and return the direction."""
        x, y = pos.x(), pos.y()
        w, h = self.width(), self.height()
        margin = self.edge_margin
        # Determine if mouse is in any of the edges
        edges = []
        if x < margin:
            edges.append('left')
        elif x > w - margin:
            edges.append('right')
        if y < margin:
            edges.append('top')
        elif y > h - margin:
            edges.append('bottom')
        return '-'.join(edges)

    def _set_cursor(self, edge):
        """Set the appropriate resize cursor based on the edge detected."""
        if edge == 'left' or edge == 'right':
            self.setCursor(Qt.CursorShape.SizeHorCursor)
        elif edge == 'top' or edge == 'bottom':
            self.setCursor(Qt.CursorShape.SizeVerCursor)
        elif edge in ('top-left', 'bottom-right'):
            self.setCursor(Qt.CursorShape.SizeFDiagCursor)
        elif edge in ('top-right', 'bottom-left'):
            self.setCursor(Qt.CursorShape.SizeBDiagCursor)
        else:
            self.unsetCursor()
    
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
