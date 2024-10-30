class AudioStreamerTrack:
    def __init__(self, url=None, duration=None):
        self.__url = url
        self.__duration = duration

    @property
    def url(self):
        return self.__url

    @property
    def duration(self):
        return self.__duration

    def set_url(self, new_url):
        self.__url = new_url

    def set_duration(self, new_duration):
        if new_duration > 0:
            self.__duration = new_duration
        else:
            raise ValueError("Duration must be positive.")