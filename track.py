import requests
import yt_dlp

from AudioStreamer.audiostreamertrack import AudioStreamerTrack

class Track(AudioStreamerTrack):
    SL = None  # Class variable for the SongLink instance

    def __init__(self, itemResult, url=None, duration=None, extra=None):
        super().__init__(url, duration, extra)
        self._itemResult = itemResult
        self._spotifyId = itemResult.get('id', '')
        self._spotifyUri = itemResult.get('uri', '')
        self._name = itemResult.get('name', '')
        self._artists = [(artist.get('id', ''), artist.get('name', '')) for artist in itemResult.get('artists', [])]
        self._album = (itemResult['album']['id'],itemResult['album']['name'])
        self._cover = requests.get(itemResult.get('album', {}).get('images', [{}])[0].get('url', '')).content if itemResult.get('album', {}).get('images', [{}])[0].get('url', '') else b''
        self._spotifyDuration = itemResult.get('duration_ms', 0) * 1000
        self._sl = None
    
    @classmethod
    def setSongLink(cls, songlink):
        """Set the shared SongLink instance for all Track instances."""
        cls.SL = songlink

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
    
    def getYoutubeAudio(self):
        if not self.url:
            try:
                self.sl = self.SL.getByUrl(self._spotifyUri)
                youtube_url = self.sl.entitiesByProvider['youtube'].linksByPlatform['youtubeMusic']
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
