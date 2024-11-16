import yt_dlp

from AudioStreamer.audiostreamertrack import AudioStreamerTrack

class Track(AudioStreamerTrack):
    #SL = None  # Class variable for the SongLink instance
    YTM = None # Class variable for the YTMusic instance

    def __init__(self, itemResult, url=None, duration=None, extra=None):
        super().__init__(url, duration, extra)
        self._itemResult = itemResult
        self._spotifyId = itemResult.get('id', '')
        self._spotifyUri = itemResult.get('uri', '')
        self._name = itemResult.get('name', '')
        self._artists = [(artist.get('id', ''), artist.get('name', '')) for artist in itemResult.get('artists', [])]
        self._album = (itemResult['album']['id'],itemResult['album']['name'])
        self._cover = itemResult.get('album', {}).get('images', [{}])[0].get('url', '')
        self._spotifyDuration = itemResult.get('duration_ms', 0) / 1000
        self._sl = None
    
    # @classmethod
    # def setSongLink(cls, songlink):
    #     """Set the shared SongLink instance for all Track instances."""
    #     cls.SL = songlink
    
    @classmethod
    def setYTMusic(cls, YTM):
        """Set the shared YTMusic instance for all Track instances."""
        cls.YTM = YTM

    @property
    def name(self):
        return self._name
    
    @property
    def artists(self):
        return ', '.join(artist[1] for artist in self._artists)

    @property
    def cover(self):
        return self._cover
    
    @property
    def spotifyDuration(self):
        return self._spotifyDuration

    @property
    def spotifyDurationFormat(self):
        return self.getDurationFormat(self.spotifyDuration)
    
    @property
    def durationFormat(self):
        return self.getDurationFormat(self.duration)
    
    @staticmethod
    def getDurationFormat(time):
        total_seconds = int(time)
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f'{minutes}:{seconds:02d}'
    
    def getYoutubeAudio(self):
        if not self.url:
            try:
                #self.sl = self.SL.getByUrl(self._spotifyUri)
                #youtube_url = self.sl.entitiesByProvider['youtube'].linksByPlatform['youtubeMusic']
                search_query = f"{self.name} {self.artists}"
                result = self.YTM.search(search_query, filter="songs", limit=1)[0]
                youtube_url = f"https://music.youtube.com/watch?v={result['videoId']}"
                ydl_opts = {
                    'format': 'bestaudio',
                    'noplaylist': True,
                    'quiet': True,
                    'no_warnings': True,
                    'extract_flat': 'in_playlist',
                    }
            
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(youtube_url, download=False)
                self.setUrl(info_dict['url'])
                self.setDuration(int(info_dict['duration']))
            except Exception as e:
                print(f'Fail to get AS Track: {e}')
                return None
