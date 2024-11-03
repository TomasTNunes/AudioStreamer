class TrackQueue():
    def __init__(self):
        self._currentPlaying = None
        self._queue = []
        self._next = []
        self._nextFrom = ''
    
    @property
    def currentPlaying(self):
        return self.currentPlaying

    def addTrack(self, track):
        pass

    def addTrackToQueue(self, track):
        pass

    def shuffle(self):
        pass

    def skip(self):
        pass

    def _clear(self):
        pass