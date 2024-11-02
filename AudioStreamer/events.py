class Event:
    """Base class for all AudioStreamer events."""
    def __init__(self):
        self._hooks = []

    def register(self, hook):
        """Register a new hook (callback function) to the event."""
        if hook not in self._hooks:
            self._hooks.append(hook)

    def unregister(self, hook):
        """Unregister a hook from the event."""
        if hook in self._hooks:
            self._hooks.remove(hook)

    def emit(self):
        """Emit the event, calling all registered hooks."""
        for hook in self._hooks:
            hook()


class TrackStartEvent(Event):
    """
    This event is emited when a track begins playing (via AS.play()).
    It is emited after track is loaded in AudioStreamer but before
    stream is opened and activated.
    """
    pass


class TrackEndEvent(Event):
    """
    This event is emited when the player finishes playing a track.
    It is emited after stream is closed.
    """
    pass


class TrackExceptionEvent(Event):
    """
    This event is emitted when a track encounters an exception during playback.
    It is emited before stream is closed.
    """
    pass
