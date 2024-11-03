class AudioStreamerTrack:
    def __init__(self, url=None, duration=None, extra=None):
        self.__url = url
        self.__duration = duration
        self.__extra = {}

    @property
    def url(self):
        return self.__url

    @property
    def duration(self):
        return self.__duration
    
    @property
    def extra(self):
        return self.__extra

    def setUrl(self, new_url):
        self.__url = new_url

    def setDuration(self, new_duration):
        if new_duration > 0:
            self.__duration = new_duration
        else:
            raise ValueError("Duration must be positive.")
    
    def set_extra(self, extra):
        self.__extra = extra